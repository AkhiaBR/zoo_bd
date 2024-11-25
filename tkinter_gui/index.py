# IMPORT DAS BIBLIOTECAS
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
import mysql.connector # importa a função de import do conector mysql

conexao_banco = mysql.connector.connect( # especifica a conexão com o database determinado
    host = "127.0.0.1",
    user = "root",
    password = "ZOO_89",
    database = "zoologico"
)
cursor = conexao_banco.cursor()

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

    global window_cadastro
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

    animal_button = Button(window_cadastro, text="ANIMAL", font=("Century Gothic", 15, "bold"), width=20 , bg="black", fg="darkorange", relief="raised", command=CAD_ANIMAL)
    animal_button.pack(pady=5)
    func_button = Button(window_cadastro, text="FUNCIONÁRIO", font=("Century Gothic", 15, "bold"), width=20 , bg="black", fg="darkorange", relief="raised", command=CAD_FUNCIONARIO) # CAD_FUNCIONARIO
    func_button.pack(pady=5)
    hab_button = Button(window_cadastro, text="HABITAT", font=("Century Gothic", 15, "bold"), width=20 , bg="black", fg="darkorange", relief="raised", command=CAD_HABITAT) # CAD_HABITAT
    hab_button.pack(pady=5)
    ing_button = Button(window_cadastro, text="INGRESSO", font=("Century Gothic", 15, "bold"), width=20 , bg="black", fg="darkorange", relief="raised", command=CAD_INGRESSO) # CAD_INGRESSO
    ing_button.pack(pady=5)
    loja_button = Button(window_cadastro, text="LOJA", font=("Century Gothic", 15, "bold"), width=20 , bg="black", fg="darkorange", relief="raised", command=CAD_LOJA) # CAD_LOJA
    loja_button.pack(pady=5)
    vis_button = Button(window_cadastro, text="VISITANTE", font=("Century Gothic", 15, "bold"), width=20 , bg="black", fg="darkorange", relief="raised", command=CAD_VISITANTE) # CAD_VISITANTE
    vis_button.pack(pady=5)

    bottom_frame = Frame(window_cadastro, width=900, height=70, bg="black", relief="raised")
    bottom_frame.pack(side=BOTTOM)

    window_cadastro.mainloop()

def abrir_alterar ():
    def voltar():
        window_alteracao.destroy()
        main_window()

    window.destroy()

    global window_alteracao
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

    animal_button = Button(window_alteracao, text="ANIMAL", font=("Century Gothic", 15, "bold"), width=20 , bg="black", fg="darkorange", relief="raised", command=ALT_ANIMAL) # ALT_ANIMAL
    animal_button.pack(pady=5)
    func_button = Button(window_alteracao, text="FUNCIONÁRIO", font=("Century Gothic", 15, "bold"), width=20 , bg="black", fg="darkorange", relief="raised", command=ALT_FUNCIONARIO) # ALT_FUNCIONARIO
    func_button.pack(pady=5)
    hab_button = Button(window_alteracao, text="HABITAT", font=("Century Gothic", 15, "bold"), width=20 , bg="black", fg="darkorange", relief="raised", command=ALT_HABITAT) # ALT_HABITAT
    hab_button.pack(pady=5)
    ing_button = Button(window_alteracao, text="INGRESSO", font=("Century Gothic", 15, "bold"), width=20 , bg="black", fg="darkorange", relief="raised", command=ALT_INGRESSO) # ALT_INGRESSO
    ing_button.pack(pady=5)
    loja_button = Button(window_alteracao, text="LOJA", font=("Century Gothic", 15, "bold"), width=20 , bg="black", fg="darkorange", relief="raised", command=ALT_LOJA) # ALT_LOJA
    loja_button.pack(pady=5)
    vis_button = Button(window_alteracao, text="VISITANTE", font=("Century Gothic", 15, "bold"), width=20 , bg="black", fg="darkorange", relief="raised", command=ALT_VISITANTE) # ALT_VISITANTE
    vis_button.pack(pady=5)

    bottom_frame = Frame(window_alteracao, width=900, height=70, bg="black", relief="raised")
    bottom_frame.pack(side=BOTTOM)

    window_alteracao.mainloop()

def abrir_excluir ():
    def voltar():
        window_excluir.destroy()
        main_window()

    window.destroy()

    global window_excluir
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

    animal_button = Button(window_excluir, text="ANIMAL", font=("Century Gothic", 15, "bold"), width=20 , bg="black", fg="darkorange", relief="raised", command=DEL_ANIMAL)
    animal_button.pack(pady=5)
    func_button = Button(window_excluir, text="FUNCIONÁRIO", font=("Century Gothic", 15, "bold"), width=20 , bg="black", fg="darkorange", relief="raised", command=DEL_FUNCIONARIO)
    func_button.pack(pady=5)
    hab_button = Button(window_excluir, text="HABITAT", font=("Century Gothic", 15, "bold"), width=20 , bg="black", fg="darkorange", relief="raised", command=DEL_HABITAT)
    hab_button.pack(pady=5)
    ing_button = Button(window_excluir, text="INGRESSO", font=("Century Gothic", 15, "bold"), width=20 , bg="black", fg="darkorange", relief="raised", command=DEL_INGRESSO)
    ing_button.pack(pady=5)
    loja_button = Button(window_excluir, text="LOJA", font=("Century Gothic", 15, "bold"), width=20 , bg="black", fg="darkorange", relief="raised", command=DEL_LOJA) 
    loja_button.pack(pady=5)
    vis_button = Button(window_excluir, text="VISITANTE", font=("Century Gothic", 15, "bold"), width=20 , bg="black", fg="darkorange", relief="raised", command=DEL_VISITANTE) 
    vis_button.pack(pady=5)

    bottom_frame = Frame(window_excluir, width=900, height=70, bg="black", relief="raised")
    bottom_frame.pack(side=BOTTOM)

    window_excluir.mainloop()

def abrir_pesquisar ():
    def voltar():
        window_pesquisar.destroy()
        main_window()

    window.destroy()

    global window_pesquisar
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

    animal_button = Button(window_pesquisar, text="ANIMAL", font=("Century Gothic", 15, "bold"), width=20 , bg="black", fg="darkorange", relief="raised", command=PES_ANIMAL)
    animal_button.pack(pady=5)
    func_button = Button(window_pesquisar, text="FUNCIONÁRIO", font=("Century Gothic", 15, "bold"), width=20 , bg="black", fg="darkorange", relief="raised", command=PES_FUNCIONARIO) # CAD_FUNCIONARIO
    func_button.pack(pady=5)
    hab_button = Button(window_pesquisar, text="HABITAT", font=("Century Gothic", 15, "bold"), width=20 , bg="black", fg="darkorange", relief="raised", command=PES_HABITAT) # CAD_HABITAT
    hab_button.pack(pady=5)
    ing_button = Button(window_pesquisar, text="INGRESSO", font=("Century Gothic", 15, "bold"), width=20 , bg="black", fg="darkorange", relief="raised", command=PES_INGRESSOS) # CAD_INGRESSO
    ing_button.pack(pady=5)
    loja_button = Button(window_pesquisar, text="LOJA", font=("Century Gothic", 15, "bold"), width=20 , bg="black", fg="darkorange", relief="raised", command=PES_LOJA) # CAD_LOJA
    loja_button.pack(pady=5)
    vis_button = Button(window_pesquisar, text="VISITANTE", font=("Century Gothic", 15, "bold"), width=20 , bg="black", fg="darkorange", relief="raised", command=PES_VISITANTE) # CAD_VISITANTE
    vis_button.pack(pady=5)

    bottom_frame = Frame(window_pesquisar, width=900, height=70, bg="black", relief="raised")
    bottom_frame.pack(side=BOTTOM)

    window_pesquisar.mainloop()

# JANELAS SQL INSERTION - CADASTRO
def CAD_ANIMAL():
    def voltar():
        window_animal_criar.destroy()
        main_window() # se tentar voltar para abrir_cadastro(), vai dar erro pois a def abrir_cadastro() vai tentar deletar a main_window, que já está apagada pois você já a apagou abrindo a def CAD_ANIMAL

    def sql_animal_cad(): # sempre em cima
        nome = nome_entry.get()
        especie = especie_entry.get()
        genero = genero_entry.get()
        datanasc = datanasc_entry.get()
        origem = origem_entry.get()
        saude = saude_entry.get()
        alimentacao = alimentacao_entry.get()
        id_habitat = id_habitat_entry.get()

        comando_sql = f'''INSERT INTO animais (Nome, Especie, Genero, Datanasc, Origem, Saúde, Alimentacao, Idhabitat) 
                    VALUES ("{nome}", "{especie}", "{genero}", "{datanasc}", "{origem}", "{saude}", "{alimentacao}", "{id_habitat}")'''


        cursor.execute(comando_sql)
        conexao_banco.commit()

        voltar()

    window_cadastro.destroy()

    global window_animal_criar
    window_animal_criar = Tk()

    window_animal_criar.title("The Gurizes Development LTDA - Painel de Cadastro: ANIMAL")
    window_animal_criar.geometry("900x600")
    window_animal_criar.resizable(width=False,height=False)
    window_animal_criar.configure(background="darkorange")

    arca_logo = PhotoImage(file="tkinter_gui/images/arca_white.png")
    top_frame = Frame(window_animal_criar, width=900, height=150, bg="black", relief="raised")
    top_frame.pack(side=TOP)

    logo_label = Label(top_frame, image=arca_logo, bg="black")
    logo_label.place(x=40, y=20)

    title_label = Label(top_frame, text="ZOOLÓGICO ARCA DE NOÉ", font=("Century Gothic", 20), bg="black", fg="white")
    title_label.place(x=280, y=55)

    back_image = PhotoImage(file="tkinter_gui/images/back_20.png")

    back_label = Button(window_animal_criar, image=back_image, bg="darkorange", command=voltar)
    back_label.place(x=40, y=180)

    nome_label = Label(window_animal_criar, text="Nome: ", font=("Century Gothic", 8, "bold"), bg="darkorange", fg="black")
    nome_label.pack(pady=(8,0))  # utilizar somente o pack(y1,y2) para centralizar / padding Y, primeiro valor top, segundo valor bottom
    nome_entry = Entry(window_animal_criar, width=30)
    nome_entry.pack()
    especie_label = Label(window_animal_criar, text="Espécie: ", font=("Century Gothic", 8, "bold"), bg="darkorange", fg="black")
    especie_label.pack()
    especie_entry = Entry(window_animal_criar, width=30)
    especie_entry.pack()
    genero_label = Label(window_animal_criar, text="Gênero: ", font=("Century Gothic", 8, "bold"), bg="darkorange", fg="black")
    genero_label.pack()
    genero_entry = Entry(window_animal_criar, width=30)
    genero_entry.pack()
    datanasc_label = Label(window_animal_criar, text="Data de Nascimento: ", font=("Century Gothic", 8, "bold"), bg="darkorange", fg="black")
    datanasc_label.pack()
    datanasc_entry = Entry(window_animal_criar, width=30)
    datanasc_entry.pack()
    origem_label = Label(window_animal_criar, text="País de Origem: ", font=("Century Gothic", 8, "bold"), bg="darkorange", fg="black")
    origem_label.pack()
    origem_entry = Entry(window_animal_criar, width=30)
    origem_entry.pack()
    saude_label = Label(window_animal_criar, text="Saúde: ", font=("Century Gothic", 8, "bold"), bg="darkorange", fg="black")
    saude_label.pack()
    saude_entry = Entry(window_animal_criar, width=30)
    saude_entry.pack()
    alimentacao_label = Label(window_animal_criar, text="Alimentação: ", font=("Century Gothic", 8, "bold"), bg="darkorange", fg="black")
    alimentacao_label.pack()
    alimentacao_entry = Entry(window_animal_criar, width=30)
    alimentacao_entry.pack()
    id_habitat_label = Label(window_animal_criar, text="ID do Habitat: ", font=("Century Gothic", 8, "bold"), bg="darkorange", fg="black")
    id_habitat_label.pack()
    id_habitat_entry = Entry(window_animal_criar, width=30)
    id_habitat_entry.pack()

    bottom_frame = Frame(window_animal_criar, width=900, height=70, bg="black", relief="raised")
    bottom_frame.pack(side=BOTTOM)

    submit_botao = Button(window_animal_criar, text="CADASTRAR", font=("Century Gothic", 10, "bold"), width=15 , bg="black", fg="darkorange", relief="raised", command=sql_animal_cad)
    submit_botao.pack(pady=10)

    window_animal_criar.mainloop()

