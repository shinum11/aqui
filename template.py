#template de como vai ficar a interface visual + ou -
#Criar uma função para pegar o os valores
from tkinter import *
janela = Tk()
janela.title("Mochila")
janela.geometry("500x500")

t1 = Label(janela,text="Digite o peso maximo da mochila: ")
t1.grid(row=0,column=0)
peso = Entry(janela, width = 10)
peso.grid(row=0,column=1 )

t2 = Label(janela,text="Digite o numero de cromossomos: ")
t2.grid(row=1,column=0)
n_cromossomos = Entry(janela, width = 10)
n_cromossomos.grid(row=1,column=1 )

t3 = Label(janela,text="Digite o numero de gerações: ")
t3.grid(row=2,column=0)
geracoes = Entry(janela, width = 10)
geracoes.grid(row=2,column=1 )

p = peso.get()
c = n_cromossomos.get()
g = geracoes.get()

#Essa vai ser a função que vai rodar o algorotimo ao clique
def ph():
    ...

botao = Button(janela, text="Iniciar", command=ph)
botao.grid(row=3,column=1)

janela.mainloop()



