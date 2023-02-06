from tkinter import *

root=Tk()
root.title("Prueba Option menu")
root.geometry("500x500")

def enviar():
    l=Label(root,text=value.get())
    l.pack()

#En la lista estan las opciones
lista =[
    'Chanchito feliz', 
    'Chanchito triste', 
    'Chanchito emocionado'
]

value=StringVar()
value.set(lista[0]) #Valor por defecto de la lista

#Dicha lista se pasa con un asterisco como paremetro. En value esta el valor seleccionado
drop=OptionMenu(root, value, *lista)
drop.pack()

btn=Button(root,text="Comprobar valor combobox", command=enviar)
btn.pack()

root.mainloop()