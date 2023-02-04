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

##Labels pasando variables
def clickVariable():
    texto = "Nombre label con variable: "+ e.get() #e.get() OBTENER el TEXTO de la etiqueta Entry 'e' y lo guarda en texto, en este caso
        ##guardaria dentro "Nombre: LoQueHayaEnElEntry"
    
    textVariableee.set(texto) #Se ha hecho un set del contenido en la variable

    aux= textVariableee.get() #El valor se puede guardar en otras variables para trabajar despues con el mismo
    print("Valor despues del set: " , aux)

    e.delete(0,END) #delete BORRA el CONTENIDO del Entry 'e' en este caso des de la posicion 0, que es el inicio, al final END

btn = Button(root, text="click etiqueta con variable", command=clickVariable)
btn.pack()


textVariableee = StringVar() #Esto es la etiqueta para la variable

lVariable=Label(root,textvariable = textVariableee) #Se asigna en textvariable y se actualiza en el set de la funcion
    #"clickVariable" en el  'textVariableee.set(COSA)'

lVariable.pack()

root.mainloop()