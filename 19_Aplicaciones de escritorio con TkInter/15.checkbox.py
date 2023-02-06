from tkinter import *

root=Tk()
root.title("Pruebas checkbox")

root.geometry("500x500")

var = StringVar()
var.set("Deseleccionado")

def mostrar():
    l=Label(root,text=var.get())
    l.pack()

c= Checkbutton(root, text="Soy un checkbox", variable = var, onvalue="Si",offvalue="Deseleccionado")
c.pack()

btn = Button(root, text="Comprobar valor checkbox", command=mostrar)
btn.pack()

root.mainloop()