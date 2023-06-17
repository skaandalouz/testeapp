from tkinter.ttk import *
from tkinter import *
from tkinter import messagebox
from playsound import playsound
from time import strftime
import locale

window = Tk()

# nome do app no título
window.title("skandalouz app - version 1.0.0")

#lbl = Label(window, text="bem-vindos!", font=("Arial Bold", 25))

#lbl.grid(column=0, row=0)

# tamanho da janela ao abrir app
#window.geometry('600x200')
#window.geometry('600x350')
window.geometry('750x350')
#window.geometry('1920x1080')

# Cor de fundo
#window.configure(bg="black")

# icone do aplicativo
window.iconbitmap("imagens/urbanterror.ico")

# Desabilitar a opção de maximizar a janela
window.resizable(False, False)

# fonte e tamanho
font=("SegoeUI", 10) 
highlightthickness=0

def mytime():
    locale.setlocale(locale.LC_TIME, "pt_BR")
    time_string = strftime('%A, %x \n  %X ') # time format
    l1.config(text=time_string)
    l1.after(1000,mytime) # time delay of 1000 milliseconds

my_font = ('SegoeUI',12,'bold')
l1=Label(window, font=my_font, fg="black", justify='right',state='disabled')
l1.place(x=590,y=5)  

#l2=Label(window,font='SegoeUI',text="Horário atual:", state='disabled')
#l2.place(x=565,y=-2)

def msgaosair():

     messagebox.showinfo("Thanks","Obrigado por utilizar esse aplicativo!")
     window.destroy()
     #window.quit()
     #window.after(100,window.quit)

#messagebox.showinfo("ALL RIGHTS RESERVED ®", "Feito por Skandalouz")

# logo urban terror
logo = PhotoImage(file="imagens/urbanterror.png")
logo = logo.subsample(1,1)

logo2 = PhotoImage(file="imagens/cummins.png")
logo2 = logo2.subsample(15,15)

logo3 = PhotoImage(file="imagens/jsl.png")
logo3 = logo3.subsample(15,15)

def umfig1 ():
    
 um1=PhotoImage(file="imagens/material.png")
 figuraum1 = Label(window, image=um1)
 figuraum1.place(x=300,y=300)



#logo4 = PhotoImage(file="imagens/jsl2.png")
#logo4 = logo4.subsample(15,15)

#logo5 = PhotoImage(file="imagens/dinho.gif", format="gif -index 0")
#logo5 = logo5.subsample(1,1)

#figura5 = Label(image=logo5)
#figura5.grid(row=0, column=7,pady=(500),padx=(1))

frameCnt = 37
frames = [PhotoImage(file='imagens/dinho1.gif',format = 'gif -index %i' %(i)) for i in range(frameCnt)]

def update(ind):
    
    frame = frames[ind]
    ind += 1
    if ind == frameCnt:
        ind = 0
    label.configure(image=frame)
    label.place(x=470, y=140)
    window.after(60, update, ind)
label = Label(window)
#label.after(3000, label.destroy)
#label.pack()
window.after(0, update, 0)


figura2 = Label(image=logo2) 
figura2.grid(row=0,column=3,pady=(19),padx=(20))

figura3 = Label(image=logo3) 
figura3.grid(row=0,column=6,pady=(0),padx=(0))

#figura4 = Label(image=logo4) 
#figura4.grid(row=0,column=7,pady=(0),padx=(0))


#figura1 = Label(image=logo)
#figura1.grid (row=2, column=3,pady=(0), padx=(300,0))

# borda botão
bd=1 

#def clicked2():
     
#     vnome=Entry(window)
#     vnome.place(x=250, y=30)

#btn = Button(window, text="Sobre", bg="white", fg="black", command=clicked2)

#btn.grid(column=2, row=0)

     # ação
     
def clear():
      vLD.set(0)
      vUM.set(0)
      print("Limpo!")
      #window.geometry('600x200')
      if vLD.get() == 0 & vUM.get() == 0:
          txt3=Label(window, font="Arial 11 bold italic underline", text="SELECIONE UMA LINHA!")
          txt3.place(x=35,y=100)
          txt3.after(2000, txt3.destroy)
          comboUM.place_forget()
          comboLD.place_forget()
          labelcombo.place_forget()
          

# checkbutton
fr_quadro1=LabelFrame(window, text="  Selecionar Linha:  ", font="corbel 12 bold", borderwidth=3,relief="groove")
fr_quadro1.place(x=250,y=30,width=300,height=100)

btn = Button(window, text="Limpar",font="corbel 10 bold", bg="white", fg="black", command=clear)
btn.place(x=493, y=10, width=55,height=25)

# texto
#txt1=Label(window,text="Selecionar a linha:",font="corbel 12 bold",foreground="blue")
#txt1.place(x=255,y=35)

vLD=IntVar()
vUM=IntVar()

