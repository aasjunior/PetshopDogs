# Importação de Bibliotecas ---------------------------------------------------------------------------------------------

from tkinter import *
from customtkinter import *
from PIL import Image, ImageTk
import mysql.connector
import sys
import io

# Paleta de Cores -------------------------------------------------------------------------------------------------------

from paleta_cores import *

# Funções -------------------------------------------------------------------------------------------------------------

def sair():
    tela.destroy()

# Configuração de Tela --------------------------------------------------------------------------------------------------

tela = CTk()
tela.title("Petshop Dog's - Pagina Inicial")

largura = 1000
altura = 600
largura_screen = tela.winfo_screenwidth()
altura_screen = tela.winfo_screenheight()
posx = largura_screen/2 - largura/2
posy = altura_screen/2 - altura/2

tela.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))
tela.resizable(False, False)

tela._set_appearance_mode("dark")
set_default_color_theme("green")

id = sys.argv[1]
# Conectar ao banco de dados
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="PetShop"
)

# Criar um cursor
cursor = mydb.cursor()

# Consultar os dados do usuário com base em seu ID
query = "SELECT nome, email, telefone, imagem FROM Funcionarios WHERE id = %s"
values = (id,)
cursor.execute(query, values)
usuario = cursor.fetchone()

if usuario:
    nome, email, telefone, imagem = usuario

# Supondo que os dados da imagem estejam armazenados na variável 'imagem'
img_data = io.BytesIO(imagem)
img = Image.open(img_data)
photo = ImageTk.PhotoImage(img)

# Criar um rótulo para exibir a imagem
label = CTkLabel(tela, image=photo)

# Importando imagens -------------------------------------------------------------------------------------------------
bg_welcome = Image.open("imgs/undraw_welcome_cats_thqn.png")
user = Image.open("imgs/user.png")
edit = Image.open("imgs/edit.png")
dog = Image.open("imgs/dog.png")
calendar = Image.open("imgs/calendar.png")
search = Image.open("imgs/search.png")

bg_welcome.thumbnail((500, 500))
user.thumbnail((35, 30))
edit.thumbnail((35, 35))
dog.thumbnail((35, 35))
calendar.thumbnail((35, 35))
search.thumbnail((35, 35))

banner_welcome = ImageTk.PhotoImage(bg_welcome)
userIcon = ImageTk.PhotoImage(user)
editIcon = ImageTk.PhotoImage(edit)
dogIcon = ImageTk.PhotoImage(dog)
calendarIcon = ImageTk.PhotoImage(calendar)
searchIcon = ImageTk.PhotoImage(search)

# Header -------------------------------------------------------------------------------------------------------------

header = CTkFrame(tela, width=1000, height=50)

logo = CTkLabel(header, text="Petsop Dog's", font=("arial bold", 18))
btnUser = CTkLabel(header, image=userIcon, text="")
btnSair = CTkLabel(header, text="Sair", font=("arial bold", 16))

# Sidebar ------------------------------------------------------------------------------------------------------------

sidebar = CTkFrame(tela, width=250, height=550)

btnRegisterPet = CTkFrame(sidebar, width=240, height=50)
iconRegisterPet = CTkLabel(btnRegisterPet, image=dogIcon, text="")
lblRegisterPet = CTkLabel(btnRegisterPet, text="Consultar Pet's", font=("arial bold", 16))

btnServices = CTkFrame(sidebar, width=240, height=50)
iconServices = CTkLabel(btnServices, image=calendarIcon, text="")
lblServices = CTkLabel(btnServices, text="Agendar Serviços", font=("arial bold", 16))

btnEdit = CTkFrame(sidebar, width=240, height=50)
iconEdit = CTkLabel(btnEdit, image=editIcon, text="edit")
lblEdit = CTkLabel(btnEdit, text="Histórico de Consultas", font=("arial bold", 16))

btnMinhaConta = CTkFrame(sidebar, width=240, height=50)
iconMinhaConta = CTkLabel(btnMinhaConta, image=userIcon, text="Minha Conta")
lblMinhaConta = CTkLabel(btnMinhaConta, text="Histórico de Consultas", font=("arial bold", 16))

# Main ---------------------------------------------------------------------------------------------------------------

formCadastro = CTkFrame(tela, corner_radius=20)
formFieldset = CTkFrame(formCadastro, fg_color="transparent")

legend = CTkLabel(formFieldset, text="Cadastro", font=("arial bold", 28))

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

# Configurando os Widgets --------------------------------------------------------------------------------------------

# Evento click

btnSair.bind("<Button-1>", lambda event: sair())

# Cursor Pointer

btnUser.configure(cursor="hand2")
btnSair.configure(cursor="hand2")

btnRegisterPet.configure(cursor="hand2")
btnServices.configure(cursor="hand2")
btnEdit.configure(cursor="hand2")
btnMinhaConta.configure(cursor="hand2")

# Gerenciadores

header.place(x=0, y=0)
logo.place(x=10, y=10)
btnUser.place(x=900, y=10)
btnSair.place(x=940, y=10)

sidebar.place(x=0, y=50)

btnRegisterPet.place(x=5, y=5)
iconRegisterPet.place(x=15, y=10)
lblRegisterPet.place(x=50, y=15)

btnServices.place(x=5, y=60)
iconServices.place(x=15, y=10)
lblServices.place(x=50, y=15)

btnEdit.place(x=5, y=115)
iconEdit.place(x=15, y=10)
lblEdit.place(x=50, y=15)

btnMinhaConta.place(x=5, y=160)
iconMinhaConta.place(x=15, y=10)
lblMinhaConta.place(x=50, y=15)

formCadastro.pack(padx=100, pady=50, fill=BOTH, expand=TRUE)
formFieldset.place(relx=0.5, rely=0.5, anchor=CENTER)
legend.grid(row=0, column=0, pady=(0, 10), sticky=W)
lblNome.grid(row=1, column=0, sticky=W)
txtNome.grid(row=2, columnspan=2, padx=(0, 5), pady=5, sticky=W)
lblEmail.grid(row=3, column=0, sticky=W)
txtEmail.grid(row=4, column=0, padx=(0, 2), pady=5, sticky=W)
lblTelefone.grid(row=3, column=1, sticky=W)
txtTelefone.grid(row=4, column=1, padx=(2, 0), pady=5, sticky=W)
lblSenha.grid(row=7, column=0, sticky=W)
txtSenha.grid(row=8, column=0, padx=(0, 2), pady=5, sticky=W)
lblConfirmarSenha.grid(row=7, column=1, sticky=W)
txtConfirmarSenha.grid(row=8, column=1, padx=(2, 0), pady=5, sticky=W)
btnSelecionarImagem.grid(row=10, column=0, pady=10, sticky=W)
btnCadastrar.grid(row=12, column=0, pady=10, sticky=W)

# Fim -------------------------------------------------------------------------------------------------------------------

tela.mainloop()