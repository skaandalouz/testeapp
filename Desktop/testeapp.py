from tkinter import *

from tkinter import messagebox

window = Tk()

window.title("skandalouz app")

#lbl = Label(window, text="bem-vindos!", font=("Arial Bold", 25))

#lbl.grid(column=0, row=0)

window.geometry('800x600')

def clicked():

     messagebox.showinfo('Envio Confirmado!', 'Doação feita! Muito Obrigado!') 

btn = Button(window, text="Sobre", bg="white", fg="black", command=clicked)

btn.grid(column=0, row=0)

#messagebox.showwarning('Aviso', 'Você acaba de ser hackeado!')  #shows warning message

#messagebox.showerror('pague para usar', 'Efetue o pagamento para o cpf: 123.456.789.12', font= (26))    #shows error message

window.mainloop()


