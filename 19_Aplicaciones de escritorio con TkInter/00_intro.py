from tkinter import *   #Esto es para la interfaz grafica. Por defecto
# esta las instalaciones de python, no hace falta instalar nada

root = Tk()#Crear la instancia de tkInter
root.title('Titulo ventana')
root.geometry('500x300') #ancho x alto por defect

###Widgets: Un widget es todo lo que podemos colocar en una UI
    ##Los widget, como la Label, queda disponible al importar tkinter
# label = Label(root, text='Nombre etiqueta') #(DondeMostrarla, nombreEtiqueta)
# label.pack() #Esto hace el elemento visible definido en la linea anterior

# Label(root, text='Etiqueta y pack a la vez').pack() #Esto es una manera alternativa de hacerlo
    ##hacerlo todo en una linea, la creacion de la Label y el pack, esta vez no se guarda en una variable


    ##Grilla:En lugar de usar pack se usa grid
l1=Label(root, text="Etiqueta 1")
l2=Label(root, text="Etiqueta 2")
l3=Label(root, text="          ") #En la fila 1 habran espacios, separando etiqueta1  y etiqueta2


l1.grid(row = 0, column=0)
l2.grid(row = 2, column=2)
l3.grid(row = 1, column = 1)






root.mainloop() #Esta instruccion escucha cambios de interfaz