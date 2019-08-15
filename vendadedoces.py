from tkinter import *
import random
import time
import datetime
from tkinter import Tk, StringVar, ttk
def d():
    novo.delete()
def oi(doce):
    global novo
    novo = Checkbutton(master=meio_baixo,  text=doce, bd=5, relief='raise', command=d)
    novo.pack(side=TOP)
def menu():
    #definitr o titulo e os doces
    titulo = 'Venda de doces 9º ano.     '+ datetime.datetime.today().strftime('   %d/%m/%Y')
    #criar uma tela
    tela = Tk ()
    tela.geometry('750x600+0+0')
    tela.title('Venda De Doces')

    #criar um frame no topo
    topo = Frame(tela, width = 750, height = 150, bd=9, relief='raise')
    topo.pack(side = TOP)
    #por o titulo
    texto_topo = Label(topo, font=('courier', 30), text=titulo)
    texto_topo.pack()

    #Criar um frame na esquerda
    esquerda = Frame(tela, width = 250, height = 550, bd=8, relief='raise')
    esquerda.pack(side = LEFT)
    esquerda.pack_propagate(0)

    #Criar um frame no meio, embaixo e em cima
    meio = Frame(tela, width = 250, height = 550, bd = 8,  relief='raise')
    meio.pack(side = LEFT)
    meio.pack_propagate(0)
    global meio_baixo
    meio_baixo = Frame(meio, width = 250, height = 270, bd = 2, relief='raise')
    meio_baixo.pack(side = BOTTOM)
    meio_baixo.pack_propagate(0)
    meio_cima = Frame(meio, width = 250, height =260, bd = 2, relief='raise')
    meio_cima.pack(side = TOP)
    meio_cima.pack_propagate(0)
    

    #Criar um frame na direita
    direita = Frame(tela, width = 250, height = 550, borderwidth=8, relief='raise')
    direita.pack(side = LEFT)
    direita.pack_propagate(0)

    #adicionar texto para o meio e para a direita
    texto_meio = Label(meio_cima, font=('courier', 18), text='Pagamento:')
    texto_meio.pack(side= TOP)
    texto_meio_b = Label(meio_baixo, font=('courier', 18), text='Pedido:')
    texto_meio_b.pack(side= TOP)
    texto_direita = Label(direita, font=('courier', 18), text='Vendidos:')
    texto_direita.pack(side= TOP)
    def addc():
        texto = input('qual doce?')
        i = Button(esquerda, text=(texto), width = 250, height = 2, activebackground = 'Gray', command = oi(texto),  bd = 5, relief='raise', font =('courier', 20))
        i.pack(side=TOP)
    global adicionar
    adicionar = Button(esquerda, bd= 4, font='courier', relief='raise', text= 'adicionar doce', command=addc)
    adicionar.pack(side=BOTTOM)
    


    tela.mainloop()
