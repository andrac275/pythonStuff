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
l=Label(frame, text="Nombre")
btn=Button(frame, text="Salir",command=root.quit)#El command root.quit hace que al clickar el boton ejecute esa funcion predefinida que cierra la app
l.pack()
btn.pack()

root.mainloop()