# IMPORT DAS BIBLIOTECAS
from tkinter import *
from tkinter import messagebox

# JANELA PRINCIPAL
def main_window():
    # CRIAR JANELA DO TKINTER
    global window
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

    cad_button = Button(window, text="CADASTRAR", font=("Century Gothic", 15, "bold"), width=20 , bg="black", fg="darkorange", relief="raised", command=abrir_cadastro)
    cad_button.pack(pady=5)
    alt_button = Button(window, text="ALTERAR", font=("Century Gothic", 15, "bold"), width=20 , bg="black", fg="darkorange", relief="raised", command=abrir_alterar)
    alt_button.pack(pady=5)
    ex_button = Button(window, text="EXCLUIR", font=("Century Gothic", 15, "bold"), width=20 , bg="black", fg="darkorange", relief="raised", command=abrir_excluir)
    ex_button.pack(pady=5)
    pes_button = Button(window, text="PESQUISAR", font=("Century Gothic", 15, "bold"), width=20 , bg="black", fg="darkorange", relief="raised", command=abrir_pesquisar)
    pes_button.pack(pady=5)

    bottom_frame = Frame(window, width=900, height=70, bg="black", relief="raised")
    bottom_frame.pack(side=BOTTOM)

    window.mainloop() # fim dos comandos para a janela

# JANELAS SECUNDÁRIAS
def abrir_cadastro ():
    def voltar():
        window_cadastro.destroy()
        main_window()

    window.destroy()

    window_cadastro = Tk()

    window_cadastro.title("The Gurizes Development LTDA - Painel de Cadastro")
    window_cadastro.geometry("900x600")
    window_cadastro.resizable(width=False,height=False)
    window_cadastro.configure(background="darkorange")

    arca_logo = PhotoImage(file="tkinter_gui/images/arca_white.png")
    top_frame = Frame(window_cadastro, width=900, height=150, bg="black", relief="raised")
    top_frame.pack(side=TOP)

    logo_label = Label(top_frame, image=arca_logo, bg="black")
    logo_label.place(x=40, y=20)

    title_label = Label(top_frame, text="ZOOLÓGICO ARCA DE NOÉ", font=("Century Gothic", 20), bg="black", fg="white")
    title_label.place(x=280, y=55)

    back_image = PhotoImage(file="tkinter_gui/images/back_20.png")

    back_label = Button(window_cadastro, image=back_image, bg="darkorange", command=voltar)
    back_label.place(x=40, y=180)

    menu_label = Label(window_cadastro, text="O QUE VOCÊ DESEJA CADASTRAR?", font=("Century Gothic", 20, "bold"), width=30 , bg="darkorange", fg="black")
    menu_label.pack(pady=(30,0)) # utilizei somente o pack() para centralizar / padding Y, primeiro valor top, segundo valor bottom

    cad_button = Button(window_cadastro, text="ANIMAL", font=("Century Gothic", 15, "bold"), width=20 , bg="black", fg="darkorange", relief="raised", command="")
    cad_button.pack(pady=5)
    alt_button = Button(window_cadastro, text="FUNCIONÁRIO", font=("Century Gothic", 15, "bold"), width=20 , bg="black", fg="darkorange", relief="raised", command="")
    alt_button.pack(pady=5)
    ex_button = Button(window_cadastro, text="HABITAT", font=("Century Gothic", 15, "bold"), width=20 , bg="black", fg="darkorange", relief="raised", command="")
    ex_button.pack(pady=5)
    pes_button = Button(window_cadastro, text="INGRESSO", font=("Century Gothic", 15, "bold"), width=20 , bg="black", fg="darkorange", relief="raised", command="")
    pes_button.pack(pady=5)
    pes_button = Button(window_cadastro, text="LOJA", font=("Century Gothic", 15, "bold"), width=20 , bg="black", fg="darkorange", relief="raised", command="")
    pes_button.pack(pady=5)
    pes_button = Button(window_cadastro, text="VISITANTE", font=("Century Gothic", 15, "bold"), width=20 , bg="black", fg="darkorange", relief="raised", command="")
    pes_button.pack(pady=5)

    bottom_frame = Frame(window_cadastro, width=900, height=70, bg="black", relief="raised")
    bottom_frame.pack(side=BOTTOM)

    window_cadastro.mainloop()

