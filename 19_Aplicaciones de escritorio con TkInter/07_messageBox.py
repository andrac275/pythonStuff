#Los messagebox son las alertas. Los popups que informan al usuario. En python se tiene warning, informacion ,error, askquestion, askokcancel y askyesno. 
#Estan abajo comentadas las funciones, simplemente descomentar y dejar una activa para probarlas

from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Pruebas messagebox")

# def click():
#     messagebox.showwarning('TituloVentana','Esto es un warning')

# def click():
#     messagebox.showinfo('TituloVentana','Esto es para informacion')

# def click():
#     messagebox.showerror('TituloVentana','Esto es un error')

##AskQuestion: Este no devuelve true o false, devuelve un string con yes o no que se tiene que comprobar
# def click():
#     respuesta = messagebox.askquestion('TituloVentana','Stash tonto???')
#     if respuesta == 'yes':
#         messagebox.showinfo("Respuesta", "La respuesta fue: " + respuesta)
#     else:
#         messagebox.showinfo("Respuesta", "La respuesta fue: " + respuesta)

## AskOkCancel: Este devuelve true o false y en los botones pone Aceptar o Cancel
# def click():
#     respuesta = messagebox.askokcancel('TituloVentana','Desea realizar accion???')
#     #Este devuelve un booleano, no como el de arriba que devolvia 'yes' o 'no'
#     if respuesta:
#         messagebox.showinfo("Respuesta", "La respuesta fue: Aceptar")
#     else:
#         messagebox.showinfo("Respuesta", "La respuesta fue: Cancel")

##AskYesNo: Este devuelve true o false y en los botones pone si o no. Es igual que el de arriba pero con los botones
    ## cambiados. El nombre es lo que cambia
def click():
    respuesta = messagebox.askyesno('TituloVentana','Desea realizar accion???')
    #Este devuelve un booleano, no como el de arriba que devolvia 'yes' o 'no'
    if respuesta:
        messagebox.showinfo("Respuesta", "La respuesta fue: Si")
    else:
        messagebox.showinfo("Respuesta", "La respuesta fue: No")


btn = Button(root, text="Presioname para alerta", command=click)
btn.pack()

root.mainloop()