#Importe das pastas


from tkinter import *
from tkinter import ttk

#Cores

cor1 = "#1e1f1e" #Preto
cor2 = "#feffff" #Branco
cor3 = "#38576b" #Azul
cor4 = "#ECEFF1" #Cinza
cor5 = "#FFAB40" #Laranja


janela = Tk()
janela.title('Calculadora')
janela.geometry('235x310+200+200')
janela.config(bg=cor1)
janela.resizable(False,False)

#criando frames

frame_tela = Frame(janela,width=235,height=50,bg=cor3)
frame_tela.grid(row=0,column=0)

frame_corpo = Frame(janela,width=235,height=268)
frame_corpo.grid(row=1,column=0)

#todos os valores
todos_valores = ''

#funções

def input_values(event):
    global todos_valores

    if(event == 'c'):
        todos_valores = ''
    elif(event=='='):
        todos_valores = eval(todos_valores)
    else:
        todos_valores = todos_valores + str(event)
    
    
    
    #passagem de valor

    valor_texto.set(todos_valores)




#criando label

valor_texto = StringVar()
app_label = Label(frame_tela,textvariable=valor_texto,width=16,height=2,padx=7,pady=2,relief=FLAT,anchor='e',justify=RIGHT,font=('Ivy 17'),bg=cor3,fg=cor2)
app_label.place(x=0,y=0)

#criando botoes

b_limpar = Button(frame_corpo,command=lambda:input_values('c'), text='C',width=11,height=2,bg=cor4,font=('Ivy 13 bold'),relief=RAISED,overrelief=RIDGE)
b_limpar.grid(row=0,column=0,columnspan=2,sticky="ew")

b_porc = Button(frame_corpo,command=lambda:input_values('%'), text='%',width=5,height=2,bg=cor4,font=('Ivy 13 bold'),relief=RAISED,overrelief=RIDGE)
b_porc.grid(row=0,column=2,sticky="ew")

b_div= Button(frame_corpo,command=lambda:input_values('/'), text='/',width=5,height=2,bg=cor5,fg=cor2,font=('Ivy 13 bold'),relief=RAISED,overrelief=RIDGE)
b_div.grid(row=0,column=3,sticky="ew")
#-----------------------------------------------------------------------------
b_1 = Button(frame_corpo,command=lambda:input_values('1'),text='1',width=5,height=2,bg=cor4,font=('Ivy 13 bold'),relief=RAISED,overrelief=RIDGE)
b_1.grid(row=1,column=0,sticky="ew")

b_2 = Button(frame_corpo,command=lambda:input_values('2'), text='2',width=5,height=2,bg=cor4,font=('Ivy 13 bold'),relief=RAISED,overrelief=RIDGE)
b_2.grid(row=1,column=1,sticky="ew")

b_3 = Button(frame_corpo,command=lambda:input_values('3'), text='3',width=5,height=2,bg=cor4,font=('Ivy 13 bold'),relief=RAISED,overrelief=RIDGE)
b_3.grid(row=1,column=2,sticky="ew")

bt_mult = Button(frame_corpo,command=lambda:input_values('*'), text='*',width=5,height=2,bg=cor5,fg=cor2,font='Ivy 13 bold',relief=RAISED,overrelief=RIDGE)
bt_mult.grid(row=1,column=3,sticky='ew')
#-------------------------------------------------------------------------------
b_4 = Button(frame_corpo,command=lambda:input_values('4'), text='4',width=5,height=2,bg=cor4,font=('Ivy 13 bold'),relief=RAISED,overrelief=RIDGE)
b_4.grid(row=2,column=0,sticky="ew")

b_5 = Button(frame_corpo,command=lambda:input_values('5'), text='5',width=5,height=2,bg=cor4,font=('Ivy 13 bold'),relief=RAISED,overrelief=RIDGE)
b_5.grid(row=2,column=1,sticky="ew")

b_6 = Button(frame_corpo,command=lambda:input_values('6'), text='6',width=5,height=2,bg=cor4,font=('Ivy 13 bold'),relief=RAISED,overrelief=RIDGE)
b_6.grid(row=2,column=2,sticky="ew")

bt_dim = Button(frame_corpo,command=lambda:input_values('-'), text='-',width=5,height=2,bg=cor5,fg=cor2,font='Ivy 13 bold',relief=RAISED,overrelief=RIDGE)
bt_dim.grid(row=2,column=3,sticky='ew')
#-------------------------------------------------------------------------------
b_7 = Button(frame_corpo,command=lambda:input_values('7'), text='7',width=5,height=2,bg=cor4,font=('Ivy 13 bold'),relief=RAISED,overrelief=RIDGE)
b_7.grid(row=3,column=0,sticky="ew")

b_8 = Button(frame_corpo,command=lambda:input_values('8'), text='8',width=5,height=2,bg=cor4,font=('Ivy 13 bold'),relief=RAISED,overrelief=RIDGE)
b_8.grid(row=3,column=1,sticky="ew")

b_9 = Button(frame_corpo,command=lambda:input_values('9'), text='9',width=5,height=2,bg=cor4,font=('Ivy 13 bold'),relief=RAISED,overrelief=RIDGE)
b_9.grid(row=3,column=2,sticky="ew")

bt_som = Button(frame_corpo,command=lambda:input_values('+'), text='+',width=5,height=2,bg=cor5,fg=cor2,font='Ivy 13 bold',relief=RAISED,overrelief=RIDGE)
bt_som.grid(row=3,column=3,sticky='ew')
#-------------------------------------------------------------------------------
b_0 = Button(frame_corpo,command=lambda:input_values('0'), text='0',width=5,height=2,bg=cor4,font=('Ivy 13 bold'),relief=RAISED,overrelief=RIDGE)
b_0.grid(row=4,column=0,columnspan=2,sticky="ew")

bt_pon = Button(frame_corpo,command=lambda:input_values('.'), text='.',width=5,heigh=2,bg=cor4,fg=cor1,font=('Ivy 13 bold'),relief=RAISED,overrelief=RIDGE)
bt_pon.grid(row=4,column=2,sticky='ew')

bt_igual = Button(frame_corpo,command=lambda:input_values('='),text='=',width=5,height=2,bg=cor5,fg=cor2,font=('Ivy, 13 bold'),relief=RAISED,overrelief=RIDGE)

bt_igual.grid(row=4,column=3,sticky='ew')




janela.mainloop()



