from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk
from customtkinter import *
import mysql.connector
import subprocess
from re import search
import io

# Paleta de Cores -------------------------------------------------------------------------------------------------------

from paleta_cores import *

# Expressões Regulares (Regex) -----------------------------------------------------------------------------------------
# # ^ -> inicio de string
# # $ -> final de string
# # [a-zA-Z0-9._%+-] -> conjunto de caracteres permitidos
# # + -> indica que a expressão anterior deve aparecer uma ou mais vezes
# # ? -> representa a correspondencia de um caractere opcional
# # \w -> corresponde a qualquer caractere alfanúmeico (equivalente a [a-zA-Z0-9_])
# # @ -> separa nome do dominio
# # [a-zA-Z0-9.-] -> conjunto de caracteres permitidos para nome de dominio
# # \ -> '\' caractere de escape utilizado para escapar o '.' que separa o dominio da extensão (o '.' tbm significa qualquer caractere, sendo necessário usar escape)
# # [a-zA-Z]{2,} -> sequencia de dois ou mais (',') caracteres alfabéticos (letras maiusculas e minusculas)

def regex(email, telefone):

    # r' ' -> declaração de string literal (raw), sem processamento de caracteres especiais
    pattern_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    pattern_telefone = r'^\d{9}$'

    # Verifica se o email inserido pelo usúario é válido
    if search(pattern_email, email):
        validaEmail = True
    else:
        validaEmail = False

    if search(pattern_telefone, telefone):
        validaTelefone = True
    else:
        validaTelefone = False

    regex = [validaEmail, validaTelefone]

    return regex

# CRUD com MySQL -------------------------------------------------------------------------------------------------------

def conn():
    # Conexão com o banco de dados
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="PetShop"
    )

    # Criação de cursor
    cursor = mydb.cursor()

    # Verificar se o email já está cadastrado
    cursor.execute("SELECT * FROM Funcionarios WHERE email = %s", (txtEmail.get().lower(),))
    usuario = cursor.fetchone()

    if usuario:
        exibirMsg('E-mail já cadastrado!')
    else:
        # Inserir um novo registro na tabela
        sql = "INSERT INTO Funcionarios (nome, email, telefone, senha, imagem) VALUES (%s, %s, %s, %s, %s)"
        values = (txtNome.get(), txtEmail.get().lower(), txtTelefone.get(), txtSenha.get(), imagem)
        cursor.execute(sql, values)
        mydb.commit()

        id = cursor.lastrowid

        popup("Usuário cadastrado com sucesso!", id)

    # Fechar a conexão
    cursor.close()
    mydb.close()

def limparCampos():
    # Limpar os campos
    txtNome.delete(0, END)
    txtEmail.delete(0, END)
    txtTelefone.delete(0, END)
    txtSenha.delete(0, END)
    txtConfirmarSenha.delete(0, END)

    # Focar no Frame e não no último campo
    formFieldset.focus()

def exibirMsg(msg):
    lblMsg.configure(text=msg)
    lblMsg.grid(row=12, columnspan=2)

def popup(msg, id):
    # Cria uma nova janela (toplevel)
    popup = CTkToplevel(tela)
    popup.title("Mensagem")

    # Posiciona a janela no centro da tela
    w = 280
    h = 150
    ws = tela.winfo_screenwidth()
    hs = tela.winfo_screenheight()
    x = (ws/2) - (280/2)
    y = (hs/2) - (150/2)
    popup.geometry("%dx%d+%d+%d" % (w, h, x, y))
    popup.resizable(False, False)

    lblPopupTitle = CTkLabel(popup, text="Alerta!", font=("arial bold", 18)).pack(pady=(5,0))
    lblPopupMsg = CTkLabel(popup, text=msg, font=("arial", 16)).place(relx=0.5, rely=0.5, anchor=CENTER)
    btnOk = CTkButton(popup, text="Ok", width=50, command=lambda: abrirPaginaInicial(popup, id))
    btnOk.place(relx=1.0, rely=1.0, anchor='se', x=-10, y=-10)

    # Impede que o usuário interaja com a janela principal enquanto o popup estiver aberto
    popup.grab_set()
    popup.mainloop()

# Inserir imagem
def selecionar_imagem():
    filename = askopenfilename()
    with open(filename, "rb") as file:
        global imagem
        imagem = file.read()
    img_data = io.BytesIO(imagem)
    img = Image.open(img_data)
    img_resized = img.resize((50, 50))
    global photo
    photo = ImageTk.PhotoImage(img_resized)
    labelPhoto.configure(image=photo)
        
def abrirPaginaInicial(popup, id):
    tela.withdraw()
    popup.withdraw()
    subprocess.run(['python', 'pagina_inicial.py', str(id)])
    popup.destroy()
    tela.destroy()

# Compara senha

def confirmarSenha(*args):

    # Permite alterar o valor da variavel definida no escopo global
    global validaSenha

    if varSenha.get() == varConfirmarSenha.get():
        exibirMsg("")
        return True
    else:
        exibirMsg("Senhas diferentes!")
        return False

