import tkinter as tk 

def enviar ():
    nome_animal = nome.get()
    print_animal.config(text=f"O nome do animal cadastrado é: {nome_animal}")

window = tk.Tk() # define uma variável para o TKINTER

window.title("JANELA PRINCIPAL") # título da aba

window.geometry("1200x800") # define o tamanho da janela do tkinter
window.resizable(False, False) # argumenta que o tamanho da janela não pode ser reajustável

hello = tk.Label(window, text="Olá, Mundo!") # label = texto, imagem, etc
hello.pack(pady=0) # coloca a label na window usando o pack() - ordem de colunas. Pady é o padding

botao_sair = tk.Button(window, text="SAIR", width=25, command=window.destroy)
botao_sair.pack(pady=8)

input_text = tk.Label(window, text="Digite o nome do animal: ")
input_text.pack(pady=0)

nome = tk.Entry(window) # input
nome.pack(pady=0)

botao_enviar = tk.Button(window, text="ENVIAR", width=25, command=enviar)
botao_enviar.pack(pady=8)

print_animal = tk.Label(window, text="")
print_animal.pack(pady=0)

window.mainloop()
