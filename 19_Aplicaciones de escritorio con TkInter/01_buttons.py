from tkinter import *

root = Tk()
root.title('Ventana de botones')
root.geometry("300x300")

label = Label(root,text="boton clickado")
def click():
    ##instanciar Label dentro de la funcion crear una label por cada click, una solucion es instanciarla arriba
        ##(fuera de la funcion) y hacer el label.pack en la funcion, eso hace que la etiqueta solo aparezca una 
        ##vez y no una etiqueta distinta cada vez que se da click en el boton
    #label = Label(root,text="boton clickado")
    label.pack()

#Argumentos de Button(dondeRenderizar, tituloBoton, funcionEjecutar, colorTexto,colorFondo)
    ##bg y fg acepta colores escritos red, yellow... y hexadecimal. ffff00 es amarillo, por eso tiene fondo amarillo.
btn = Button(root, text="clickMe",command=click,fg="red",bg="#ffff00")
btn.pack()

root.mainloop()