def CAD_FUNCIONARIO():
    def voltar():
        window_animal_criar.destroy()
        main_window() # se tentar voltar para abrir_cadastro(), vai dar erro pois a def abrir_cadastro() vai tentar deletar a main_window, que já está apagada pois você já a apagou abrindo a def CAD_ANIMAL

    def sql_animal_cad(): # sempre em cima
        nome = nome_entry.get()
        cargo = cargo_entry.get()
        datacontratacao = datacontratacao_entry.get()
        email = email_entry.get()
        telefone = telefone_entry.get()

        comando_sql = f'''INSERT INTO funcionarios (Nome, Cargo, Datacontratacao, Email, Telefone) 
                    VALUES ("{nome}", "{cargo}", "{datacontratacao}", "{email}", "{telefone}")'''


        cursor.execute(comando_sql)
        conexao_banco.commit()

        voltar()

    window_cadastro.destroy()

    global window_animal_criar
    window_animal_criar = Tk()

    window_animal_criar.title("The Gurizes Development LTDA - Painel de Cadastro: FUNCIONÁRIO")
    window_animal_criar.geometry("900x600")
    window_animal_criar.resizable(width=False,height=False)
    window_animal_criar.configure(background="darkorange")

    arca_logo = PhotoImage(file="tkinter_gui/images/arca_white.png")
    top_frame = Frame(window_animal_criar, width=900, height=150, bg="black", relief="raised")
    top_frame.pack(side=TOP)

    logo_label = Label(top_frame, image=arca_logo, bg="black")
    logo_label.place(x=40, y=20)

    title_label = Label(top_frame, text="ZOOLÓGICO ARCA DE NOÉ", font=("Century Gothic", 20), bg="black", fg="white")
    title_label.place(x=280, y=55)

    back_image = PhotoImage(file="tkinter_gui/images/back_20.png")

    back_label = Button(window_animal_criar, image=back_image, bg="darkorange", command=voltar)
    back_label.place(x=40, y=180)

    nome_label = Label(window_animal_criar, text="Nome: ", font=("Century Gothic", 8, "bold"), bg="darkorange", fg="black")
    nome_label.pack(pady=(8,0))  # utilizar somente o pack(y1,y2) para centralizar / padding Y, primeiro valor top, segundo valor bottom
    nome_entry = Entry(window_animal_criar, width=30)
    nome_entry.pack()
    cargo_label = Label(window_animal_criar, text="Cargo: ", font=("Century Gothic", 8, "bold"), bg="darkorange", fg="black")
    cargo_label.pack()
    cargo_entry = Entry(window_animal_criar, width=30)
    cargo_entry.pack()
    datacontratacao_label = Label(window_animal_criar, text="Data de Contratação: ", font=("Century Gothic", 8, "bold"), bg="darkorange", fg="black")
    datacontratacao_label.pack()
    datacontratacao_entry = Entry(window_animal_criar, width=30)
    datacontratacao_entry.pack()
    email_label = Label(window_animal_criar, text="E-mail: ", font=("Century Gothic", 8, "bold"), bg="darkorange", fg="black")
    email_label.pack()
    email_entry = Entry(window_animal_criar, width=30)
    email_entry.pack()
    telefone_label = Label(window_animal_criar, text="Telefone: ", font=("Century Gothic", 8, "bold"), bg="darkorange", fg="black")
    telefone_label.pack()
    telefone_entry = Entry(window_animal_criar, width=30)
    telefone_entry.pack()

    bottom_frame = Frame(window_animal_criar, width=900, height=70, bg="black", relief="raised")
    bottom_frame.pack(side=BOTTOM)

    submit_botao = Button(window_animal_criar, text="CADASTRAR", font=("Century Gothic", 10, "bold"), width=15 , bg="black", fg="darkorange", relief="raised", command=sql_animal_cad)
    submit_botao.pack(pady=10)

    window_animal_criar.mainloop()

def CAD_HABITAT():
    def voltar():
        window_animal_criar.destroy()
        main_window() # se tentar voltar para abrir_cadastro(), vai dar erro pois a def abrir_cadastro() vai tentar deletar a main_window, que já está apagada pois você já a apagou abrindo a def CAD_ANIMAL

    def sql_animal_cad(): # sempre em cima
        tipo = tipo_entry.get()
        tamanho = tamanho_entry.get()
        clima = clima_entry.get()

        comando_sql = f'''INSERT INTO habitat (Tipo, Tamanho, Clima) 
                    VALUES ("{tipo}", "{tamanho}", "{clima}")'''


        cursor.execute(comando_sql)
        conexao_banco.commit()

        voltar()

    window_cadastro.destroy()

    global window_animal_criar
    window_animal_criar = Tk()

    window_animal_criar.title("The Gurizes Development LTDA - Painel de Cadastro: HABITAT")
    window_animal_criar.geometry("900x600")
    window_animal_criar.resizable(width=False,height=False)
    window_animal_criar.configure(background="darkorange")

    arca_logo = PhotoImage(file="tkinter_gui/images/arca_white.png")
    top_frame = Frame(window_animal_criar, width=900, height=150, bg="black", relief="raised")
    top_frame.pack(side=TOP)

    logo_label = Label(top_frame, image=arca_logo, bg="black")
    logo_label.place(x=40, y=20)

    title_label = Label(top_frame, text="ZOOLÓGICO ARCA DE NOÉ", font=("Century Gothic", 20), bg="black", fg="white")
    title_label.place(x=280, y=55)

    back_image = PhotoImage(file="tkinter_gui/images/back_20.png")

    back_label = Button(window_animal_criar, image=back_image, bg="darkorange", command=voltar)
    back_label.place(x=40, y=180)

    tipo_label = Label(window_animal_criar, text="Tipo: ", font=("Century Gothic", 8, "bold"), bg="darkorange", fg="black")
    tipo_label.pack(pady=(8,0))  # utilizar somente o pack(y1,y2) para centralizar / padding Y, primeiro valor top, segundo valor bottom
    tipo_entry = Entry(window_animal_criar, width=30)
    tipo_entry.pack()
    tamanho_label = Label(window_animal_criar, text="Tamanho (m²): ", font=("Century Gothic", 8, "bold"), bg="darkorange", fg="black")
    tamanho_label.pack()
    tamanho_entry = Entry(window_animal_criar, width=30)
    tamanho_entry.pack()
    clima_label = Label(window_animal_criar, text="Clima: ", font=("Century Gothic", 8, "bold"), bg="darkorange", fg="black")
    clima_label.pack()
    clima_entry = Entry(window_animal_criar, width=30)
    clima_entry.pack()

    bottom_frame = Frame(window_animal_criar, width=900, height=70, bg="black", relief="raised")
    bottom_frame.pack(side=BOTTOM)

    submit_botao = Button(window_animal_criar, text="CADASTRAR", font=("Century Gothic", 10, "bold"), width=15 , bg="black", fg="darkorange", relief="raised", command=sql_animal_cad)
    submit_botao.pack(pady=10)

    window_animal_criar.mainloop()

def CAD_INGRESSO():
    def voltar():
        window_animal_criar.destroy()
        main_window() # se tentar voltar para abrir_cadastro(), vai dar erro pois a def abrir_cadastro() vai tentar deletar a main_window, que já está apagada pois você já a apagou abrindo a def CAD_ANIMAL

    def sql_animal_cad(): # sempre em cima
        tipo = tipo_entry.get()
        preco = preco_entry.get()
        datavalidade = datavalidade_entry.get()
        quantidade = quantidade_entry.get()
        desconto = desconto_entry.get()

        comando_sql = f'''INSERT INTO ingressos (Tipo, Preco, Datavalidade, Quantidade, Desconto) 
                    VALUES ("{tipo}","{preco}", "{datavalidade}", "{quantidade}", "{desconto}")'''


        cursor.execute(comando_sql)
        conexao_banco.commit()

        voltar()

    window_cadastro.destroy()

    global window_animal_criar
    window_animal_criar = Tk()

    window_animal_criar.title("The Gurizes Development LTDA - Painel de Cadastro: INGRESSO")
    window_animal_criar.geometry("900x600")
    window_animal_criar.resizable(width=False,height=False)
    window_animal_criar.configure(background="darkorange")

    arca_logo = PhotoImage(file="tkinter_gui/images/arca_white.png")
    top_frame = Frame(window_animal_criar, width=900, height=150, bg="black", relief="raised")
    top_frame.pack(side=TOP)

    logo_label = Label(top_frame, image=arca_logo, bg="black")
    logo_label.place(x=40, y=20)

    title_label = Label(top_frame, text="ZOOLÓGICO ARCA DE NOÉ", font=("Century Gothic", 20), bg="black", fg="white")
    title_label.place(x=280, y=55)

    back_image = PhotoImage(file="tkinter_gui/images/back_20.png")

    back_label = Button(window_animal_criar, image=back_image, bg="darkorange", command=voltar)
    back_label.place(x=40, y=180)

    tipo_label = Label(window_animal_criar, text="Tipo: ", font=("Century Gothic", 8, "bold"), bg="darkorange", fg="black")
    tipo_label.pack(pady=(8,0))  # utilizar somente o pack(y1,y2) para centralizar / padding Y, primeiro valor top, segundo valor bottom
    tipo_entry = Entry(window_animal_criar, width=30)
    tipo_entry.pack()
    preco_label = Label(window_animal_criar, text="Preço: ", font=("Century Gothic", 8, "bold"), bg="darkorange", fg="black")
    preco_label.pack()  # utilizar somente o pack(y1,y2) para centralizar / padding Y, primeiro valor top, segundo valor bottom
    preco_entry = Entry(window_animal_criar, width=30)
    preco_entry.pack()
    datavalidade_label = Label(window_animal_criar, text="Data de Validade: ", font=("Century Gothic", 8, "bold"), bg="darkorange", fg="black")
    datavalidade_label.pack()
    datavalidade_entry = Entry(window_animal_criar, width=30)
    datavalidade_entry.pack()
    quantidade_label = Label(window_animal_criar, text="Quantidade: ", font=("Century Gothic", 8, "bold"), bg="darkorange", fg="black")
    quantidade_label.pack()
    quantidade_entry = Entry(window_animal_criar, width=30)
    quantidade_entry.pack()
    desconto_label = Label(window_animal_criar, text="Desconto(%): ", font=("Century Gothic", 8, "bold"), bg="darkorange", fg="black")
    desconto_label.pack()
    desconto_entry = Entry(window_animal_criar, width=30)
    desconto_entry.pack()

    bottom_frame = Frame(window_animal_criar, width=900, height=70, bg="black", relief="raised")
    bottom_frame.pack(side=BOTTOM)

    submit_botao = Button(window_animal_criar, text="CADASTRAR", font=("Century Gothic", 10, "bold"), width=15 , bg="black", fg="darkorange", relief="raised", command=sql_animal_cad)
    submit_botao.pack(pady=10)

    window_animal_criar.mainloop()

