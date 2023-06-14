from tkinter import *
from customtkinter import *
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
import tkinter.messagebox as MessageBox
import mysql.connector
import sys
import io

# Paleta de Cores -------------------------------------------------------------------------------------------------------

from paleta_cores import *

# Funções -------------------------------------------------------------------------------------------------------------
# from rotate_image import *
import cv2
import numpy as np
import os

# def rotate_image(image, angle):
#     # obter a altura e a largura da imagem
#     height, width = image.shape[:2]
#     # get the center point of the image
#     center = (width / 2, height / 2)
#     # get the rotation matrix
#     rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
#     # rotate the image
#     rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height), borderValue=(255, 255, 255))
#     # adjust the position of the rotated image
#     rotated_center = np.dot(rotation_matrix, [center[0], center[1], 1])
#     x_diff = center[0] - rotated_center[0]
#     y_diff = center[1] - rotated_center[1]
#     translation_matrix = np.float32([[1, 0, x_diff], [0, 1, y_diff]])
#     translated_image = cv2.warpAffine(rotated_image, translation_matrix, (width, height), borderValue=(255, 255, 255))
#     return translated_image

# def select_image():
#     global image_path
#     global image
#     global rotated_image
#     # open a file dialog to select the image
#     image_path = filedialog.askopenfilename()
#     # load the image
#     image = cv2.imread(image_path)
#     # rotate the image to the initial position
#     rotated_image = rotate_image(image, 0)
#     # show the initial image
#     show_image(rotated_image)

# def rotate_image_handler():
#     global rotated_image
#     angle = 45  # or any other desired angle
#     rotated_image = rotate_image(rotated_image, angle)
#     show_image(rotated_image)

# def show_image(image):
#     image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#     image_pil = Image.fromarray(image)
#     image_tk = CTkImage(image_pil)
#     canvas.itemconfigure(image_canvas, image=image_tk)
#     canvas.image = image_tk

# def show_image_pil(image_pil):
#     image_tk = ImageTk.PhotoImage(image_pil)
#     canvas.itemconfigure(image_canvas, image=image_tk)
#     canvas.image = image_tk

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