def abrir_alterar ():
    def voltar():
        window_alteracao.destroy()
        main_window()

    window.destroy()

    window_alteracao = Tk()

    window_alteracao.title("The Gurizes Development LTDA - Painel de Alteração")
    window_alteracao.geometry("900x600")
    window_alteracao.resizable(width=False,height=False)
    window_alteracao.configure(background="darkorange")

    arca_logo = PhotoImage(file="tkinter_gui/images/arca_white.png")
    top_frame = Frame(window_alteracao, width=900, height=150, bg="black", relief="raised")
    top_frame.pack(side=TOP)

    logo_label = Label(top_frame, image=arca_logo, bg="black")
    logo_label.place(x=40, y=20)

    title_label = Label(top_frame, text="ZOOLÓGICO ARCA DE NOÉ", font=("Century Gothic", 20), bg="black", fg="white")
    title_label.place(x=280, y=55)

    back_image = PhotoImage(file="tkinter_gui/images/back_20.png")

    back_label = Button(window_alteracao, image=back_image, bg="darkorange", command=voltar)
    back_label.place(x=40, y=180)

    menu_label = Label(window_alteracao, text="O QUE VOCÊ DESEJA ALTERAR?", font=("Century Gothic", 20, "bold"), width=30 , bg="darkorange", fg="black")
    menu_label.pack(pady=(30,0)) # utilizei somente o pack() para centralizar / padding Y, primeiro valor top, segundo valor bottom

    cad_button = Button(window_alteracao, text="ANIMAL", font=("Century Gothic", 15, "bold"), width=20 , bg="black", fg="darkorange", relief="raised", command="")
    cad_button.pack(pady=5)
    alt_button = Button(window_alteracao, text="FUNCIONÁRIO", font=("Century Gothic", 15, "bold"), width=20 , bg="black", fg="darkorange", relief="raised", command="")
    alt_button.pack(pady=5)
    ex_button = Button(window_alteracao, text="HABITAT", font=("Century Gothic", 15, "bold"), width=20 , bg="black", fg="darkorange", relief="raised", command="")
    ex_button.pack(pady=5)
    pes_button = Button(window_alteracao, text="INGRESSO", font=("Century Gothic", 15, "bold"), width=20 , bg="black", fg="darkorange", relief="raised", command="")
    pes_button.pack(pady=5)
    pes_button = Button(window_alteracao, text="LOJA", font=("Century Gothic", 15, "bold"), width=20 , bg="black", fg="darkorange", relief="raised", command="")
    pes_button.pack(pady=5)
    pes_button = Button(window_alteracao, text="VISITANTE", font=("Century Gothic", 15, "bold"), width=20 , bg="black", fg="darkorange", relief="raised", command="")
    pes_button.pack(pady=5)

    bottom_frame = Frame(window_alteracao, width=900, height=70, bg="black", relief="raised")
    bottom_frame.pack(side=BOTTOM)

    window_alteracao.mainloop()

def abrir_excluir ():
    def voltar():
        window_excluir.destroy()
        main_window()

    window.destroy()

    window_excluir = Tk()

    window_excluir.title("The Gurizes Development LTDA - Painel de Exclusão")
    window_excluir.geometry("900x600")
    window_excluir.resizable(width=False,height=False)
    window_excluir.configure(background="darkorange")

    arca_logo = PhotoImage(file="tkinter_gui/images/arca_white.png")
    top_frame = Frame(window_excluir, width=900, height=150, bg="black", relief="raised")
    top_frame.pack(side=TOP)

    logo_label = Label(top_frame, image=arca_logo, bg="black")
    logo_label.place(x=40, y=20)

    title_label = Label(top_frame, text="ZOOLÓGICO ARCA DE NOÉ", font=("Century Gothic", 20), bg="black", fg="white")
    title_label.place(x=280, y=55)

    back_image = PhotoImage(file="tkinter_gui/images/back_20.png")

    back_label = Button(window_excluir, image=back_image, bg="darkorange", command=voltar)
    back_label.place(x=40, y=180)

    menu_label = Label(window_excluir, text="O QUE VOCÊ DESEJA EXCLUIR?", font=("Century Gothic", 20, "bold"), width=30 , bg="darkorange", fg="black")
    menu_label.pack(pady=(30,0)) # utilizei somente o pack() para centralizar / padding Y, primeiro valor top, segundo valor bottom

    cad_button = Button(window_excluir, text="ANIMAL", font=("Century Gothic", 15, "bold"), width=20 , bg="black", fg="darkorange", relief="raised", command="")
    cad_button.pack(pady=5)
    alt_button = Button(window_excluir, text="FUNCIONÁRIO", font=("Century Gothic", 15, "bold"), width=20 , bg="black", fg="darkorange", relief="raised", command="")
    alt_button.pack(pady=5)
    ex_button = Button(window_excluir, text="HABITAT", font=("Century Gothic", 15, "bold"), width=20 , bg="black", fg="darkorange", relief="raised", command="")
    ex_button.pack(pady=5)
    pes_button = Button(window_excluir, text="INGRESSO", font=("Century Gothic", 15, "bold"), width=20 , bg="black", fg="darkorange", relief="raised", command="")
    pes_button.pack(pady=5)
    pes_button = Button(window_excluir, text="LOJA", font=("Century Gothic", 15, "bold"), width=20 , bg="black", fg="darkorange", relief="raised", command="")
    pes_button.pack(pady=5)
    pes_button = Button(window_excluir, text="VISITANTE", font=("Century Gothic", 15, "bold"), width=20 , bg="black", fg="darkorange", relief="raised", command="")
    pes_button.pack(pady=5)

    bottom_frame = Frame(window_excluir, width=900, height=70, bg="black", relief="raised")
    bottom_frame.pack(side=BOTTOM)

    window_excluir.mainloop()