def CAD_LOJA():
    def voltar():
        window_animal_criar.destroy()
        main_window() # se tentar voltar para abrir_cadastro(), vai dar erro pois a def abrir_cadastro() vai tentar deletar a main_window, que já está apagada pois você já a apagou abrindo a def CAD_ANIMAL

    def sql_animal_cad(): # sempre em cima
        nome = nome_entry.get()
        servico = servico_entry.get()
        horario = horario_entry.get()
        receita = receita_entry.get()
        email = email_entry.get()
        telefone = telefone_entry.get()

        comando_sql = f'''INSERT INTO lojas (Nome, Servico, Horario, Receita, Email, Telefone) 
                    VALUES ("{nome}","{servico}", "{horario}", "{receita}", "{email}","{telefone}")'''


        cursor.execute(comando_sql)
        conexao_banco.commit()

        voltar()

    window_cadastro.destroy()

    global window_animal_criar
    window_animal_criar = Tk()

    window_animal_criar.title("The Gurizes Development LTDA - Painel de Cadastro: INGRESSO")
    window_animal_criar.geometry("900x600")
    window_animal_criar.resizable(width=False,height=False)
    window_animal_criar.configure(background="darkorange")

    arca_logo = PhotoImage(file="tkinter_gui/images/arca_white.png")
    top_frame = Frame(window_animal_criar, width=900, height=150, bg="black", relief="raised")
    top_frame.pack(side=TOP)

    logo_label = Label(top_frame, image=arca_logo, bg="black")
    logo_label.place(x=40, y=20)

    title_label = Label(top_frame, text="ZOOLÓGICO ARCA DE NOÉ", font=("Century Gothic", 20), bg="black", fg="white")
    title_label.place(x=280, y=55)

    back_image = PhotoImage(file="tkinter_gui/images/back_20.png")

    back_label = Button(window_animal_criar, image=back_image, bg="darkorange", command=voltar)
    back_label.place(x=40, y=180)

    nome_label = Label(window_animal_criar, text="Nome: ", font=("Century Gothic", 8, "bold"), bg="darkorange", fg="black")
    nome_label.pack(pady=(8,0))  # utilizar somente o pack(y1,y2) para centralizar / padding Y, primeiro valor top, segundo valor bottom
    nome_entry = Entry(window_animal_criar, width=30)
    nome_entry.pack()
    servico_label = Label(window_animal_criar, text="Serviço: ", font=("Century Gothic", 8, "bold"), bg="darkorange", fg="black")
    servico_label.pack()  # utilizar somente o pack(y1,y2) para centralizar / padding Y, primeiro valor top, segundo valor bottom
    servico_entry = Entry(window_animal_criar, width=30)
    servico_entry.pack()
    horario_label = Label(window_animal_criar, text="Horas Operadas: ", font=("Century Gothic", 8, "bold"), bg="darkorange", fg="black")
    horario_label.pack()
    horario_entry = Entry(window_animal_criar, width=30)
    horario_entry.pack()
    receita_label = Label(window_animal_criar, text="Receita (Mensal): ", font=("Century Gothic", 8, "bold"), bg="darkorange", fg="black")
    receita_label.pack()
    receita_entry = Entry(window_animal_criar, width=30)
    receita_entry.pack()
    email_label = Label(window_animal_criar, text="E-mail: ", font=("Century Gothic", 8, "bold"), bg="darkorange", fg="black")
    email_label.pack()
    email_entry = Entry(window_animal_criar, width=30)
    email_entry.pack()
    telefone_label = Label(window_animal_criar, text="Telefone: ", font=("Century Gothic", 8, "bold"), bg="darkorange", fg="black")
    telefone_label.pack()
    telefone_entry = Entry(window_animal_criar, width=30)
    telefone_entry.pack()

    bottom_frame = Frame(window_animal_criar, width=900, height=70, bg="black", relief="raised")
    bottom_frame.pack(side=BOTTOM)

    submit_botao = Button(window_animal_criar, text="CADASTRAR", font=("Century Gothic", 10, "bold"), width=15 , bg="black", fg="darkorange", relief="raised", command=sql_animal_cad)
    submit_botao.pack(pady=10)

    window_animal_criar.mainloop()

def CAD_LOJA():
    def voltar():
        window_animal_criar.destroy()
        main_window() # se tentar voltar para abrir_cadastro(), vai dar erro pois a def abrir_cadastro() vai tentar deletar a main_window, que já está apagada pois você já a apagou abrindo a def CAD_ANIMAL

    def sql_animal_cad(): # sempre em cima
        nome = nome_entry.get()
        servico = servico_entry.get()
        horario = horario_entry.get()
        receita = receita_entry.get()
        email = email_entry.get()
        telefone = telefone_entry.get()

        comando_sql = f'''INSERT INTO lojas (Nome, Servico, Horario, Receita, Email, Telefone) 
                    VALUES ("{nome}","{servico}", "{horario}", "{receita}", "{email}","{telefone}")'''


        cursor.execute(comando_sql)
        conexao_banco.commit()

        voltar()

    window_cadastro.destroy()

    global window_animal_criar
    window_animal_criar = Tk()

    window_animal_criar.title("The Gurizes Development LTDA - Painel de Cadastro: INGRESSO")
    window_animal_criar.geometry("900x600")
    window_animal_criar.resizable(width=False,height=False)
    window_animal_criar.configure(background="darkorange")

    arca_logo = PhotoImage(file="tkinter_gui/images/arca_white.png")
    top_frame = Frame(window_animal_criar, width=900, height=150, bg="black", relief="raised")
    top_frame.pack(side=TOP)

    logo_label = Label(top_frame, image=arca_logo, bg="black")
    logo_label.place(x=40, y=20)

    title_label = Label(top_frame, text="ZOOLÓGICO ARCA DE NOÉ", font=("Century Gothic", 20), bg="black", fg="white")
    title_label.place(x=280, y=55)

    back_image = PhotoImage(file="tkinter_gui/images/back_20.png")

    back_label = Button(window_animal_criar, image=back_image, bg="darkorange", command=voltar)
    back_label.place(x=40, y=180)

    nome_label = Label(window_animal_criar, text="Nome: ", font=("Century Gothic", 8, "bold"), bg="darkorange", fg="black")
    nome_label.pack(pady=(8,0))  # utilizar somente o pack(y1,y2) para centralizar / padding Y, primeiro valor top, segundo valor bottom
    nome_entry = Entry(window_animal_criar, width=30)
    nome_entry.pack()
    servico_label = Label(window_animal_criar, text="Serviço: ", font=("Century Gothic", 8, "bold"), bg="darkorange", fg="black")
    servico_label.pack(pady=(8,0))  # utilizar somente o pack(y1,y2) para centralizar / padding Y, primeiro valor top, segundo valor bottom
    servico_entry = Entry(window_animal_criar, width=30)
    servico_entry.pack()
    horario_label = Label(window_animal_criar, text="Horas Operadas: ", font=("Century Gothic", 8, "bold"), bg="darkorange", fg="black")
    horario_label.pack()
    horario_entry = Entry(window_animal_criar, width=30)
    horario_entry.pack()
    receita_label = Label(window_animal_criar, text="Receita (Mensal): ", font=("Century Gothic", 8, "bold"), bg="darkorange", fg="black")
    receita_label.pack()
    receita_entry = Entry(window_animal_criar, width=30)
    receita_entry.pack()
    email_label = Label(window_animal_criar, text="E-mail: ", font=("Century Gothic", 8, "bold"), bg="darkorange", fg="black")
    email_label.pack()
    email_entry = Entry(window_animal_criar, width=30)
    email_entry.pack()
    telefone_label = Label(window_animal_criar, text="Telefone: ", font=("Century Gothic", 8, "bold"), bg="darkorange", fg="black")
    telefone_label.pack()
    telefone_entry = Entry(window_animal_criar, width=30)
    telefone_entry.pack()

    bottom_frame = Frame(window_animal_criar, width=900, height=70, bg="black", relief="raised")
    bottom_frame.pack(side=BOTTOM)

    submit_botao = Button(window_animal_criar, text="CADASTRAR", font=("Century Gothic", 10, "bold"), width=15 , bg="black", fg="darkorange", relief="raised", command=sql_animal_cad)
    submit_botao.pack(pady=10)

    window_animal_criar.mainloop()

