from tkinter import *
from customtkinter import *
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
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

angle = 0

def rotate_photo(photo):
    global angle
    angle -= 45
    # Convert the PhotoImage to a PIL Image
    pil_image = ImageTk.getimage(photo)

    # Rotate the image
    rotated_image = pil_image.rotate(angle)

    # Convert the rotated image back to a PhotoImage
    rotated_photo = ImageTk.PhotoImage(rotated_image)

    # Update the canvas item with the rotated image
    canvas.itemconfigure(image_canvas, image=rotated_photo)
    canvas.image = rotated_photo


def selecionar_imagem():
    filename = askopenfilename()
    with open(filename, "rb") as file:
        global imagem_bytes
        imagem_bytes = file.read()

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

if usuario:
    nome, email, telefone, imagem = usuario

# Supondo que os dados da imagem estejam armazenados na variável 'imagem'
img_data = io.BytesIO(imagem)
img = Image.open(img_data)
img_resized = img.resize((200, 200))
photo = ImageTk.PhotoImage(img_resized)

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

btnRotateImagem = CTkFrame(sidebar, width=240, height=50)
iconRotateImagem = CTkLabel(btnRotateImagem, image=rotateIcon, text="")
lblRotateImagem = CTkLabel(btnRotateImagem, text="Rotação de Imagem", font=("arial bold", 16))

btnMinhaConta = CTkFrame(sidebar, width=240, height=50)
iconMinhaConta = CTkLabel(btnMinhaConta, image=userIcon, text="")
lblMinhaConta = CTkLabel(btnMinhaConta, text="Minha Conta", font=("arial bold", 16))


# Main ---------------------------------------------------------------------------------------------------------------

main = CTkFrame(tela, width=750, height=550, fg_color="#e9e9e9")
title = CTkLabel(main, text="Rotacionar a imagem", font=("arial bold", 24), text_color="#000000")
btnsImage = CTkFrame(main, width=300, height=50, fg_color="#e9e9e9")

canvas_width = 600
canvas_height = 300
canvas = Canvas(main, width=canvas_width, height=canvas_height)
canvas.pack()

# Calculate the coordinates for centering the image
center_x = canvas_width // 2
center_y = canvas_height // 2

image_canvas = canvas.create_image(center_x, center_y, anchor="center")
canvas.itemconfigure(image_canvas, image=photo)
canvas.image = photo

# create the select image button
select_image_button = CTkButton(btnsImage, text="Selecione a imagem", command=selecionar_imagem)

# create the rotate image button

rotate_button = CTkButton(btnsImage, text="Rotacionar", command=lambda: rotate_photo(photo))

# Configurando os Widgets --------------------------------------------------------------------------------------------

# Evento click

btnSair.bind("<Button-1>", lambda event: sair())
btnMinhaConta.bind("<Button-1>", lambda event: abrirPagina('minha_conta.py',id))

# Cursor Pointer

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
iconRegisterPet.place(x=15, y=10)
lblRegisterPet.place(x=50, y=15)

btnServices.place(x=5, y=60)
iconServices.place(x=15, y=10)
lblServices.place(x=50, y=15)

btnEdit.place(x=5, y=115)
iconEdit.place(x=15, y=10)
lblEdit.place(x=50, y=15)

btnRotateImagem.place(x=5, y=170)
iconRotateImagem.place(x=15, y=10)
lblRotateImagem.place(x=50, y=15)

btnMinhaConta.place(x=5, y=225)
iconMinhaConta.place(x=15, y=10)
lblMinhaConta.place(x=50, y=15)

main.place(x=250, y=50)
title.place(x=100, y=50)
canvas.place(relx=0.5, y=300, anchor=CENTER)
btnsImage.place(relx=0.5, y=400, anchor=CENTER)
select_image_button.place(x=0, y=0)
rotate_button.place(x=150, y=0)

# Fim -------------------------------------------------------------------------------------------------------------------

tela.mainloop()