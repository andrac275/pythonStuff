from tkinter import *

root = Tk()
root.title("Frame test")
#root.geometry("300x300")

#Esto es el frame, el cual no estara visible hasta que se le agregue contenido
    #Los argumentos text, padx,pady y borderwidth son opcionales, se pueden no poner simplemente
        #padx y pady se usa para darle un margen.
frame = LabelFrame(root, text="Login",padx=10, pady=10,borderwidth=10) #aqui añade el padding por la parte interior del FRAME
frame.pack(padx=50, pady=50)    #Aqui el padding se añade en la parte externa del FRAME

#Estos widgets se añaden al frame en lugar del root que se habia hecho hasta ahora
l=Label(frame, text="Nombre con LabelFrame")
btn=Button(frame, text="Salir",command=root.quit)#El command root.quit hace que al clickar el boton ejecute esa funcion predefinida que cierra la app
l.pack()
btn.pack()

#--------------------------------
#Aqui es Frame en lugar de LabelFrame. Esto sirve para agrupar cosas pero sin que se muestre al usuario
frame2 = Frame(root, padx=10, pady=10,borderwidth=10) #da igual que se ponga padx pady o borderwidth, no va a mostrar nada al usuario
frame2.pack(padx=50, pady=50)

#Estos widgets se añaden al frame en lugar del root que se habia hecho hasta ahora
l2=Label(frame2, text="Nombre con Frame")
btn2=Button(frame2, text="Salir",command=root.quit)#El command root.quit hace que al clickar el boton ejecute esa funcion predefinida que cierra la app
l2.pack()
btn2.pack()

root.mainloop()