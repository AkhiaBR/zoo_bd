# IMPORT DAS BIBLIOTECAS
from tkinter import *
from tkinter import messagebox

# CRIAR JANELA DO TKINTER
window = Tk()

window.title("The Gurizes Development LTDA - Painel de Acesso") # título da janela
window.geometry("900x600") # define o tamanho da janela
window.resizable(width=False,height=False) # retira o redimensionar da janela
window.configure(background="darkorange") # configura a cor do background

# IMAGENS
arca_logo = PhotoImage(file="tkinter_gui/images/arca_white.png")

# WIDGETS
top_frame = Frame(window, width=900, height=150, bg="black", relief="raised")
top_frame.pack(side=TOP)

logo_label = Label(top_frame, image=arca_logo, bg="black")
logo_label.place(x=40, y=20)

title_label = Label(top_frame, text="ZOOLÓGICO ARCA DE NOÉ", font=("Century Gothic", 20), bg="black", fg="white")
title_label.place(x=280, y=55)

menu_label = Label(window, text="MENU DE OPÇÕES", font=("Century Gothic", 20, "bold"), width=20 , bg="darkorange", fg="black")
menu_label.pack(pady=(60,0)) # utilizei somente o pack() para centralizar / padding Y, primeiro valor top, segundo valor bottom

cad_button = Button(window, text="CADASTRAR", font=("Century Gothic", 15, "bold"), width=20 , bg="black", fg="darkorange", relief="raised")
cad_button.pack(pady=5)
alt_button = Button(window, text="ALTERAR", font=("Century Gothic", 15, "bold"), width=20 , bg="black", fg="darkorange", relief="raised")
alt_button.pack(pady=5)
ex_button = Button(window, text="EXCLUIR", font=("Century Gothic", 15, "bold"), width=20 , bg="black", fg="darkorange", relief="raised")
ex_button.pack(pady=5)
pes_button = Button(window, text="PESQUISAR", font=("Century Gothic", 15, "bold"), width=20 , bg="black", fg="darkorange", relief="raised")
pes_button.pack(pady=5)

bottom_frame = Frame(window, width=900, height=70, bg="black", relief="raised")
bottom_frame.pack(side=BOTTOM)

window.mainloop() # fim dos comandos para a janela