# Create
def cadastrar():
    # Verificar se todos os campos estão preenchidos
    if(len(txtNome.get()) > 0 and len(txtEmail.get()) > 0 and len(txtTelefone.get()) > 0 and len(txtSenha.get()) > 0 and len(txtConfirmarSenha.get()) > 0 and txtSenha.get() != "*****" and txtSenha.get() != "*****"):
        if confirmarSenha():
            validacao = regex(txtEmail.get(), txtTelefone.get())
            if validacao == [True, True]:
                conn()

            elif validacao == [True, False]:
                exibirMsg("Telefone inválido!")
                txtTelefone.focus()
            elif validacao == [False, True]:
                exibirMsg("E-mail inválido!")
                txtEmail.focus()
            else:
                exibirMsg("E-mail e telefone inválidos!")
                txtEmail.focus()
                txtTelefone.focus()
    else:
        exibirMsg("Preencha todos os campos!")


# Configuração de Tela --------------------------------------------------------------------------------------------------

tela = CTk()
tela.title("Petshop Dog's - Cadastro")

largura = 800
altura = 500
largura_screen = tela.winfo_screenwidth()
altura_screen = tela.winfo_screenheight()
posx = largura_screen/2 - largura/2
posy = altura_screen/2 - altura/2

tela.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))
tela.resizable(False, False)

tela._set_appearance_mode("dark")
set_default_color_theme("green")

# Formulário -----------------------------------------------------------------------------------------------------------
user = Image.open("imgs/user.png")
user.thumbnail((35, 30))
userIcon = ImageTk.PhotoImage(user)

formCadastro = CTkFrame(tela, corner_radius=20, width=600, height=450)
formFieldset = CTkFrame(formCadastro, fg_color="transparent")

legend = CTkLabel(formFieldset, text="Cadastro", font=("arial bold", 28))

fotoUser = CTkFrame(formFieldset, width=45, height=45, border_color='e9e9e9')
labelPhoto = CTkLabel(fotoUser, image=userIcon, text="")

lblNome = CTkLabel(formFieldset, text="Nome Completo", font=("arial bold", 16))
txtNome = CTkEntry(formFieldset, placeholder_text="Nome Completo", width=400)

lblEmail = CTkLabel(formFieldset, text="Seu E-mail", font=("arial bold", 16))
txtEmail = CTkEntry(formFieldset, placeholder_text="Seu E-mail", width=200)

lblTelefone = CTkLabel(formFieldset, text="Telefone", font=("arial bold", 16))
txtTelefone = CTkEntry(formFieldset, placeholder_text="Telefone", width=200)

btnSelecionarImagem = CTkButton(formFieldset, text="Selecionar Imagem", command=selecionar_imagem)

lblSenha = CTkLabel(formFieldset, text="Senha", font=("arial bold", 16))
varSenha = StringVar()
txtSenha = CTkEntry(formFieldset, width=200, show="*", textvariable=varSenha)

lblConfirmarSenha = CTkLabel(formFieldset, text="Confirme a Senha", font=("arial bold", 16))
varConfirmarSenha = StringVar()
txtConfirmarSenha = CTkEntry(formFieldset, width=200, show="*", textvariable=varConfirmarSenha)

btnCadastrar = CTkButton(formFieldset, text="Cadastrar", width=100, command=cadastrar)

lblMsg = CTkLabel(formFieldset, text="", font=("ariel bold", 16))

# Configurando os Widgets ----------------------------------------------------------------------------------------------

# Comparação de senhas

varSenha.trace('w', confirmarSenha)
varConfirmarSenha.trace('w', confirmarSenha)

# Gerenciadores

formCadastro.place(relx=0.5, rely=0.5, anchor=CENTER)
formFieldset.place(relx=0.5, rely=0.5, anchor=CENTER)
legend.grid(row=0, column=0, pady=(0, 10), sticky=W)
fotoUser.grid(row=1, column=0, sticky=W)
labelPhoto.place(relx=0.5, rely=0.5, anchor=CENTER)
lblNome.grid(row=2, column=0, sticky=W)
txtNome.grid(row=3, columnspan=2, padx=(0, 5), pady=5, sticky=W)
lblEmail.grid(row=4, column=0, sticky=W)
txtEmail.grid(row=5, column=0, padx=(0, 2), pady=5, sticky=W)
lblTelefone.grid(row=4, column=1, sticky=W)
txtTelefone.grid(row=5, column=1, padx=(2, 0), pady=5, sticky=W)
lblSenha.grid(row=8, column=0, sticky=W)
txtSenha.grid(row=9, column=0, padx=(0, 2), pady=5, sticky=W)
lblConfirmarSenha.grid(row=8, column=1, sticky=W)
txtConfirmarSenha.grid(row=9, column=1, padx=(2, 0), pady=5, sticky=W)
btnSelecionarImagem.grid(row=11, column=0, pady=10, sticky=W)
btnCadastrar.grid(row=12, column=0, pady=10, sticky=W)

# Fim -------------------------------------------------------------------------------------------------------------------

tela.mainloop()