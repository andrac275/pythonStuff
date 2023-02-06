from tkinter import *
from PIL import Image, ImageTk

root=Tk()
root.title("Ejercicio Carrusel")

img1=ImageTk.PhotoImage(Image.open("images/1a.png"))
img2=ImageTk.PhotoImage(Image.open("images/1b.png"))
img3=ImageTk.PhotoImage(Image.open("images/2.png"))
img4=ImageTk.PhotoImage(Image.open("images/3.png"))

lista = [img1,img2,img3,img4]

l = Label(root,image=img1)
l.grid(row=0,column=0,columnspan=3) #Se pone columnspan3 para dejar espacio al boton de avanzar y retroceder, que estaran en la primera y tercera columna

def adelante(img_num):
    #El global se usa para seleccionar las variables del alcance superior, no las de dentro de la funcion.
    #Para este caso pues estará usando la Label y los dos buttons que se definieron en las lineas:
        #14,57,58
    global l
    global btn_atras
    global btn_adelante
    
    l.grid_forget() #Borra la imagen de la grilla+
    l=Label(root,image=lista[img_num])
    btn_atras = Button(root, text="<-", command=lambda: atras(img_num - 1))
    btn_adelante = Button(root, text="->", command=lambda: adelante(img_num + 1))
    
    if img_num == len(lista)-1:
        btn_adelante = Button(root, text="N/A",state=DISABLED)

    l.grid(row=0,column=0,columnspan=3)
    btn_atras.grid(row=1,column=0)
    btn_adelante.grid(row=1,column=2)

def atras(img_num):
    #El global se usa para seleccionar las variables del alcance superior, no las de dentro de la funcion.
    #Para este caso pues estará usando la Label y los dos buttons que se definieron en las lineas:
        #14,57,58
    global l
    global btn_atras
    global btn_adelante
    
    l.grid_forget() #Borra la imagen de la grilla+
    l=Label(root,image=lista[img_num])
    btn_atras = Button(root, text="<-", command=lambda: atras(img_num - 1))
    btn_adelante = Button(root, text="->", command=lambda: adelante(img_num + 1))
    
    if img_num == 0:
        btn_atras = Button(root, text="N/A",state=DISABLED)

    l.grid(row=0,column=0,columnspan=3)
    btn_atras.grid(row=1,column=0)
    btn_adelante.grid(row=1,column=2)

btn_atras = Button(root, text="N/A", state=DISABLED)
btn_adelante = Button(root, text="->", command=lambda: adelante(1))

btn_atras.grid(row=1, column=0)
btn_adelante.grid(row=1,column=2)

root.mainloop()