def abrir_pesquisar ():
    def voltar():
        window_pesquisar.destroy()
        main_window()

    window.destroy()

    window_pesquisar = Tk()

    window_pesquisar.title("The Gurizes Development LTDA - Painel de Pesquisa")
    window_pesquisar.geometry("900x600")
    window_pesquisar.resizable(width=False,height=False)
    window_pesquisar.configure(background="darkorange")

    arca_logo = PhotoImage(file="tkinter_gui/images/arca_white.png")
    top_frame = Frame(window_pesquisar, width=900, height=150, bg="black", relief="raised")
    top_frame.pack(side=TOP)

    logo_label = Label(top_frame, image=arca_logo, bg="black")
    logo_label.place(x=40, y=20)

    title_label = Label(top_frame, text="ZOOLÓGICO ARCA DE NOÉ", font=("Century Gothic", 20), bg="black", fg="white")
    title_label.place(x=280, y=55)

    back_image = PhotoImage(file="tkinter_gui/images/back_20.png")

    back_label = Button(window_pesquisar, image=back_image, bg="darkorange", command=voltar)
    back_label.place(x=40, y=180)

    menu_label = Label(window_pesquisar, text="O QUE VOCÊ DESEJA PESQUISAR?", font=("Century Gothic", 20, "bold"), width=30 , bg="darkorange", fg="black")
    menu_label.pack(pady=(30,0)) # utilizei somente o pack() para centralizar / padding Y, primeiro valor top, segundo valor bottom

    cad_button = Button(window_pesquisar, text="ANIMAL", font=("Century Gothic", 15, "bold"), width=20 , bg="black", fg="darkorange", relief="raised", command="")
    cad_button.pack(pady=5)
    alt_button = Button(window_pesquisar, text="FUNCIONÁRIO", font=("Century Gothic", 15, "bold"), width=20 , bg="black", fg="darkorange", relief="raised", command="")
    alt_button.pack(pady=5)
    ex_button = Button(window_pesquisar, text="HABITAT", font=("Century Gothic", 15, "bold"), width=20 , bg="black", fg="darkorange", relief="raised", command="")
    ex_button.pack(pady=5)
    pes_button = Button(window_pesquisar, text="INGRESSO", font=("Century Gothic", 15, "bold"), width=20 , bg="black", fg="darkorange", relief="raised", command="")
    pes_button.pack(pady=5)
    pes_button = Button(window_pesquisar, text="LOJA", font=("Century Gothic", 15, "bold"), width=20 , bg="black", fg="darkorange", relief="raised", command="")
    pes_button.pack(pady=5)
    pes_button = Button(window_pesquisar, text="VISITANTE", font=("Century Gothic", 15, "bold"), width=20 , bg="black", fg="darkorange", relief="raised", command="")
    pes_button.pack(pady=5)

    bottom_frame = Frame(window_pesquisar, width=900, height=70, bg="black", relief="raised")
    bottom_frame.pack(side=BOTTOM)

    window_pesquisar.mainloop()

main_window()