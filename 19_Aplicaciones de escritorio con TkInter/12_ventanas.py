from tkinter import *

from PIL import ImageTk,Image

root = Tk()
root.title('Prueba de ventanas')

# Solucion 1: Usando main loop.
# def open():
#     img = ImageTk.PhotoImage(Image.open('images/1a.png'))
#     top = Toplevel() #Esto es para crear la ventana
#     top.title('Ventana emergente')  #Se le puede asignar titulo a dicha ventana
#     #Y colocar widgets.
#     l=Label(top, text="Soy un texto en la ventana emergente")
#     l2=Label(top,image=img)
#     l.pack()
#     l2.pack()
#     top.mainloop()    #hay que poner el mainloop en la nueva ventana sino cuando abre la nueva ventana no aparece
#        #la imagen porque tras ejecutar la funcion pierde el contexto 'img' y se queda en blanco por el garbage colector

# Solucion 2: Usando variable global
# def open():
#     global img  #Al ser img global, no pierde el contexto al ejecutar la funcion y se mantiene mostrando la imagen. El garbage colector NO destruye la variable
#     img = ImageTk.PhotoImage(Image.open('images/1a.png'))
#     top = Toplevel() #Esto es para crear la ventana
#     top.title('Ventana emergente')  #Se le puede asignar titulo a dicha ventana
#     #Y colocar widgets.
#     l=Label(top, text="Soy un texto en la ventana emergente")
#     l2=Label(top,image=img)
#     l.pack()
#     l2.pack()
#     #top.mainloop()   #Aqui no hace falta porque img es global

#Solucion 3: Pasar la imagen como argumento, definiendola antes.
    #Esta en un scope superior la imagen, asi que el garbage colector NO destruye la variable y se muestra correctamente
def open(img):
    top = Toplevel() #Esto es para crear la ventana
    top.title('Ventana emergente')  #Se le puede asignar titulo a dicha ventana
    #Y colocar widgets.
    l=Label(top, text="Soy un texto en la ventana emergente")
    l2=Label(top,image=img)
    l.pack()
    l2.pack()

#Para solucion 1 y 2
#btn = Button(root, text='Click' , command=open).pack()

#Para solucin 3
img = ImageTk.PhotoImage(Image.open('images/1a.png'))
btn = Button(root, text='Click' , command=lambda: open(img)).pack()

root.mainloop()