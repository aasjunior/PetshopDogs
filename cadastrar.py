# Importação de Bibliotecas ---------------------------------------------------------------------------------------------

from tkinter import *
from customtkinter import *
from pymongo import MongoClient
from re import *

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

def validaEmail(email):

    # r' ' -> declaração de string literal (raw), sem processamento de caracteres especiais
    pattern_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    # Verifica se o email inserido pelo usúario é válido
    if search(pattern_email, email):
        return True
    else:
        return False

# CRUD com MongoDB -----------------------------------------------------------------------------------------------------

# Conexão com o banco de dados
client = MongoClient('localhost', 27017)

# Seleciona o banco de dados
db = client['PetShop']

# Armazena a coleção
collection = db['Funcionarios']

# Create
def cadastrar():

    email = txtEmail.get()

    if validaEmail(email):
        # Cria um novo documento na coleção
        collection.insert_one({
            'nome': txtNome.get(),
            'email': txtEmail.get(),
            'telefone': txtTelefone.get(),
            'senha': txtSenha.get()
        })

        # Limpar os campos
        txtNome.delete(0, END)
        txtEmail.delete(0, END)
        txtTelefone.delete(0, END)
        txtSenha.delete(0, END)
        txtConfirmarSenha.delete(0, END)

        # Focar no Frame e não no último campo
        formFieldset.focus()

    else:
        msg.configure(text="E-mail inválido")
        msg.grid(row=12, columnspan=2)
        txtEmail.focus()
        txtEmail.configure(border_color="red")

# Configuração de Tela --------------------------------------------------------------------------------------------------

tela = CTk()
tela.title("Petshop Dog's - Cadastro")
tela.geometry("800x500")
tela.resizable(False, False)

tela._set_appearance_mode("dark")
set_default_color_theme("green")

# Formulário -----------------------------------------------------------------------------------------------------------

formCadastro = CTkFrame(tela, corner_radius=20)
formFieldset = CTkFrame(formCadastro, fg_color="transparent")

legend = CTkLabel(formFieldset, text="Cadastro", font=("arial bold", 28))

lblNome = CTkLabel(formFieldset, text="Nome Completo", font=("arial bold", 16))
txtNome = CTkEntry(formFieldset, placeholder_text="Nome Completo", width=400)

lblEmail = CTkLabel(formFieldset, text="Seu E-mail", font=("arial bold", 16))
txtEmail = CTkEntry(formFieldset, placeholder_text="Seu E-mail", width=200)

lblTelefone = CTkLabel(formFieldset, text="Telefone", font=("arial bold", 16))
txtTelefone = CTkEntry(formFieldset, placeholder_text="(99) 99999-9999", width=200)


lblSenha = CTkLabel(formFieldset, text="Senha", font=("arial bold", 16))
txtSenha = CTkEntry(formFieldset, placeholder_text="Senha", width=200, show="*")

lblConfirmarSenha = CTkLabel(formFieldset, text="Confirme a Senha", font=("arial bold", 16))
txtConfirmarSenha = CTkEntry(formFieldset, placeholder_text="Confirmar Senha", width=200, show="*")

btnCadastrar = CTkButton(formFieldset, text="Cadastrar", width=100, command=cadastrar)

msg = CTkLabel(formFieldset, text="", font=("ariel bold", 16))

# Configurando os Widgets ----------------------------------------------------------------------------------------------

# Gerenciadores

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
btnCadastrar.grid(row=11, column=0, pady=10, sticky=W)

# Fim -------------------------------------------------------------------------------------------------------------------

tela.mainloop()