def CAD_VISITANTE():
    def voltar():
        window_animal_criar.destroy()
        main_window() # se tentar voltar para abrir_cadastro(), vai dar erro pois a def abrir_cadastro() vai tentar deletar a main_window, que já está apagada pois você já a apagou abrindo a def CAD_ANIMAL

    def sql_animal_cad(): # sempre em cima
        nome = nome_entry.get()
        datavisita = datavisita_entry.get()
        idingresso = idingresso_entry.get()

        comando_sql = f'''INSERT INTO visitantes (Nome, Datavisita, Idingresso) 
                    VALUES ("{nome}","{datavisita}", "{idingresso}")'''


        cursor.execute(comando_sql)
        conexao_banco.commit()

        voltar()

    window_cadastro.destroy()

    global window_animal_criar
    window_animal_criar = Tk()

    window_animal_criar.title("The Gurizes Development LTDA - Painel de Cadastro: INGRESSO")
    window_animal_criar.geometry("900x600")
    window_animal_criar.resizable(width=False,height=False)
    window_animal_criar.configure(background="darkorange")

    arca_logo = PhotoImage(file="tkinter_gui/images/arca_white.png")
    top_frame = Frame(window_animal_criar, width=900, height=150, bg="black", relief="raised")
    top_frame.pack(side=TOP)

    logo_label = Label(top_frame, image=arca_logo, bg="black")
    logo_label.place(x=40, y=20)

    title_label = Label(top_frame, text="ZOOLÓGICO ARCA DE NOÉ", font=("Century Gothic", 20), bg="black", fg="white")
    title_label.place(x=280, y=55)

    back_image = PhotoImage(file="tkinter_gui/images/back_20.png")

    back_label = Button(window_animal_criar, image=back_image, bg="darkorange", command=voltar)
    back_label.place(x=40, y=180)

    nome_label = Label(window_animal_criar, text="Nome: ", font=("Century Gothic", 8, "bold"), bg="darkorange", fg="black")
    nome_label.pack(pady=(8,0))  # utilizar somente o pack(y1,y2) para centralizar / padding Y, primeiro valor top, segundo valor bottom
    nome_entry = Entry(window_animal_criar, width=30)
    nome_entry.pack()
    datavisita_label = Label(window_animal_criar, text="Data de Visita: ", font=("Century Gothic", 8, "bold"), bg="darkorange", fg="black")
    datavisita_label.pack()  # utilizar somente o pack(y1,y2) para centralizar / padding Y, primeiro valor top, segundo valor bottom
    datavisita_entry = Entry(window_animal_criar, width=30)
    datavisita_entry.pack()
    idingresso_label = Label(window_animal_criar, text="ID do Ingresso: ", font=("Century Gothic", 8, "bold"), bg="darkorange", fg="black")
    idingresso_label.pack()
    idingresso_entry = Entry(window_animal_criar, width=30)
    idingresso_entry.pack()

    bottom_frame = Frame(window_animal_criar, width=900, height=70, bg="black", relief="raised")
    bottom_frame.pack(side=BOTTOM)

    submit_botao = Button(window_animal_criar, text="CADASTRAR", font=("Century Gothic", 10, "bold"), width=15 , bg="black", fg="darkorange", relief="raised", command=sql_animal_cad)
    submit_botao.pack(pady=10)

    window_animal_criar.mainloop()

# JANELAS SQL INSERTION - ALTERAR
def ALT_ANIMAL():
    def voltar():
        window_animal_alterar.destroy()
        main_window() # se tentar voltar para abrir_cadastro(), vai dar erro pois a def abrir_cadastro() vai tentar deletar a main_window, que já está apagada pois você já a apagou abrindo a def CAD_ANIMAL

    def sql_animal_alt(): # sempre em cima
        id_animal = id_animal_entry.get()
        novasaude = saude_entry.get()

        comando_sql = f'''UPDATE animais SET `Saúde` = "{novasaude}" WHERE Id = {id_animal}'''

        cursor.execute(comando_sql)
        conexao_banco.commit()

        voltar()

    window_alteracao.destroy()

    global window_animal_alterar
    window_animal_alterar = Tk()

    window_animal_alterar.title("The Gurizes Development LTDA - Painel de Alteração: ANIMAL")
    window_animal_alterar.geometry("900x600")
    window_animal_alterar.resizable(width=False,height=False)
    window_animal_alterar.configure(background="darkorange")

    arca_logo = PhotoImage(file="tkinter_gui/images/arca_white.png")
    top_frame = Frame(window_animal_alterar, width=900, height=150, bg="black", relief="raised")
    top_frame.pack(side=TOP)

    logo_label = Label(top_frame, image=arca_logo, bg="black")
    logo_label.place(x=40, y=20)

    title_label = Label(top_frame, text="ZOOLÓGICO ARCA DE NOÉ", font=("Century Gothic", 20), bg="black", fg="white")
    title_label.place(x=280, y=55)

    back_image = PhotoImage(file="tkinter_gui/images/back_20.png")

    back_label = Button(window_animal_alterar, image=back_image, bg="darkorange", command=voltar)
    back_label.place(x=40, y=180)

    id_animal_label = Label(window_animal_alterar, text="ID do Animal: ", font=("Century Gothic", 8, "bold"), bg="darkorange", fg="black")
    id_animal_label.pack(pady=(8,0))  # utilizar somente o pack(y1,y2) para centralizar / padding Y, primeiro valor top, segundo valor bottom
    id_animal_entry = Entry(window_animal_alterar, width=30)
    id_animal_entry.pack()
    saude_label = Label(window_animal_alterar, text="Atualização da Saúde: ", font=("Century Gothic", 8, "bold"), bg="darkorange", fg="black")
    saude_label.pack()  # utilizar somente o pack(y1,y2) para centralizar / padding Y, primeiro valor top, segundo valor bottom
    saude_entry = Entry(window_animal_alterar, width=30)
    saude_entry.pack()

    bottom_frame = Frame(window_animal_alterar, width=900, height=70, bg="black", relief="raised")
    bottom_frame.pack(side=BOTTOM)

    submit_botao = Button(window_animal_alterar, text="ALTERAR", font=("Century Gothic", 10, "bold"), width=15 , bg="black", fg="darkorange", relief="raised", command=sql_animal_alt)
    submit_botao.pack(pady=10)

    window_animal_alterar.mainloop()

def ALT_FUNCIONARIO():
    def voltar():
        window_animal_alterar.destroy()
        main_window() # se tentar voltar para abrir_cadastro(), vai dar erro pois a def abrir_cadastro() vai tentar deletar a main_window, que já está apagada pois você já a apagou abrindo a def CAD_ANIMAL

    def sql_animal_alt(): # sempre em cima
        id_funcionario = id_funcionario_entry.get()
        novocargo = cargo_entry.get()

        comando_sql = f'''UPDATE funcionarios SET `Cargo` = "{novocargo}" WHERE Id = {id_funcionario}'''

        cursor.execute(comando_sql)
        conexao_banco.commit()

        voltar()

    window_alteracao.destroy()

    global window_animal_alterar
    window_animal_alterar = Tk()

    window_animal_alterar.title("The Gurizes Development LTDA - Painel de Alteração: FUNCIONÁRIO")
    window_animal_alterar.geometry("900x600")
    window_animal_alterar.resizable(width=False,height=False)
    window_animal_alterar.configure(background="darkorange")

    arca_logo = PhotoImage(file="tkinter_gui/images/arca_white.png")
    top_frame = Frame(window_animal_alterar, width=900, height=150, bg="black", relief="raised")
    top_frame.pack(side=TOP)

    logo_label = Label(top_frame, image=arca_logo, bg="black")
    logo_label.place(x=40, y=20)

    title_label = Label(top_frame, text="ZOOLÓGICO ARCA DE NOÉ", font=("Century Gothic", 20), bg="black", fg="white")
    title_label.place(x=280, y=55)

    back_image = PhotoImage(file="tkinter_gui/images/back_20.png")

    back_label = Button(window_animal_alterar, image=back_image, bg="darkorange", command=voltar)
    back_label.place(x=40, y=180)

    id_funcionario_label = Label(window_animal_alterar, text="ID do Funcionário: ", font=("Century Gothic", 8, "bold"), bg="darkorange", fg="black")
    id_funcionario_label.pack(pady=(8,0))  # utilizar somente o pack(y1,y2) para centralizar / padding Y, primeiro valor top, segundo valor bottom
    id_funcionario_entry = Entry(window_animal_alterar, width=30)
    id_funcionario_entry.pack()
    cargo_label = Label(window_animal_alterar, text="Atualização do Cargo: ", font=("Century Gothic", 8, "bold"), bg="darkorange", fg="black")
    cargo_label.pack()  # utilizar somente o pack(y1,y2) para centralizar / padding Y, primeiro valor top, segundo valor bottom
    cargo_entry = Entry(window_animal_alterar, width=30)
    cargo_entry.pack()

    bottom_frame = Frame(window_animal_alterar, width=900, height=70, bg="black", relief="raised")
    bottom_frame.pack(side=BOTTOM)

    submit_botao = Button(window_animal_alterar, text="ALTERAR", font=("Century Gothic", 10, "bold"), width=15 , bg="black", fg="darkorange", relief="raised", command=sql_animal_alt)
    submit_botao.pack(pady=10)

    window_animal_alterar.mainloop()

def ALT_HABITAT():
    def voltar():
        window_animal_alterar.destroy()
        main_window() # se tentar voltar para abrir_cadastro(), vai dar erro pois a def abrir_cadastro() vai tentar deletar a main_window, que já está apagada pois você já a apagou abrindo a def CAD_ANIMAL

    def sql_animal_alt(): # sempre em cima
        id_habitat = id_habitat_entry.get()
        novoclima = clima_entry.get()

        comando_sql = f'''UPDATE habitat SET `Clima` = "{novoclima}" WHERE Id = {id_habitat}'''

        cursor.execute(comando_sql)
        conexao_banco.commit()

        voltar()

    window_alteracao.destroy()

    global window_animal_alterar
    window_animal_alterar = Tk()

    window_animal_alterar.title("The Gurizes Development LTDA - Painel de Alteração: HABITAT")
    window_animal_alterar.geometry("900x600")
    window_animal_alterar.resizable(width=False,height=False)
    window_animal_alterar.configure(background="darkorange")

    arca_logo = PhotoImage(file="tkinter_gui/images/arca_white.png")
    top_frame = Frame(window_animal_alterar, width=900, height=150, bg="black", relief="raised")
    top_frame.pack(side=TOP)

    logo_label = Label(top_frame, image=arca_logo, bg="black")
    logo_label.place(x=40, y=20)

    title_label = Label(top_frame, text="ZOOLÓGICO ARCA DE NOÉ", font=("Century Gothic", 20), bg="black", fg="white")
    title_label.place(x=280, y=55)

    back_image = PhotoImage(file="tkinter_gui/images/back_20.png")

    back_label = Button(window_animal_alterar, image=back_image, bg="darkorange", command=voltar)
    back_label.place(x=40, y=180)

    id_habitat_label = Label(window_animal_alterar, text="ID do Habitat: ", font=("Century Gothic", 8, "bold"), bg="darkorange", fg="black")
    id_habitat_label.pack(pady=(8,0))  # utilizar somente o pack(y1,y2) para centralizar / padding Y, primeiro valor top, segundo valor bottom
    id_habitat_entry = Entry(window_animal_alterar, width=30)
    id_habitat_entry.pack()
    clima_label = Label(window_animal_alterar, text="Atualização do Clima: ", font=("Century Gothic", 8, "bold"), bg="darkorange", fg="black")
    clima_label.pack()  # utilizar somente o pack(y1,y2) para centralizar / padding Y, primeiro valor top, segundo valor bottom
    clima_entry = Entry(window_animal_alterar, width=30)
    clima_entry.pack()

    bottom_frame = Frame(window_animal_alterar, width=900, height=70, bg="black", relief="raised")
    bottom_frame.pack(side=BOTTOM)

    submit_botao = Button(window_animal_alterar, text="ALTERAR", font=("Century Gothic", 10, "bold"), width=15 , bg="black", fg="darkorange", relief="raised", command=sql_animal_alt)
    submit_botao.pack(pady=10)

    window_animal_alterar.mainloop()

