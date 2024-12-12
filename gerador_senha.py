from tkinter import *
from tkinter.ttk import Progressbar
import tkinter.messagebox
import pyperclip
import random
import string

# Variáveis Globais
comprimento_senha = 7

def obter_valor_slider(valor):
    global comprimento_senha
    comprimento_senha = int(valor)
    atualizar_progresso()

def atualizar_progresso():
    global comprimento_senha
    forca = (maiusculas.get() + minusculas.get() + caracteres_especiais.get() + numeros.get()) * 5 + comprimento_senha * 5
    barra_progresso['value'] = forca

def gerar_senha():
    if not (maiusculas.get() or minusculas.get() or caracteres_especiais.get() or numeros.get()):
        tkinter.messagebox.showwarning("Seleção inválida", "Por favor, selecione pelo menos uma opção.")
        return

    senha = ""
    conjunto_caracteres = ""
    
    if maiusculas.get(): conjunto_caracteres += string.ascii_uppercase
    if minusculas.get(): conjunto_caracteres += string.ascii_lowercase
    if numeros.get(): conjunto_caracteres += string.digits
    if caracteres_especiais.get(): conjunto_caracteres += string.punctuation
    
    senha = ''.join(random.sample(conjunto_caracteres, comprimento_senha))

    campo_senha.delete(0, END)
    campo_senha.insert(0, senha)

def copiar_para_area_transferencia():
    senha_copiada = campo_senha.get()
    pyperclip.copy(senha_copiada)
    tkinter.messagebox.showinfo("Copiado", "Senha copiada para a área de transferência.")

# Configuração da Janela Principal
root = Tk()
root.title("Gerador de Senha TryCatch")
root.geometry("700x350")

# Título
titulo = Label(root, text="Gerador de Senha TryCatch", fg="Blue", font=("Arial", 15, 'bold'))
titulo.place(x=200, y=10)

# Variáveis de Controle
numeros = IntVar()
minusculas = IntVar()
maiusculas = IntVar()
caracteres_especiais = IntVar()

# Checkbuttons
frame_checkbuttons = Frame(root)
frame_checkbuttons.place(x=100, y=40)

C1 = Checkbutton(frame_checkbuttons, text="A-Z", variable=maiusculas, onvalue=1, offvalue=0, command=atualizar_progresso)
C1.grid(row=0, column=0, padx=5)
C2 = Checkbutton(frame_checkbuttons, text="a-z", variable=minusculas, onvalue=1, offvalue=0, command=atualizar_progresso)
C2.grid(row=0, column=1, padx=5)
C3 = Checkbutton(frame_checkbuttons, text="0-9", variable=numeros, onvalue=1, offvalue=0, command=atualizar_progresso)
C3.grid(row=0, column=2, padx=5)
C4 = Checkbutton(frame_checkbuttons, text="Caracteres Especiais", variable=caracteres_especiais, onvalue=1, offvalue=0, command=atualizar_progresso)
C4.grid(row=0, column=3, padx=5)

# Controle de Comprimento
rotulo_comprimento = Label(root, text="Comprimento", font=("Arial", 11))
rotulo_comprimento.place(x=500, y=80)

s1 = Scale(root, from_=7, to=16, orient=HORIZONTAL, command=obter_valor_slider)
s1.place(x=550, y=70)

# Barra de Progresso
rotulo_forca = Label(root, text="Força da Senha", font=("Arial", 12, "bold"))
rotulo_forca.place(x=280, y=110)

barra_progresso = Progressbar(root, orient=HORIZONTAL, length=400, mode='determinate')
barra_progresso.place(x=150, y=140)

# Botão de Geração
botao_gerar = Button(root, text="Gerar", fg="green", font=("Arial", 10, 'bold'), command=gerar_senha)
botao_gerar.place(x=300, y=180)

# Campo de Senha
campo_senha = Entry(root, width=30)
campo_senha.place(x=220, y=210)

# Botão de Cópia
botao_copiar = Button(root, text="Copiar", fg="green", font=("Arial", 10, 'bold'), command=copiar_para_area_transferencia)
botao_copiar.place(x=320, y=240)

# Ícone da Janela
foto = PhotoImage(file="password.png")
root.iconphoto(False, foto)

# Iniciar o Loop da Interface
root.mainloop()
