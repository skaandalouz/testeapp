from tkinter import *

from tkinter import messagebox

window = Tk()

#nome do app no título
window.title("skandalouz app - version 1.0.0")

#lbl = Label(window, text="bem-vindos!", font=("Arial Bold", 25))

#lbl.grid(column=0, row=0)

#tamanho da janela ao abrir app
window.geometry('800x480') 

# Desabilitar a opção de maximizar a janela
window.resizable(False, False)

#fonte e tamanho
font=("SegoeUI",10) 
highlightthickness=0

#borda botão
bd=1 

def clicked():

     messagebox.showinfo('Envio Confirmado!', 'Doação feita! Muito Obrigado!') 

btn = Button(window, text="Sobre", bg="white", fg="black", command=clicked)

btn.grid(column=0, row=0)

btn = Button(window, text="Sobre", bg="white", fg="black")

btn.grid(column=2, row=0)

#messagebox.showwarning('Aviso', 'Você acaba de ser hackeado!')  #shows warning message

#messagebox.showerror('pague para usar', 'Efetue o pagamento para o cpf: 123.456.789.12', font= (26))    #shows error message

window.mainloop()