def ALT_INGRESSO():
    def voltar():
        window_animal_alterar.destroy()
        main_window() # se tentar voltar para abrir_cadastro(), vai dar erro pois a def abrir_cadastro() vai tentar deletar a main_window, que já está apagada pois você já a apagou abrindo a def CAD_ANIMAL

    def sql_animal_alt(): # sempre em cima
        id_ingresso = id_ingresso_entry.get()
        novopreco = novopreco_entry.get()

        comando_sql = f'''UPDATE ingressos SET `Preco` = "{novopreco}" WHERE Id = {id_ingresso}'''

        cursor.execute(comando_sql)
        conexao_banco.commit()

        voltar()

    window_alteracao.destroy()

    global window_animal_alterar
    window_animal_alterar = Tk()

    window_animal_alterar.title("The Gurizes Development LTDA - Painel de Alteração: INGRESSO")
    window_animal_alterar.geometry("900x600")
    window_animal_alterar.resizable(width=False,height=False)
    window_animal_alterar.configure(background="darkorange")

    arca_logo = PhotoImage(file="tkinter_gui/images/arca_white.png")
    top_frame = Frame(window_animal_alterar, width=900, height=150, bg="black", relief="raised")
    top_frame.pack(side=TOP)

    logo_label = Label(top_frame, image=arca_logo, bg="black")
    logo_label.place(x=40, y=20)

    title_label = Label(top_frame, text="ZOOLÓGICO ARCA DE NOÉ", font=("Century Gothic", 20), bg="black", fg="white")
    title_label.place(x=280, y=55)

    back_image = PhotoImage(file="tkinter_gui/images/back_20.png")

    back_label = Button(window_animal_alterar, image=back_image, bg="darkorange", command=voltar)
    back_label.place(x=40, y=180)

    id_ingresso_label = Label(window_animal_alterar, text="ID do Ingresso: ", font=("Century Gothic", 8, "bold"), bg="darkorange", fg="black")
    id_ingresso_label.pack(pady=(8,0))  # utilizar somente o pack(y1,y2) para centralizar / padding Y, primeiro valor top, segundo valor bottom
    id_ingresso_entry = Entry(window_animal_alterar, width=30)
    id_ingresso_entry.pack()
    novopreco_label = Label(window_animal_alterar, text="Atualização do Preco: ", font=("Century Gothic", 8, "bold"), bg="darkorange", fg="black")
    novopreco_label.pack()  # utilizar somente o pack(y1,y2) para centralizar / padding Y, primeiro valor top, segundo valor bottom
    novopreco_entry = Entry(window_animal_alterar, width=30)
    novopreco_entry.pack()

    bottom_frame = Frame(window_animal_alterar, width=900, height=70, bg="black", relief="raised")
    bottom_frame.pack(side=BOTTOM)

    submit_botao = Button(window_animal_alterar, text="ALTERAR", font=("Century Gothic", 10, "bold"), width=15 , bg="black", fg="darkorange", relief="raised", command=sql_animal_alt)
    submit_botao.pack(pady=10)

    window_animal_alterar.mainloop()

def ALT_LOJA():
    def voltar():
        window_animal_alterar.destroy()
        main_window() # se tentar voltar para abrir_cadastro(), vai dar erro pois a def abrir_cadastro() vai tentar deletar a main_window, que já está apagada pois você já a apagou abrindo a def CAD_ANIMAL

    def sql_animal_alt(): # sempre em cima
        id_loja = id_loja_entry.get()
        nova_receita = nova_receita_entry.get()

        comando_sql = f'''UPDATE lojas SET `Receita` = "{nova_receita}" WHERE Id = {id_loja}'''

        cursor.execute(comando_sql)
        conexao_banco.commit()

        voltar()

    window_alteracao.destroy()

    global window_animal_alterar
    window_animal_alterar = Tk()

    window_animal_alterar.title("The Gurizes Development LTDA - Painel de Alteração: LOJA")
    window_animal_alterar.geometry("900x600")
    window_animal_alterar.resizable(width=False,height=False)
    window_animal_alterar.configure(background="darkorange")

    arca_logo = PhotoImage(file="tkinter_gui/images/arca_white.png")
    top_frame = Frame(window_animal_alterar, width=900, height=150, bg="black", relief="raised")
    top_frame.pack(side=TOP)

    logo_label = Label(top_frame, image=arca_logo, bg="black")
    logo_label.place(x=40, y=20)

    title_label = Label(top_frame, text="ZOOLÓGICO ARCA DE NOÉ", font=("Century Gothic", 20), bg="black", fg="white")
    title_label.place(x=280, y=55)

    back_image = PhotoImage(file="tkinter_gui/images/back_20.png")

    back_label = Button(window_animal_alterar, image=back_image, bg="darkorange", command=voltar)
    back_label.place(x=40, y=180)

    id_loja_label = Label(window_animal_alterar, text="ID da Loja: ", font=("Century Gothic", 8, "bold"), bg="darkorange", fg="black")
    id_loja_label.pack(pady=(8,0))  # utilizar somente o pack(y1,y2) para centralizar / padding Y, primeiro valor top, segundo valor bottom
    id_loja_entry = Entry(window_animal_alterar, width=30)
    id_loja_entry.pack()
    nova_receita_label = Label(window_animal_alterar, text="Atualização da Receita: ", font=("Century Gothic", 8, "bold"), bg="darkorange", fg="black")
    nova_receita_label.pack()  # utilizar somente o pack(y1,y2) para centralizar / padding Y, primeiro valor top, segundo valor bottom
    nova_receita_entry = Entry(window_animal_alterar, width=30)
    nova_receita_entry.pack()

    bottom_frame = Frame(window_animal_alterar, width=900, height=70, bg="black", relief="raised")
    bottom_frame.pack(side=BOTTOM)

    submit_botao = Button(window_animal_alterar, text="ALTERAR", font=("Century Gothic", 10, "bold"), width=15 , bg="black", fg="darkorange", relief="raised", command=sql_animal_alt)
    submit_botao.pack(pady=10)

    window_animal_alterar.mainloop()

def ALT_VISITANTE():
    def voltar():
        window_animal_alterar.destroy()
        main_window() # se tentar voltar para abrir_cadastro(), vai dar erro pois a def abrir_cadastro() vai tentar deletar a main_window, que já está apagada pois você já a apagou abrindo a def CAD_ANIMAL

    def sql_animal_alt(): # sempre em cima
        id_visitante = id_visitante_entry.get()
        nova_data = nova_data_entry.get()

        comando_sql = f'''UPDATE visitantes SET `Datavisita` = "{nova_data}" WHERE Id = {id_visitante}'''

        cursor.execute(comando_sql)
        conexao_banco.commit()

        voltar()

    window_alteracao.destroy()

    global window_animal_alterar
    window_animal_alterar = Tk()

    window_animal_alterar.title("The Gurizes Development LTDA - Painel de Alteração: VISITANTE")
    window_animal_alterar.geometry("900x600")
    window_animal_alterar.resizable(width=False,height=False)
    window_animal_alterar.configure(background="darkorange")

    arca_logo = PhotoImage(file="tkinter_gui/images/arca_white.png")
    top_frame = Frame(window_animal_alterar, width=900, height=150, bg="black", relief="raised")
    top_frame.pack(side=TOP)

    logo_label = Label(top_frame, image=arca_logo, bg="black")
    logo_label.place(x=40, y=20)

    title_label = Label(top_frame, text="ZOOLÓGICO ARCA DE NOÉ", font=("Century Gothic", 20), bg="black", fg="white")
    title_label.place(x=280, y=55)

    back_image = PhotoImage(file="tkinter_gui/images/back_20.png")

    back_label = Button(window_animal_alterar, image=back_image, bg="darkorange", command=voltar)
    back_label.place(x=40, y=180)

    id_visitante_label = Label(window_animal_alterar, text="ID do Visitante: ", font=("Century Gothic", 8, "bold"), bg="darkorange", fg="black")
    id_visitante_label.pack(pady=(8,0))  # utilizar somente o pack(y1,y2) para centralizar / padding Y, primeiro valor top, segundo valor bottom
    id_visitante_entry = Entry(window_animal_alterar, width=30)
    id_visitante_entry.pack()
    nova_data_label = Label(window_animal_alterar, text="Atualização da Data de Visita: ", font=("Century Gothic", 8, "bold"), bg="darkorange", fg="black")
    nova_data_label.pack()  # utilizar somente o pack(y1,y2) para centralizar / padding Y, primeiro valor top, segundo valor bottom
    nova_data_entry = Entry(window_animal_alterar, width=30)
    nova_data_entry.pack()

    bottom_frame = Frame(window_animal_alterar, width=900, height=70, bg="black", relief="raised")
    bottom_frame.pack(side=BOTTOM)

    submit_botao = Button(window_animal_alterar, text="ALTERAR", font=("Century Gothic", 10, "bold"), width=15 , bg="black", fg="darkorange", relief="raised", command=sql_animal_alt)
    submit_botao.pack(pady=10)

    window_animal_alterar.mainloop()

# JANELAS SQL INSERTION - DELETAR
def DEL_ANIMAL():
    def voltar():
        window_animal_deletar.destroy()
        main_window() # se tentar voltar para abrir_cadastro(), vai dar erro pois a def abrir_cadastro() vai tentar deletar a main_window, que já está apagada pois você já a apagou abrindo a def CAD_ANIMAL

    def sql_animal_del(): # funcao sempre em cima
        id_animal = id_animal_entry.get()

        comando_sql = f'''DELETE FROM animais WHERE Id = {id_animal}'''

        cursor.execute(comando_sql)
        conexao_banco.commit()

        voltar()

    window_excluir.destroy()

    global window_animal_deletar
    window_animal_deletar = Tk()

    window_animal_deletar.title("The Gurizes Development LTDA - Painel de Exclusão: ANIMAL")
    window_animal_deletar.geometry("900x600")
    window_animal_deletar.resizable(width=False,height=False)
    window_animal_deletar.configure(background="darkorange")

    arca_logo = PhotoImage(file="tkinter_gui/images/arca_white.png")
    top_frame = Frame(window_animal_deletar, width=900, height=150, bg="black", relief="raised")
    top_frame.pack(side=TOP)

    logo_label = Label(top_frame, image=arca_logo, bg="black")
    logo_label.place(x=40, y=20)

    title_label = Label(top_frame, text="ZOOLÓGICO ARCA DE NOÉ", font=("Century Gothic", 20), bg="black", fg="white")
    title_label.place(x=280, y=55)

    back_image = PhotoImage(file="tkinter_gui/images/back_20.png")

    back_label = Button(window_animal_deletar, image=back_image, bg="darkorange", command=voltar)
    back_label.place(x=40, y=180)

    id_animal_label = Label(window_animal_deletar, text="ID do Animal: ", font=("Century Gothic", 8, "bold"), bg="darkorange", fg="black")
    id_animal_label.pack(pady=(8,0))  # utilizar somente o pack(y1,y2) para centralizar / padding Y, primeiro valor top, segundo valor bottom
    id_animal_entry = Entry(window_animal_deletar, width=30)
    id_animal_entry.pack()

    bottom_frame = Frame(window_animal_deletar, width=900, height=100, bg="black", relief="raised")
    bottom_frame.pack(side=BOTTOM)

    submit_botao = Button(window_animal_deletar, text="DELETAR", font=("Century Gothic", 10, "bold"), width=15 , bg="black", fg="darkorange", relief="raised", command=sql_animal_del)
    submit_botao.pack(pady=10)

    window_animal_deletar.mainloop()

