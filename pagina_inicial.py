# Importação de Bibliotecas ---------------------------------------------------------------------------------------------

from tkinter import *
from customtkinter import *
from PIL import Image, ImageTk

# Paleta de Cores -------------------------------------------------------------------------------------------------------

from paleta_cores import *

# Funções -------------------------------------------------------------------------------------------------------------

def sair():
    tela.destroy()

# Configuração de Tela --------------------------------------------------------------------------------------------------

tela = CTk()
tela.title("Petshop Dog's - Pagina Inicial")
tela.geometry("1000x600")
tela.resizable(False, False)

tela._set_appearance_mode("dark")
set_default_color_theme("green")

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

# Main ---------------------------------------------------------------------------------------------------------------

main = CTkFrame(tela, width=750, height=550, fg_color="#e9e9e9")
txtSearch = CTkEntry(main, width=400, height=40, placeholder_text="Pesquisar")
btnSearch = CTkButton(main, width=50, height=40, image=searchIcon, text="")
bg_image = CTkLabel(main, image=banner_welcome, width=500, text="")

# Configurando os Widgets --------------------------------------------------------------------------------------------

# Evento click

btnSair.bind("<Button-1>", lambda event: sair())

# Cursor Pointer

btnUser.configure(cursor="hand2")
btnSair.configure(cursor="hand2")

btnRegisterPet.configure(cursor="hand2")
btnServices.configure(cursor="hand2")
btnEdit.configure(cursor="hand2")

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

main.place(x=250, y=50)
txtSearch.place(x=20, y=20)
btnSearch.place(x=420, y=20)
bg_image.place(relx=0.5, rely=0.5, anchor=CENTER)

# Fim -------------------------------------------------------------------------------------------------------------------

tela.mainloop()