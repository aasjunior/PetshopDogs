from tkinter import *
from customtkinter import *
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
import tkinter.messagebox as MessageBox
import mysql.connector
import subprocess
import sys
import io

# Paleta de Cores -------------------------------------------------------------------------------------------------------

from paleta_cores import *

# Funções -------------------------------------------------------------------------------------------------------------
# from rotate_image import *
import cv2
import numpy as np
import os

def selecionar_imagem():
    filename = askopenfilename()
    with open(filename, "rb") as file:
        global imagem_bytes
        imagem_bytes = file.read()

def update_user(id, nome, email, telefone):
    # Conectar ao banco de dados
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="PetShop"
    )

    # Criar um cursor
    cursor = mydb.cursor()

    # Atualizar os dados do usuário com base em seu ID
    query = "UPDATE Funcionarios SET nome = %s, email = %s, telefone = %s WHERE id = %s"
    values = (nome, email, telefone, id)
    cursor.execute(query, values)
    mydb.commit()
    MessageBox.showinfo("Status", "Atualizado com sucesso!")

    mydb.close()


def sair():
    tela.destroy()

def abrirPagina(page, id):
    tela.withdraw()
    subprocess.run(['python', page, str(id)])
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

# id = sys.argv[1]
id = 1

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


# Importando imagens -------------------------------------------------------------------------------------------------
bg_welcome = Image.open("imgs/undraw_welcome_cats_thqn.png")
user = Image.open("imgs/user.png")
edit = Image.open("imgs/edit.png")
dog = Image.open("imgs/dog.png")
calendar = Image.open("imgs/calendar.png")
search = Image.open("imgs/search.png")
rotate = Image.open("imgs/rotate.png")

bg_welcome.thumbnail((500, 500))
user.thumbnail((35, 30))
edit.thumbnail((35, 35))
dog.thumbnail((35, 35))
calendar.thumbnail((35, 35))
search.thumbnail((35, 35))
rotate.thumbnail((35, 35))

banner_welcome = ImageTk.PhotoImage(bg_welcome)
userIcon = ImageTk.PhotoImage(user)
editIcon = ImageTk.PhotoImage(edit)
dogIcon = ImageTk.PhotoImage(dog)
calendarIcon = ImageTk.PhotoImage(calendar)
searchIcon = ImageTk.PhotoImage(search)
rotateIcon = ImageTk.PhotoImage(rotate)

# Header -------------------------------------------------------------------------------------------------------------

header = CTkFrame(tela, width=1000, height=50)

logo = CTkLabel(header, text="Petsop Dog's", font=("arial bold", 18))
btnUser = CTkLabel(header, image=userIcon, text="")
btnSair = CTkLabel(header, text="Sair", font=("arial bold", 16))

# Sidebar ------------------------------------------------------------------------------------------------------------

sidebar = CTkFrame(tela, width=230, height=550)

btnRegisterPet = CTkButton(sidebar, width=220, height=50, text="Consultar Pet's", font=("arial bold", 16), anchor=W, image=dogIcon)
btnServices = CTkButton(sidebar, width=220, height=50, text="Agendar Serviços", font=("arial bold", 16), anchor=W, image=calendarIcon)
btnEdit = CTkButton(sidebar, width=220, height=50, text="Histórico de Consultas", font=("arial bold", 16), anchor=W, image=editIcon)
btnRotateImagem = CTkButton(sidebar, width=220, height=50, text="Rotação de Imagem", font=("arial bold", 16), anchor=W, image=rotateIcon, command=lambda: abrirPagina('pagina_rotate.py',id))
btnMinhaConta = CTkButton(sidebar, width=220, height=50, text="Minha Conta", font=("arial bold", 16), anchor=W, image=userIcon)



# Main ---------------------------------------------------------------------------------------------------------------

main = CTkFrame(tela, width=770, height=550, fg_color="#e9e9e9")
formCadastro = CTkFrame(main, corner_radius=20, width=600, height=500)
formFieldset = CTkFrame(formCadastro, fg_color="transparent")

legend = CTkLabel(formFieldset, text="Atualizar Cadastro", font=("arial bold", 28))

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

btnSalvar = CTkButton(formFieldset, text="Salvar", width=100, command=lambda: update_user(1, txtNome.get(), txtEmail.get(), txtTelefone.get()))

lblMsg = CTkLabel(formFieldset, text="", font=("ariel bold", 16))

if usuario:
    nome, email, telefone, imagem = usuario
    txtNome.insert(0, nome)
    txtEmail.insert(0, email)
    txtTelefone.insert(0, telefone)

# Supondo que os dados da imagem estejam armazenados na variável 'imagem'
img_data = io.BytesIO(imagem)
img = Image.open(img_data)
img_resized = img.resize((40, 40))
photo = ImageTk.PhotoImage(img_resized)

# Criar um rótulo para exibir a imagem
fotoUser = CTkFrame(formFieldset, width=45, height=45, border_color='e9e9e9')
labelPhoto = CTkLabel(fotoUser, image=photo, text="")


# Configurando os Widgets --------------------------------------------------------------------------------------------

# Evento click

btnSair.bind("<Button-1>", lambda event: sair())
logo.bind("<Button-1>", lambda event: abrirPagina('pagina_inicial.py',id))
btnRotateImagem.bind("<Button-1>", lambda event: abrirPagina('pagina_rotate.py',id))

# Cursor Pointer

logo.configure(cursor="hand2")
btnUser.configure(cursor="hand2")
btnSair.configure(cursor="hand2")

btnRegisterPet.configure(cursor="hand2")
btnServices.configure(cursor="hand2")
btnEdit.configure(cursor="hand2")
btnRotateImagem.configure(cursor="hand2")
btnMinhaConta.configure(cursor="hand2")

# Gerenciadores

header.place(x=0, y=0)
logo.place(x=10, y=10)
btnUser.place(x=900, y=10)
btnSair.place(x=940, y=10)

sidebar.place(x=0, y=50)

btnRegisterPet.place(x=5, y=5)
btnServices.place(x=5, y=60)
btnEdit.place(x=5, y=115)
btnRotateImagem.place(x=5, y=170)
btnMinhaConta.place(x=5, y=225)

main.place(x=230, y=50)
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
btnSelecionarImagem.grid(row=11, column=0, pady=10, sticky=W)
btnSalvar.grid(row=13, column=0, pady=10, sticky=W)


# Fim -------------------------------------------------------------------------------------------------------------------

tela.mainloop()