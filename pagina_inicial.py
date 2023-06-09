# Importação de Bibliotecas ---------------------------------------------------------------------------------------------

from tkinter import *
from customtkinter import *
from PIL import Image, ImageTk
import mysql.connector
import subprocess
import sys
import io

# Paleta de Cores -------------------------------------------------------------------------------------------------------

from paleta_cores import *

# Funções -------------------------------------------------------------------------------------------------------------

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

id =1
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
btnMinhaConta = CTkButton(sidebar, width=220, height=50, text="Minha Conta", font=("arial bold", 16), anchor=W, image=userIcon, command=lambda: abrirPagina('minha_conta.py',id))


# Main ---------------------------------------------------------------------------------------------------------------

main = CTkFrame(tela, width=770, height=550, fg_color="#e9e9e9")
txtSearch = CTkEntry(main, width=400, height=40, placeholder_text="Pesquisar")
btnSearch = CTkButton(main, width=50, height=40, image=searchIcon, text="")
bg_image = CTkLabel(main, image=banner_welcome, width=500, text="")

# Configurando os Widgets --------------------------------------------------------------------------------------------

# Evento click
btnSair.bind("<Button-1>", lambda event: sair())

# Cursor Pointer

logo.configure(cursor="hand2")
btnUser.configure(cursor="hand2")
btnSair.configure(cursor="hand2")

btnRegisterPet.configure(cursor="hand2")
btnServices.configure(cursor="hand2")
btnEdit.configure(cursor="hand2")
btnRotateImagem.configure(cursor="hand2")
btnMinhaConta.configure(cursor="hand2")

# Vincular o evento <Button-1> ao frame
btnRotateImagem.bind("<Button-1>", lambda event: abrirPagina('pagina_rotate.py',id))
btnMinhaConta.bind("<Button-1>", lambda event: abrirPagina('minha_conta.py',id))


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
txtSearch.place(x=20, y=20)
btnSearch.place(x=420, y=20)
bg_image.place(relx=0.5, rely=0.5, anchor=CENTER)

# Fim -------------------------------------------------------------------------------------------------------------------

tela.mainloop()