def DEL_FUNCIONARIO():
    def voltar():
        window_animal_deletar.destroy()
        main_window() # se tentar voltar para abrir_cadastro(), vai dar erro pois a def abrir_cadastro() vai tentar deletar a main_window, que já está apagada pois você já a apagou abrindo a def CAD_ANIMAL

    def sql_animal_del(): # funcao sempre em cima
        id_funcionario = id_funcionario_entry.get()

        comando_sql = f'''DELETE FROM funcionarios WHERE Id = {id_funcionario}'''

        cursor.execute(comando_sql)
        conexao_banco.commit()

        voltar()

    window_excluir.destroy()

    global window_animal_deletar
    window_animal_deletar = Tk()

    window_animal_deletar.title("The Gurizes Development LTDA - Painel de Exclusão: FUNCIONÁRIO")
    window_animal_deletar.geometry("900x600")
    window_animal_deletar.resizable(width=False,height=False)
    window_animal_deletar.configure(background="darkorange")

    arca_logo = PhotoImage(file="tkinter_gui/images/arca_white.png")
    top_frame = Frame(window_animal_deletar, width=900, height=150, bg="black", relief="raised")
    top_frame.pack(side=TOP)

    logo_label = Label(top_frame, image=arca_logo, bg="black")
    logo_label.place(x=40, y=20)

    title_label = Label(top_frame, text="ZOOLÓGICO ARCA DE NOÉ", font=("Century Gothic", 20), bg="black", fg="white")
    title_label.place(x=280, y=55)

    back_image = PhotoImage(file="tkinter_gui/images/back_20.png")

    back_label = Button(window_animal_deletar, image=back_image, bg="darkorange", command=voltar)
    back_label.place(x=40, y=180)

    id_funcionario_label = Label(window_animal_deletar, text="ID do Funcionário: ", font=("Century Gothic", 8, "bold"), bg="darkorange", fg="black")
    id_funcionario_label.pack(pady=(8,0))  # utilizar somente o pack(y1,y2) para centralizar / padding Y, primeiro valor top, segundo valor bottom
    id_funcionario_entry = Entry(window_animal_deletar, width=30)
    id_funcionario_entry.pack()

    bottom_frame = Frame(window_animal_deletar, width=900, height=100, bg="black", relief="raised")
    bottom_frame.pack(side=BOTTOM)

    submit_botao = Button(window_animal_deletar, text="DELETAR", font=("Century Gothic", 10, "bold"), width=15 , bg="black", fg="darkorange", relief="raised", command=sql_animal_del)
    submit_botao.pack(pady=10)

    window_animal_deletar.mainloop()

def DEL_HABITAT():
    def voltar():
        window_animal_deletar.destroy()
        main_window() # se tentar voltar para abrir_cadastro(), vai dar erro pois a def abrir_cadastro() vai tentar deletar a main_window, que já está apagada pois você já a apagou abrindo a def CAD_ANIMAL

    def sql_animal_del(): # funcao sempre em cima
        id_habitat = id_habitat_entry.get()

        comando_sql = f'''UPDATE habitat SET Tipo = "NULL", Tamanho = 0, Clima = "NULL" WHERE Id = {id_habitat}''' # como habitat serve como uma foreign key para outras tabelas, decidi apenas limpar os valores escrevendo "NULL" 

        cursor.execute(comando_sql)
        conexao_banco.commit()

        voltar()

    window_excluir.destroy()

    global window_animal_deletar
    window_animal_deletar = Tk()

    window_animal_deletar.title("The Gurizes Development LTDA - Painel de Exclusão: HABITAT")
    window_animal_deletar.geometry("900x600")
    window_animal_deletar.resizable(width=False,height=False)
    window_animal_deletar.configure(background="darkorange")

    arca_logo = PhotoImage(file="tkinter_gui/images/arca_white.png")
    top_frame = Frame(window_animal_deletar, width=900, height=150, bg="black", relief="raised")
    top_frame.pack(side=TOP)

    logo_label = Label(top_frame, image=arca_logo, bg="black")
    logo_label.place(x=40, y=20)

    title_label = Label(top_frame, text="ZOOLÓGICO ARCA DE NOÉ", font=("Century Gothic", 20), bg="black", fg="white")
    title_label.place(x=280, y=55)

    back_image = PhotoImage(file="tkinter_gui/images/back_20.png")

    back_label = Button(window_animal_deletar, image=back_image, bg="darkorange", command=voltar)
    back_label.place(x=40, y=180)

    id_habitat_label = Label(window_animal_deletar, text="ID do Habitat: ", font=("Century Gothic", 8, "bold"), bg="darkorange", fg="black")
    id_habitat_label.pack(pady=(8,0))  # utilizar somente o pack(y1,y2) para centralizar / padding Y, primeiro valor top, segundo valor bottom
    id_habitat_entry = Entry(window_animal_deletar, width=30)
    id_habitat_entry.pack()

    bottom_frame = Frame(window_animal_deletar, width=900, height=100, bg="black", relief="raised")
    bottom_frame.pack(side=BOTTOM)

    submit_botao = Button(window_animal_deletar, text="DELETAR", font=("Century Gothic", 10, "bold"), width=15 , bg="black", fg="darkorange", relief="raised", command=sql_animal_del)
    submit_botao.pack(pady=10)

    window_animal_deletar.mainloop()

def DEL_INGRESSO():
    def voltar():
        window_animal_deletar.destroy()
        main_window() # se tentar voltar para abrir_cadastro(), vai dar erro pois a def abrir_cadastro() vai tentar deletar a main_window, que já está apagada pois você já a apagou abrindo a def CAD_ANIMAL

    def sql_animal_del(): # funcao sempre em cima
        id_ingresso = id_ingresso_entry.get()

        comando_sql = f'''UPDATE ingressos SET Tipo = "NULL", Preco = 0, Datavalidade = "1000-01-01", Quantidade = 0, Desconto = 0 WHERE Id = {id_ingresso}''' # como ingressos também serve como uma foreign key para outras tabelas, decidi apenas limpar os valores

        cursor.execute(comando_sql)
        conexao_banco.commit()

        voltar()

    window_excluir.destroy()

    global window_animal_deletar
    window_animal_deletar = Tk()

    window_animal_deletar.title("The Gurizes Development LTDA - Painel de Exclusão: INGRESSO")
    window_animal_deletar.geometry("900x600")
    window_animal_deletar.resizable(width=False,height=False)
    window_animal_deletar.configure(background="darkorange")

    arca_logo = PhotoImage(file="tkinter_gui/images/arca_white.png")
    top_frame = Frame(window_animal_deletar, width=900, height=150, bg="black", relief="raised")
    top_frame.pack(side=TOP)

    logo_label = Label(top_frame, image=arca_logo, bg="black")
    logo_label.place(x=40, y=20)

    title_label = Label(top_frame, text="ZOOLÓGICO ARCA DE NOÉ", font=("Century Gothic", 20), bg="black", fg="white")
    title_label.place(x=280, y=55)

    back_image = PhotoImage(file="tkinter_gui/images/back_20.png")

    back_label = Button(window_animal_deletar, image=back_image, bg="darkorange", command=voltar)
    back_label.place(x=40, y=180)

    id_ingresso_label = Label(window_animal_deletar, text="ID do Ingresso: ", font=("Century Gothic", 8, "bold"), bg="darkorange", fg="black")
    id_ingresso_label.pack(pady=(8,0))  # utilizar somente o pack(y1,y2) para centralizar / padding Y, primeiro valor top, segundo valor bottom
    id_ingresso_entry = Entry(window_animal_deletar, width=30)
    id_ingresso_entry.pack()

    bottom_frame = Frame(window_animal_deletar, width=900, height=100, bg="black", relief="raised")
    bottom_frame.pack(side=BOTTOM)

    submit_botao = Button(window_animal_deletar, text="DELETAR", font=("Century Gothic", 10, "bold"), width=15 , bg="black", fg="darkorange", relief="raised", command=sql_animal_del)
    submit_botao.pack(pady=10)

    window_animal_deletar.mainloop()

def DEL_LOJA():
    def voltar():
        window_animal_deletar.destroy()
        main_window() # se tentar voltar para abrir_cadastro(), vai dar erro pois a def abrir_cadastro() vai tentar deletar a main_window, que já está apagada pois você já a apagou abrindo a def CAD_ANIMAL

    def sql_animal_del(): # funcao sempre em cima
        id_loja = id_loja_entry.get()

        comando_sql = f'''DELETE FROM lojas WHERE Id = {id_loja}'''

        cursor.execute(comando_sql)
        conexao_banco.commit()

        voltar()

    window_excluir.destroy()

    global window_animal_deletar
    window_animal_deletar = Tk()

    window_animal_deletar.title("The Gurizes Development LTDA - Painel de Exclusão: LOJA")
    window_animal_deletar.geometry("900x600")
    window_animal_deletar.resizable(width=False,height=False)
    window_animal_deletar.configure(background="darkorange")

    arca_logo = PhotoImage(file="tkinter_gui/images/arca_white.png")
    top_frame = Frame(window_animal_deletar, width=900, height=150, bg="black", relief="raised")
    top_frame.pack(side=TOP)

    logo_label = Label(top_frame, image=arca_logo, bg="black")
    logo_label.place(x=40, y=20)

    title_label = Label(top_frame, text="ZOOLÓGICO ARCA DE NOÉ", font=("Century Gothic", 20), bg="black", fg="white")
    title_label.place(x=280, y=55)

    back_image = PhotoImage(file="tkinter_gui/images/back_20.png")

    back_label = Button(window_animal_deletar, image=back_image, bg="darkorange", command=voltar)
    back_label.place(x=40, y=180)

    id_loja_label = Label(window_animal_deletar, text="ID da Loja: ", font=("Century Gothic", 8, "bold"), bg="darkorange", fg="black")
    id_loja_label.pack(pady=(8,0))  # utilizar somente o pack(y1,y2) para centralizar / padding Y, primeiro valor top, segundo valor bottom
    id_loja_entry = Entry(window_animal_deletar, width=30)
    id_loja_entry.pack()

    bottom_frame = Frame(window_animal_deletar, width=900, height=100, bg="black", relief="raised")
    bottom_frame.pack(side=BOTTOM)

    submit_botao = Button(window_animal_deletar, text="DELETAR", font=("Century Gothic", 10, "bold"), width=15 , bg="black", fg="darkorange", relief="raised", command=sql_animal_del)
    submit_botao.pack(pady=10)

    window_animal_deletar.mainloop()

