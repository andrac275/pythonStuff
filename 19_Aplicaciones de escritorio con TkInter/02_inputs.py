from tkinter import *

root = Tk()
root.title('Ventana de inputs')
root.geometry("300x300")

##INPUT: en python se llama Entry
e = Entry(root, width=40)
e.pack()
e.insert(0, "Ingresa tu nombre.") #Esto es como hacer un placeholder o insertar cosas de una base de datos

def click():
    texto = "Nombre: "+ e.get() #e.get() OBTENER el TEXTO de la etiqueta Entry 'e' y lo guarda en texto, en este caso
        ##guardaria dentro "Nombre: LoQueHayaEnElEntry"
    l.configure(text=texto) #Configure es para CAMBIAR el CONTENIDO de una etiqueta LABEL. Al dar click pues, se cambia el
        ##label de la etiqueta 'l'
    e.delete(0,END) #delete BORRA el CONTENIDO del Entry 'e' en este caso des de la posicion 0, que es el inicio, al final END

btn = Button(root, text="click", command=click)
btn.pack()

l=Label(root,text="Nombre: ")
l.pack()

root.mainloop()