#label combobox
labelcombo = Label(window,font="corbel 10 bold underline", text="Escolha o PN:")
labelcombo.place(x=20,y=130)          

#criando combobox
comboLD=Combobox(window)
comboUM=Combobox(window)

def comboboxUM():
     #definindo valores combobox
     comboUM['values'] = ('Linha UM','A066X019','A066X013','A060Y299','A064H090')
     #comboUM.current(0)
     comboUM['state'] = 'readonly'
     comboUM.place(x=105,y=130)

def comboboxLD():
     #definindo valores combobox
     comboLD['values'] = ('Linha LD','A066X026', 'A059W666','A055E026', 'A063T161','A062U294')
     #comboLD.current(0)
     comboLD['state'] = 'readonly'
     comboLD.place(x=105,y=130)          

cb_LD=Checkbutton(fr_quadro1 ,text="Linha LD",variable=vLD,onvalue=1,offvalue=0, command=lambda:[linhaLDClicado(),comboboxLD()], font="corbel 11 bold")
cb_LD.pack(side=LEFT)  

def visualizar():
     if vLD.get() == 1:
      ve=comboLD.get()
      print("PN:"+ve)
     else:
       ve=comboUM.get()
       print("PN:"+ve)

     if comboUM.get() == "A066X019":
       print("Abraçadeira")
       #playsound('music/A066X019.wav')

       a066x019=Label(window, font='corbel 20 bold', bg="black")
       a066x019.place(x=150,y=200)
       a066x019.config(text="Abraçadeira", fg="white")
       a066x019.after(10000, a066x019.place_forget)

     elif comboUM.get() == "A066X013":
       print("Abraçadeira Menor") 

       #playsound('music/A066X013.wav')
       
       a066x013=Label(window, font='corbel 20 bold', bg="black")
       a066x013.place(x=150,y=200)
       a066x013.config(text="Abraçadeira menor", fg="white")


btn_ver=Button(window, text="Visualizar",command=visualizar)
btn_ver.place(x=25, y=155)

#figura1 = Label(image=logo)
#figura1.grid(row=0, column=8,pady=(110), padx=(250)) 


def linhaUMClicado():
     #messagebox.showinfo("Aviso", "Linha UM, selecionada!") 
     if vUM.get() == 1:
          labelcombo = Label(window,font="corbel 10 bold underline", text="Escolha o PN:")
          labelcombo.place(x=20,y=130)
          print("LINHA UM SELECIONADA!") , vLD.set(0) 
          txt2=Label(window, font="Arial 11 bold italic underline", text="Linha UM Selecionada!")
          txt2.place(x=35,y=100)
          txt2.after(2000, txt2.destroy)
     else:
          vLD.set(1) 

def linhaLDClicado():
     #messagebox.showinfo("Aviso", "Linha LD, selecionada!")
     #window.geometry('600x400')
     if vLD.get() == 1:
          labelcombo = Label(window,font="corbel 10 bold underline", text="Escolha o PN:")
          labelcombo.place(x=20,y=130)
          print("LINHA LD SELECIONADA!") , vUM.set(0)
          txt1=Label(window, font="Arial 11 bold italic underline", text="Linha LD Selecionada!")
          txt1.place(x=35,y=100)
          txt1.after(2000, txt1.destroy)
     else:
          vUM.set(1)          
              

cb_UM=Checkbutton(fr_quadro1, text="Linha UM",variable=vUM,onvalue=1,offvalue=0, command=lambda:[linhaUMClicado(),comboboxUM()], font="corbel 11 bold")
cb_UM.pack(side=RIGHT)  
  

#cb_UM.place(x=90, y=34)  

def sobre():
     #for widget in window.winfo_children():
     #widget.destroy()
      barradeMenus=Menu(window)
      Informações=Menu(barradeMenus,tearoff=0)
      Informações.add_command(label="Início",command='')
      Informações.add_separator()
      Informações.add_command(label="Sair",command=msgaosair)
      barradeMenus.add_cascade(label="Menu",menu=Informações)
      window.config(menu=barradeMenus)

    
      



# barra de menus
barradeMenus=Menu(window)
Informações=Menu(barradeMenus,tearoff=0)
Informações.add_command(label="Início",command='')
Informações.add_command(label="Sobre",command=sobre)
Informações.add_separator()
Informações.add_command(label="Sair",command=msgaosair)
barradeMenus.add_cascade(label="Menu",menu=Informações)



#sobreframe=Frame(window,width=400, height=400, bg="red")

window.config(menu=barradeMenus)
     
#messagebox.showwarning('Aviso', 'Você acaba de ser hackeado!')  #shows warning message

#messagebox.showerror('pague para usar', 'Efetue o pagamento para o cpf: 123.456.789.12', font= (26))    #shows error message

mytime()
window.mainloop()




