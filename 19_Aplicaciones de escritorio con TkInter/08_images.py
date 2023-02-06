from tkinter import *
from PIL import ImageTk, Image  #PIL es de la libreria "Pillow" la cual se descarga con pip3 install Pillow

root = Tk()
root.title("Prueba imagen")

###Esto es para mostar la imagen en el gestor de imagenes del sistema operativo
#imagen = Image.open('1a.png')  #Guardar la imagen abierta en la variable
#imagen.show()   #Abre y MUESTRA la imagen en el visor del sist oper

###Esto es para mostrar la imagen en la aplicacion
img=ImageTk.PhotoImage(Image.open("1a.png"))
l=Label(image=img)
l.pack()

root.mainloop()