def DEL_VISITANTE():
    def voltar():
        window_animal_deletar.destroy()
        main_window() # se tentar voltar para abrir_cadastro(), vai dar erro pois a def abrir_cadastro() vai tentar deletar a main_window, que já está apagada pois você já a apagou abrindo a def CAD_ANIMAL

    def sql_animal_del(): # funcao sempre em cima
        id_visitante = id_visitante_entry.get()

        comando_sql = f'''DELETE FROM visitantes WHERE Id = {id_visitante}'''

        cursor.execute(comando_sql)
        conexao_banco.commit()

        voltar()

    window_excluir.destroy()

    global window_animal_deletar
    window_animal_deletar = Tk()

    window_animal_deletar.title("The Gurizes Development LTDA - Painel de Exclusão: VISITANTE")
    window_animal_deletar.geometry("900x600")
    window_animal_deletar.resizable(width=False,height=False)
    window_animal_deletar.configure(background="darkorange")

    arca_logo = PhotoImage(file="tkinter_gui/images/arca_white.png")
    top_frame = Frame(window_animal_deletar, width=900, height=150, bg="black", relief="raised")
    top_frame.pack(side=TOP)

    logo_label = Label(top_frame, image=arca_logo, bg="black")
    logo_label.place(x=40, y=20)

    title_label = Label(top_frame, text="ZOOLÓGICO ARCA DE NOÉ", font=("Century Gothic", 20), bg="black", fg="white")
    title_label.place(x=280, y=55)

    back_image = PhotoImage(file="tkinter_gui/images/back_20.png")

    back_label = Button(window_animal_deletar, image=back_image, bg="darkorange", command=voltar)
    back_label.place(x=40, y=180)

    id_visitante_label = Label(window_animal_deletar, text="ID do Visitante: ", font=("Century Gothic", 8, "bold"), bg="darkorange", fg="black")
    id_visitante_label.pack(pady=(8,0))  # utilizar somente o pack(y1,y2) para centralizar / padding Y, primeiro valor top, segundo valor bottom
    id_visitante_entry = Entry(window_animal_deletar, width=30)
    id_visitante_entry.pack()

    bottom_frame = Frame(window_animal_deletar, width=900, height=100, bg="black", relief="raised")
    bottom_frame.pack(side=BOTTOM)

    submit_botao = Button(window_animal_deletar, text="DELETAR", font=("Century Gothic", 10, "bold"), width=15 , bg="black", fg="darkorange", relief="raised", command=sql_animal_del)
    submit_botao.pack(pady=10)

    window_animal_deletar.mainloop()

# JANELAS SQL INSERTION - PESQUISAR

def PES_ANIMAL():
    
    def voltar():
        window_animal_pesquisar.destroy()
        main_window() # se tentar voltar para abrir_cadastro(), vai dar erro pois a def abrir_cadastro() vai tentar deletar a main_window, que já está apagada pois você já a apagou abrindo a def CAD_ANIMAL

    window_pesquisar.destroy()

    global window_animal_pesquisar
    window_animal_pesquisar = Tk()

    window_animal_pesquisar.title("The Gurizes Development LTDA - Painel de Pesquisa: ANIMAL")
    window_animal_pesquisar.geometry("900x600")
    window_animal_pesquisar.resizable(width=False,height=False)
    window_animal_pesquisar.configure(background="darkorange")

    arca_logo = PhotoImage(file="tkinter_gui/images/arca_white.png")
    top_frame = Frame(window_animal_pesquisar, width=900, height=150, bg="black", relief="raised")
    top_frame.pack(side=TOP)

    logo_label = Label(top_frame, image=arca_logo, bg="black")
    logo_label.place(x=40, y=20)

    title_label = Label(top_frame, text="ZOOLÓGICO ARCA DE NOÉ", font=("Century Gothic", 20), bg="black", fg="white")
    title_label.place(x=280, y=55)

    # TREEVIEW
    comando_sql = f'''SELECT * FROM animais'''
    cursor.execute(comando_sql)
    
    tree = ttk.Treeview(window_animal_pesquisar, show='headings')
    style = ttk.Style()
    style.configure("Treeview", background="black", foreground="darkorange")


    tree['columns'] = ('Id','Nome', 'Especie', 'Genero', 'Datanasc', 'Origem', 'Saúde', 'Alimentacao', 'Idhabitat')

    # Formatação das colunas
    tree.column("Id", anchor=tk.CENTER, width=50)
    tree.column("Nome", anchor=tk.CENTER, width=80)
    tree.column("Especie", anchor=tk.CENTER, width=60)
    tree.column("Genero", anchor=tk.CENTER, width=50)
    tree.column("Datanasc", anchor=tk.CENTER, width=60)
    tree.column("Origem", anchor=tk.CENTER, width=60)
    tree.column("Saúde", anchor=tk.CENTER, width=80)
    tree.column("Alimentacao", anchor=tk.CENTER, width=80)
    tree.column("Idhabitat", anchor=tk.CENTER, width=50)

    # Cabeçalho das colunas
    tree.heading("Id", text="ID_Animal", anchor=tk.CENTER)
    tree.heading("Nome", text="Nome", anchor=tk.CENTER)
    tree.heading("Especie", text="Espécie", anchor=tk.CENTER)
    tree.heading("Genero", text="Gênero", anchor=tk.CENTER)
    tree.heading("Datanasc", text="Data Nasc.", anchor=tk.CENTER)
    tree.heading("Origem", text="Origem", anchor=tk.CENTER)
    tree.heading("Saúde", text="Saúde", anchor=tk.CENTER)
    tree.heading("Alimentacao", text="Alimentação", anchor=tk.CENTER)
    tree.heading("Idhabitat", text="ID_Habitat", anchor=tk.CENTER)

    for row in cursor:
        tree.insert('','end',values=row)

    tree.pack(pady=50)

    bottom_frame = Frame(window_animal_pesquisar, width=900, height=100, bg="black", relief="raised")
    bottom_frame.pack(side=BOTTOM)

    button_volt = Button(bottom_frame, text="VOLTAR PARA O MENU", font=("Century Gothic", 20), bg="darkorange", fg="black", command=voltar)
    button_volt.place(x=300, y=20)

    window_animal_pesquisar.mainloop()

def PES_FUNCIONARIO():
    
    def voltar():
        window_animal_pesquisar.destroy()
        main_window() # se tentar voltar para abrir_cadastro(), vai dar erro pois a def abrir_cadastro() vai tentar deletar a main_window, que já está apagada pois você já a apagou abrindo a def CAD_ANIMAL

    window_pesquisar.destroy()

    global window_animal_pesquisar
    window_animal_pesquisar = Tk()

    window_animal_pesquisar.title("The Gurizes Development LTDA - Painel de Pesquisa: FUNCIONÁRIO")
    window_animal_pesquisar.geometry("900x600")
    window_animal_pesquisar.resizable(width=False,height=False)
    window_animal_pesquisar.configure(background="darkorange")

    arca_logo = PhotoImage(file="tkinter_gui/images/arca_white.png")
    top_frame = Frame(window_animal_pesquisar, width=900, height=150, bg="black", relief="raised")
    top_frame.pack(side=TOP)

    logo_label = Label(top_frame, image=arca_logo, bg="black")
    logo_label.place(x=40, y=20)

    title_label = Label(top_frame, text="ZOOLÓGICO ARCA DE NOÉ", font=("Century Gothic", 20), bg="black", fg="white")
    title_label.place(x=280, y=55)

    # TREEVIEW
    comando_sql = f'''SELECT * FROM funcionarios'''
    cursor.execute(comando_sql)
    
    tree = ttk.Treeview(window_animal_pesquisar, show='headings')
    style = ttk.Style()
    style.configure("Treeview", background="black", foreground="darkorange")


    tree['columns'] = ('Id','Nome', 'Cargo', 'Datacontratacao', 'Email', 'Telefone')

    # Formatação das colunas
    tree.column("Id", anchor=tk.CENTER, width=30)
    tree.column("Nome", anchor=tk.CENTER, width=80)
    tree.column("Cargo", anchor=tk.CENTER, width=60)
    tree.column("Datacontratacao", anchor=tk.CENTER, width=50)
    tree.column("Email", anchor=tk.CENTER, width=60)
    tree.column("Telefone", anchor=tk.CENTER, width=60)

    # Cabeçalho das colunas
    tree.heading("Id", text="ID", anchor=tk.CENTER)
    tree.heading("Nome", text="Nome", anchor=tk.CENTER)
    tree.heading("Cargo", text="Cargo", anchor=tk.CENTER)
    tree.heading("Datacontratacao", text="Data Contr.", anchor=tk.CENTER)
    tree.heading("Email", text="E-mail", anchor=tk.CENTER)
    tree.heading("Telefone", text="Telefone", anchor=tk.CENTER)

    for row in cursor:
        tree.insert('','end',values=row)

    tree.pack(pady=50)

    bottom_frame = Frame(window_animal_pesquisar, width=900, height=100, bg="black", relief="raised")
    bottom_frame.pack(side=BOTTOM)

    button_volt = Button(bottom_frame, text="VOLTAR PARA O MENU", font=("Century Gothic", 20), bg="darkorange", fg="black", command=voltar)
    button_volt.place(x=300, y=20)

    window_animal_pesquisar.mainloop()

