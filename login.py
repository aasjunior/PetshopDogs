# Importação de Bibliotecas ---------------------------------------------------------------------------------------------

from tkinter import *
from customtkinter import *
from pymongo import MongoClient
import subprocess

# Paleta de Cores -------------------------------------------------------------------------------------------------------

from paleta_cores import *


# Funções --------------------------------------------------------------------------------------------------------------

def registrarUsuario():
    tela.withdraw()
    subprocess.run(['python', 'cadastrar.py'])
    tela.destroy()

def logar():
    # Conexão com o banco de dados
    client = MongoClient('localhost', 27017)

    # Seleciona o banco de dados
    db = client['PetShop']

    # Armazena a coleção
    collection = db['Funcionarios']

    usuario = collection.find_one({'email': txtEmail.get(), 'senha': txtSenha.get()})

    if usuario:
        tela.withdraw()
        subprocess.run(['python', 'pagina_inicial.py'])
        tela.destroy()
    else:
        msg.configure(text="Usuário ou senha inválida")
        msg.pack()

# Configuração de Tela --------------------------------------------------------------------------------------------------

tela = CTk()
tela.title("Login")

largura = 600
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

formLogin = CTkFrame(tela, corner_radius=20)
formFieldset = CTkFrame(formLogin, fg_color="transparent")
formBtns = CTkFrame(formFieldset, fg_color="transparent")

legend = CTkLabel(formFieldset, text="Fazer Login", font=("arial bold", 16))

txtEmail = CTkEntry(formFieldset, placeholder_text="Seu E-mail", width=210)
txtSenha = CTkEntry(formFieldset, placeholder_text="Sua Senha", show='*', width=210)

btnLogin = CTkButton(formBtns, text="Login", fg_color=green, width=100, command=lambda: logar())
btnRegistrar = CTkButton(formBtns, text="Registrar", fg_color="transparent", border_width=2, border_color="gray", width=100, command=lambda: registrarUsuario())
btnEsqueceuSenha = CTkLabel(formBtns, text="Esqueceu a Senha")

msg = CTkLabel(formFieldset, text="", font=("ariel bold", 12))

# Configurando os Widgets --------------------------------------------------------------------------------------------

# Cursor Pointer

btnEsqueceuSenha.configure(cursor="hand2")

# Adicionando efeito hover ao botão

def on_enter(e):
    btnEsqueceuSenha.configure(text_color=light_green)
def on_leave(e):
    btnEsqueceuSenha.configure(text_color="white")

# Associando evento Enter e Leave ao botão

btnEsqueceuSenha.bind("<Enter>", on_enter)
btnEsqueceuSenha.bind("<Leave>", on_leave)

# Gerenciadores

formLogin.pack(padx=150, pady=110, fill=BOTH, expand=TRUE)
formFieldset.place(relx=0.5, rely=0.5, anchor=CENTER)
legend.pack(pady=(10, 20))
txtEmail.pack(pady=(0, 10))
txtSenha.pack(pady=(0, 10))
formBtns.pack(pady=(10, 10))
btnEsqueceuSenha.pack(pady=(5,0), side=BOTTOM)
btnLogin.pack(padx=(0, 5), pady=(0, 5), side=LEFT)
btnRegistrar.pack(padx=(5, 0), pady=(0, 5), side=RIGHT)

# Fim -------------------------------------------------------------------------------------------------------------------

tela.mainloop()