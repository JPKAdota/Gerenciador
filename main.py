from tkinter import *
from tkinter import Tk, ttk
#importando pillow
from PIL import ImageTk,Image
#importando barra de progresso
from tkinter.ttk import Progressbar

#importando Matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.figure import Figure



#cores
co0 = "#2e2d2b"
co1 = "#feffff"
co2 = "#4fa882"
co3 = "#38576b"
co4 = "#403d3d"
co5 = "#e06636"
co6 = "#038cfc"
co7 = "#3fbfb9"
co8 = "#263238"
co9 = "#e9edf5"

colors = ['#5588bb', '#66bbbb', '#99bb55', '#ee9944', '#444466', '#bb5555']

#criando janela
janela =  Tk()
janela.title()
janela.geometry("900x650")
janela.configure(background=co9)
janela.resizable(width=FALSE, height=FALSE)

style= ttk.Style(janela)
style.theme_use("clam")

#criando frames para divisão da tela
frameCima = Frame(janela, width=1043, height=50, bg=co1, relief="flat")
frameCima.grid(row=0, column=0)

frameMeio = Frame(janela, width=1043, height=361, bg=co1,pady=20, relief="raised")
frameMeio.grid(row=1, column=0, padx=0, pady=1, sticky=NSEW)

frameBaixo = Frame(janela, width=1043, height=300, bg=co1, relief="flat")
frameBaixo.grid(row=2, column=0, padx=10, pady=0, sticky=NSEW)

#Trabalhando no Frame Cima
#acessando a imagem
app_img = Image.open('logo.png')
app_img = app_img.resize((45,45)) #dimensões da imagem
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frameCima, image=app_img, text=" Orçamento pessoal", width=900, compound=LEFT, padx=5, relief=RAISED, anchor=NW, font=('Verdana 20 bold'), bg=co1, fg=co4)
app_logo.place(x=0, y=0)


#Percentagem----------------------------------------------

def percentagem():
    l_nome = Label(frameMeio, text="Porcentagem da Receita Gasta", height=1, anchor=NW, font=('Verdana 12'), bg= co1, fg=co4)
    l_nome.place(x=7,y=5)

    style= ttk.Style()
    style.theme_use('default')
    style.configure("black.Horizontal.TProgressbar", background='#daed6b')
    style.configure("TProgressbar", thickness=25)

    bar = Progressbar(frameMeio, length=180)
    bar.place(x=10,y=35)
    bar['value'] = 50

    valor = 50

    l_percetagem = Label(frameMeio, text="{:,.2f}%".format(valor), anchor=NW, font=('Verdana 12'), bg= co1, fg=co4)
    l_percetagem.place(x=200,y=35)




percentagem()
janela.mainloop()