def PES_HABITAT():
    
    def voltar():
        window_animal_pesquisar.destroy()
        main_window() # se tentar voltar para abrir_cadastro(), vai dar erro pois a def abrir_cadastro() vai tentar deletar a main_window, que já está apagada pois você já a apagou abrindo a def CAD_ANIMAL

    window_pesquisar.destroy()

    global window_animal_pesquisar
    window_animal_pesquisar = Tk()

    window_animal_pesquisar.title("The Gurizes Development LTDA - Painel de Pesquisa: HABITAT")
    window_animal_pesquisar.geometry("900x600")
    window_animal_pesquisar.resizable(width=False,height=False)
    window_animal_pesquisar.configure(background="darkorange")

    arca_logo = PhotoImage(file="tkinter_gui/images/arca_white.png")
    top_frame = Frame(window_animal_pesquisar, width=900, height=150, bg="black", relief="raised")
    top_frame.pack(side=TOP)

    logo_label = Label(top_frame, image=arca_logo, bg="black")
    logo_label.place(x=40, y=20)

    title_label = Label(top_frame, text="ZOOLÓGICO ARCA DE NOÉ", font=("Century Gothic", 20), bg="black", fg="white")
    title_label.place(x=280, y=55)

    # TREEVIEW
    comando_sql = f'''SELECT * FROM habitat'''
    cursor.execute(comando_sql)
    
    tree = ttk.Treeview(window_animal_pesquisar, show='headings')
    style = ttk.Style()
    style.configure("Treeview", background="black", foreground="darkorange")


    tree['columns'] = ('Id','Tipo', 'Tamanho', 'Clima')

    # Formatação das colunas
    tree.column("Id", anchor=tk.CENTER, width=30)
    tree.column("Tipo", anchor=tk.CENTER, width=80)
    tree.column("Tamanho", anchor=tk.CENTER, width=60)
    tree.column("Clima", anchor=tk.CENTER, width=50)

    # Cabeçalho das colunas
    tree.heading("Id", text="ID", anchor=tk.CENTER)
    tree.heading("Tipo", text="Tipo", anchor=tk.CENTER)
    tree.heading("Tamanho", text="Tamanho", anchor=tk.CENTER)
    tree.heading("Clima", text="Clima", anchor=tk.CENTER)

    for row in cursor:
        tree.insert('','end',values=row)

    tree.pack(pady=50)

    bottom_frame = Frame(window_animal_pesquisar, width=900, height=100, bg="black", relief="raised")
    bottom_frame.pack(side=BOTTOM)

    button_volt = Button(bottom_frame, text="VOLTAR PARA O MENU", font=("Century Gothic", 20), bg="darkorange", fg="black", command=voltar)
    button_volt.place(x=300, y=20)

    window_animal_pesquisar.mainloop()

def PES_INGRESSOS():
    
    def voltar():
        window_animal_pesquisar.destroy()
        main_window() # se tentar voltar para abrir_cadastro(), vai dar erro pois a def abrir_cadastro() vai tentar deletar a main_window, que já está apagada pois você já a apagou abrindo a def CAD_ANIMAL

    window_pesquisar.destroy()

    global window_animal_pesquisar
    window_animal_pesquisar = Tk()

    window_animal_pesquisar.title("The Gurizes Development LTDA - Painel de Pesquisa: INGRESSO")
    window_animal_pesquisar.geometry("900x600")
    window_animal_pesquisar.resizable(width=False,height=False)
    window_animal_pesquisar.configure(background="darkorange")

    arca_logo = PhotoImage(file="tkinter_gui/images/arca_white.png")
    top_frame = Frame(window_animal_pesquisar, width=900, height=150, bg="black", relief="raised")
    top_frame.pack(side=TOP)

    logo_label = Label(top_frame, image=arca_logo, bg="black")
    logo_label.place(x=40, y=20)

    title_label = Label(top_frame, text="ZOOLÓGICO ARCA DE NOÉ", font=("Century Gothic", 20), bg="black", fg="white")
    title_label.place(x=280, y=55)

    # TREEVIEW
    comando_sql = f'''SELECT * FROM ingressos'''
    cursor.execute(comando_sql)
    
    tree = ttk.Treeview(window_animal_pesquisar, show='headings')
    style = ttk.Style()
    style.configure("Treeview", background="black", foreground="darkorange")


    tree['columns'] = ('Id','Tipo', 'Preco', 'Datavalidade', 'Quantidade', 'Desconto')

    # Formatação das colunas
    tree.column("Id", anchor=tk.CENTER, width=30)
    tree.column("Tipo", anchor=tk.CENTER, width=80)
    tree.column("Preco", anchor=tk.CENTER, width=60)
    tree.column("Datavalidade", anchor=tk.CENTER, width=50)
    tree.column("Quantidade", anchor=tk.CENTER, width=60)
    tree.column("Desconto", anchor=tk.CENTER, width=60)

    # Cabeçalho das colunas
    tree.heading("Id", text="ID", anchor=tk.CENTER)
    tree.heading("Tipo", text="Tipo", anchor=tk.CENTER)
    tree.heading("Preco", text="Preco", anchor=tk.CENTER)
    tree.heading("Datavalidade", text="Data Val.", anchor=tk.CENTER)
    tree.heading("Quantidade", text="Quantidade", anchor=tk.CENTER)
    tree.heading("Desconto", text="Desconto", anchor=tk.CENTER)

    for row in cursor:
        tree.insert('','end',values=row)

    tree.pack(pady=50)

    bottom_frame = Frame(window_animal_pesquisar, width=900, height=100, bg="black", relief="raised")
    bottom_frame.pack(side=BOTTOM)

    button_volt = Button(bottom_frame, text="VOLTAR PARA O MENU", font=("Century Gothic", 20), bg="darkorange", fg="black", command=voltar)
    button_volt.place(x=300, y=20)

    window_animal_pesquisar.mainloop()

def PES_LOJA():
    
    def voltar():
        window_animal_pesquisar.destroy()
        main_window() # se tentar voltar para abrir_cadastro(), vai dar erro pois a def abrir_cadastro() vai tentar deletar a main_window, que já está apagada pois você já a apagou abrindo a def CAD_ANIMAL

    window_pesquisar.destroy()

    global window_animal_pesquisar
    window_animal_pesquisar = Tk()

    window_animal_pesquisar.title("The Gurizes Development LTDA - Painel de Pesquisa: LOJA")
    window_animal_pesquisar.geometry("900x600")
    window_animal_pesquisar.resizable(width=False,height=False)
    window_animal_pesquisar.configure(background="darkorange")

    arca_logo = PhotoImage(file="tkinter_gui/images/arca_white.png")
    top_frame = Frame(window_animal_pesquisar, width=900, height=150, bg="black", relief="raised")
    top_frame.pack(side=TOP)

    logo_label = Label(top_frame, image=arca_logo, bg="black")
    logo_label.place(x=40, y=20)

    title_label = Label(top_frame, text="ZOOLÓGICO ARCA DE NOÉ", font=("Century Gothic", 20), bg="black", fg="white")
    title_label.place(x=280, y=55)

    # TREEVIEW
    comando_sql = f'''SELECT * FROM lojas'''
    cursor.execute(comando_sql)
    
    tree = ttk.Treeview(window_animal_pesquisar, show='headings')
    style = ttk.Style()
    style.configure("Treeview", background="black", foreground="darkorange")


    tree['columns'] = ('Id','Nome', 'Servico', 'Horario', 'Receita', 'Email', 'Telefone')

    # Formatação das colunas
    tree.column("Id", anchor=tk.CENTER, width=30)
    tree.column("Nome", anchor=tk.CENTER, width=80)
    tree.column("Servico", anchor=tk.CENTER, width=60)
    tree.column("Horario", anchor=tk.CENTER, width=50)
    tree.column("Receita", anchor=tk.CENTER, width=60)
    tree.column("Email", anchor=tk.CENTER, width=60)
    tree.column("Telefone", anchor=tk.CENTER, width=60)

    # Cabeçalho das colunas
    tree.heading("Id", text="ID", anchor=tk.CENTER)
    tree.heading("Nome", text="Nome", anchor=tk.CENTER)
    tree.heading("Servico", text="Servico", anchor=tk.CENTER)
    tree.heading("Horario", text="Horário Func.", anchor=tk.CENTER)
    tree.heading("Receita", text="Receita", anchor=tk.CENTER)
    tree.heading("Email", text="E-mail", anchor=tk.CENTER)
    tree.heading("Telefone", text="Telefone", anchor=tk.CENTER)

    for row in cursor:
        tree.insert('','end',values=row)

    tree.pack(pady=50)

    bottom_frame = Frame(window_animal_pesquisar, width=900, height=100, bg="black", relief="raised")
    bottom_frame.pack(side=BOTTOM)

    button_volt = Button(bottom_frame, text="VOLTAR PARA O MENU", font=("Century Gothic", 20), bg="darkorange", fg="black", command=voltar)
    button_volt.place(x=300, y=20)

    window_animal_pesquisar.mainloop()

def PES_VISITANTE():
    
    def voltar():
        window_animal_pesquisar.destroy()
        main_window() # se tentar voltar para abrir_cadastro(), vai dar erro pois a def abrir_cadastro() vai tentar deletar a main_window, que já está apagada pois você já a apagou abrindo a def CAD_ANIMAL

    window_pesquisar.destroy()

    global window_animal_pesquisar
    window_animal_pesquisar = Tk()

    window_animal_pesquisar.title("The Gurizes Development LTDA - Painel de Pesquisa: VISITANTE")
    window_animal_pesquisar.geometry("900x600")
    window_animal_pesquisar.resizable(width=False,height=False)
    window_animal_pesquisar.configure(background="darkorange")

    arca_logo = PhotoImage(file="tkinter_gui/images/arca_white.png")
    top_frame = Frame(window_animal_pesquisar, width=900, height=150, bg="black", relief="raised")
    top_frame.pack(side=TOP)

    logo_label = Label(top_frame, image=arca_logo, bg="black")
    logo_label.place(x=40, y=20)

    title_label = Label(top_frame, text="ZOOLÓGICO ARCA DE NOÉ", font=("Century Gothic", 20), bg="black", fg="white")
    title_label.place(x=280, y=55)

    # TREEVIEW
    comando_sql = f'''SELECT * FROM visitantes'''
    cursor.execute(comando_sql)
    
    tree = ttk.Treeview(window_animal_pesquisar, show='headings')
    style = ttk.Style()
    style.configure("Treeview", background="black", foreground="darkorange")


    tree['columns'] = ('Id','Nome', 'Datavisita', 'Idingresso')

    # Formatação das colunas
    tree.column("Id", anchor=tk.CENTER, width=30)
    tree.column("Nome", anchor=tk.CENTER, width=80)
    tree.column("Datavisita", anchor=tk.CENTER, width=60)
    tree.column("Idingresso", anchor=tk.CENTER, width=50)

    # Cabeçalho das colunas
    tree.heading("Id", text="ID", anchor=tk.CENTER)
    tree.heading("Nome", text="Nome", anchor=tk.CENTER)
    tree.heading("Datavisita", text="Data Vis.", anchor=tk.CENTER)
    tree.heading("Idingresso", text="ID Ing.", anchor=tk.CENTER)

    for row in cursor:
        tree.insert('','end',values=row)

    tree.pack(pady=50)

    bottom_frame = Frame(window_animal_pesquisar, width=900, height=100, bg="black", relief="raised")
    bottom_frame.pack(side=BOTTOM)

    button_volt = Button(bottom_frame, text="VOLTAR PARA O MENU", font=("Century Gothic", 20), bg="darkorange", fg="black", command=voltar)
    button_volt.place(x=300, y=20)

    window_animal_pesquisar.mainloop()

main_window()