from tkinter import *
import random
import time
import datetime
from tkinter import Tk, StringVar, ttk
costs = []
global total_do_dia
total_do_dia = []
pags = []
global pedidos
pedidos = []
global oquepediu
oquepediu=[]
letters = ['a', 'b', 'c', 'd', 'e', 'f']
def resetar():
    global texto_meio_c
    texto_meio_c.pack_forget()
    texto_meio_c = Label(meio_cima_cima, font=('courier', 13), text = 'total: $'+ str(sum(costs)))
    texto_meio_c.pack()
def remover(doce, x, cost):
    pedidos.remove(doce)
    costs.remove(int(cost))
    global texto_meio_c
    texto_meio_c.pack_forget()
    texto_meio_c = Label(meio_cima_cima, font=('courier', 13), text = 'total: $'+ str(sum(costs)))
    texto_meio_c.pack()
    x.pack_forget()
def finalizar():
    global nomi
    global costs
    global direita
    total_do_dia.append(sum(costs))
    nome = nomi.get()
    hist = Label(direita, text=('\n'+nome+':'+' '*(18-len(nome))+'Total: $'+str(sum(costs))), font=('courier', 14))
    hist.pack(anchor=NW)
    lista2 = []
    global pedidos
    for i in pedidos:
        if i not in lista2:
            hist = Label(direita, text=('-',i, pedidos.count(i) ), font=('courier', 14))
            hist.pack(anchor=NW)
            lista2.append(i)
    for i in oquepediu:
        i.destroy()
    global ao_todo
    ao_todo.pack_forget()
    global direita_b
    ao_todo = Label(direita_b, font=('courier', 13), text = 'total de hoje: $'+ str(sum(total_do_dia)))
    ao_todo.pack()
    pedidos = []
    pags = []
    costs = []
    resetar()
def soma():
    global credi
    pago = credi.get()
    pags.append(int(pago))
    global texto_meio_c
    texto_meio_c.pack_forget()
    texto_meio_c = Label(meio_cima_cima, font=('courier', 13), text = 'total: $'+ str(sum(costs)))
    texto_meio_c.pack()
    global cred
    cred.pack(side=TOP)
    global troco
    troco.pack_forget()
    troco = Label(meio_cima, text = ('troco', str(-(sum(costs)-int(pago)))), font=('courier', 13))
    troco.pack()
def add_ped(doce, cost):
    pedidos.append(doce)
    costs.append(int(cost))
    global texto_meio_c
    texto_meio_c.pack_forget()
    global meio_cima_cima
    texto_meio_c = Label(meio_cima_cima, font=('courier', 13), text = 'total: $'+ str(sum(costs)))
    texto_meio_c.pack(side = TOP)
    x = ''.join((random.choice(letters)for i in range(5)))
    x = Checkbutton(master=meio_baixo, text=doce, bd=5, relief='raise', command=lambda:remover(doce, x, cost))
    x.pack(side=TOP)
    oquepediu.append(x)
def menu():
    pago = 0
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
    global esquerda
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
    global meio_cima
    meio_cima = Frame(meio, width = 250, height =260, bd = 2, relief='raise')
    meio_cima.pack(side = TOP)
    meio_cima.pack_propagate(0)
    global meio_cima_cima
    meio_cima_cima = Frame(meio_cima, width = 250, height =150)
    meio_cima_cima.pack(side=TOP)

    #criar uma pergunta de nome e finalizar
    fim = Frame(meio_cima, height = 50, width = 250)
    fim.pack(side=BOTTOM)
    nom = Label(fim, text = 'Nome:', font=('courier', 16))
    nom.pack(side=LEFT)
    global nomi
    nomi = Entry(fim, width = 10)
    nomi.pack(side=LEFT)
    final = Button(fim, text= 'finalizar', command = finalizar)
    final.pack(side=LEFT)

    #Criar um frame na direita e em baixo e o texto do total
    global direita
    direita = Frame(tela, width = 250, height = 550, bd=8, relief='raise')
    direita.pack(side = LEFT)
    direita.pack_propagate(0)
    global direita_b
    direita_b = Frame(direita, width = 250, height = 30)
    direita_b.pack(side=BOTTOM)
    global ao_todo
    ao_todo = Label(direita_b, font=('courier', 13), text = 'total de hoje: $'+ str(sum(costs)))
    ao_todo.pack(side = RIGHT)
    #adicionar texto para o meio e para a direita
    texto_meio = Label(meio_cima_cima, font=('courier', 18), text='Pagamento:')
    texto_meio.pack(side= TOP)
    texto_meio_b = Label(meio_baixo, font=('courier', 18), text='Pedido:')
    texto_meio_b.pack(side= TOP)
    texto_direita = Label(direita, font=('courier', 18), text='Vendidos:')
    texto_direita.pack(side= TOP)
    global texto_meio_c
    texto_meio_c = Label(meio_cima_cima, font=('courier', 13), text = 'total: $'+ str(sum(pags)))
    texto_meio_c.pack(side = TOP)
    global cred
    cred = Frame(meio_cima, width=130, height = 60, bd = 3, relief='raise')
    cred.pack(side=TOP)
    cred.pack_propagate(0)
    cre = Label(cred, text = 'pago:', font=('courier', 13))
    cre.pack(side=LEFT)
    global credi
    credi = Entry(cred, width = 3)
    credi.pack(side=LEFT)
    cr = Button(cred, text='  ', font=('courier', 10), command = soma)
    cr.pack(side=LEFT)
    global troco
    troco = Label(meio_cima, text = ('troco', str(sum(costs)-pago)), font=('courier', 13))
    troco.pack()
    def addc(): 
        global nome_do_doce
        global preco_do_doce
        texto = nome_do_doce.get()
        textod = texto
        preco = preco_do_doce.get()
        cost = preco
        new_doce= Frame(esquerda, height =30, width = 250, bd= 5, relief='sunken')
        new_doce.pack(side=TOP)
        novo_doce = Button(new_doce, text=(texto, '$' + str(preco)), width = 250, height = 2, activebackground = 'Gray', command =lambda: add_ped(textod, cost), font =('courier', 20))
        novo_doce.pack(side=TOP)
    def caixinha():
        caixinha = Tk()
        caixinha.geometry('300x150')
        caixinha.title('Adicionar Doce')
        textinho = Label(caixinha, text='Doce:', font=('courier', 14))
        textinho.pack(side=TOP)
        global nome_do_doce
        nome_do_doce = Entry(caixinha, bd = 3, relief='raise')
        nome_do_doce.pack(side=TOP)
        global preco_do_doce
        preco_do_doce = Entry(caixinha, bd = 3, relief='raise')
        preco_do_doce.pack(side=BOTTOM)
        textinhop = Label(caixinha, text='Preco:', font=('courier', 14))
        textinhop.pack(side=BOTTOM)
        confirmar = Button(caixinha, text='Adicionar', font=('courier', 16), command= addc)
        confirmar.pack(side=TOP)
    global adicionar
    adicionar = Button(esquerda, bd= 4, font='courier', relief='raise', text= 'adicionar doce', command=caixinha)
    adicionar.pack(side=BOTTOM)
    tela.mainloop()
menu()
