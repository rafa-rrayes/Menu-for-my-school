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
    #define title
    titulo = 'Venda de doces 9º ano.     '+ datetime.datetime.today().strftime('   %d/%m/%Y')
    #create a screen
    tela = Tk ()
    tela.geometry('750x600+0+0')
    tela.title('Venda De Doces')

    #create a frame on top
    topo = Frame(tela, width = 750, height = 150, bd=9, relief='raise')
    topo.pack(side = TOP)
    #por o titulo
    texto_topo = Label(topo, font=('courier', 30), text=titulo)
    texto_topo.pack()

    #create frame on left
    esquerda = Frame(tela, width = 250, height = 550, bd=8, relief='raise')
    esquerda.pack(side = LEFT)
    esquerda.pack_propagate(0)

    #create frame on midle, top and bottom
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
    

    #create frame on left
    direita = Frame(tela, width = 250, height = 550, borderwidth=8, relief='raise')
    direita.pack(side = LEFT)
    direita.pack_propagate(0)

    #create text for midle and right
    texto_meio = Label(meio_cima, font=('courier', 18), text='Pagamento:')
    texto_meio.pack(side= TOP)
    texto_meio_b = Label(meio_baixo, font=('courier', 18), text='Pedido:')
    texto_meio_b.pack(side= TOP)
    texto_direita = Label(direita, font=('courier', 18), text='Vendidos:')
    texto_direita.pack(side= TOP)
    
    #create a new candy button
    def addc():
        texto = input('which candy?')
        the_candy = Frame(esquerda, bd = 5, relief ='raise')
        the_candy.pack()
        i = Button(the_candy, text=(texto), width = 245, height = 2, activebackground = 'Gray', command = oi(texto),  bd = 5, relief='raise', font =('courier', 20))
        i.pack(side=TOP)
        
    #add candy button
    global adicionar
    adicionar = Button(esquerda, bd= 4, font='courier', relief='raise', text= 'add candy', command=addc)
    adicionar.pack(side=BOTTOM)
    


    tela.mainloop()
