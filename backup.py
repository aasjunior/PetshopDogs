# Importação de Bibliotecas ---------------------------------------------------------------------------------------------

from tkinter import *
from customtkinter import *

# Paleta de Cores -------------------------------------------------------------------------------------------------------

from paleta_cores import *

# Configuração de Tela --------------------------------------------------------------------------------------------------

tela = CTk()
tela.title("Cadastro")
tela.geometry("800x600")
tela.resizable(False, False)

tela._set_appearance_mode("dark")
set_default_color_theme("green")

# Formulário -----------------------------------------------------------------------------------------------------------

formCadastro = CTkFrame(tela, corner_radius=20)
formFieldset = CTkFrame(formCadastro, fg_color="transparent")

legend = CTkLabel(formFieldset, text="Cadastro", font=("arial bold", 28))

txtNome = CTkEntry(formFieldset, placeholder_text="Nome Completo", width=200)
txtSegundoNome = CTkEntry(formFieldset, placeholder_text="Segundo Nome", width=250)

txtEmail = CTkEntry(formFieldset, placeholder_text="Seu E-mail", width=200)

txtTelefoneDDD = CTkEntry(formFieldset, placeholder_text="DDD", width=40)
txtTelefoneNumero = CTkEntry(formFieldset, placeholder_text="Número", width=60)

txtSenha = CTkEntry(formFieldset, placeholder_text="Senha", width=200, show="*")
txtConfirmarSenha = CTkEntry(formFieldset, placeholder_text="Confirmar Senha", width=200, show="*")

btnCadastrar = CTkButton(formFieldset, text="Cadastrar", width=100)

# Configurando os Widgets ----------------------------------------------------------------------------------------------

# Gerenciadores

formCadastro.pack(padx=50, pady=50, fill=BOTH, expand=TRUE)
formFieldset.place(relx=0.5, rely=0.5, anchor=CENTER)
legend.grid(row=0, column=0, pady=(0, 10), sticky=W)
txtNome.grid(row=1, column=0, padx=(0, 5), sticky=W)
txtEmail.grid(row=2, column=0, pady=5, sticky=W)
txtTelefoneDDD.grid(row=3, column=0, pady=5, sticky=W)
txtTelefoneNumero.grid(row=3, column=0, pady=5)
txtSenha.grid(row=4, column=0, pady=5, sticky=W)
txtConfirmarSenha.grid(row=5, column=0, pady=5, sticky=W)
btnCadastrar.grid(row=6, column=0, pady=10, sticky=W)

# Fim -------------------------------------------------------------------------------------------------------------------

tela.mainloop()