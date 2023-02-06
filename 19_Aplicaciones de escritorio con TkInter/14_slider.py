from tkinter import  *

root = Tk()
root.title("Prueba sliders")

#opcion 1: Al dar click al boton, se llama a la funcion
# vertical = Scale(root, from_=0, to=200)
# horizontal = Scale(root, from_=0, to=200,orient=HORIZONTAL)

#opcion 2: El valor se envia al cambiar el slider
vertical = Scale(root, from_=0, to=200, command= lambda x:enviar())
horizontal = Scale(root, from_=0, to=200,orient=HORIZONTAL, command= lambda x: enviar())

vertical.pack()
horizontal.pack()

def enviar():
    ver.set("Valor del vertical: "+str(vertical.get()))
    hor.set("Valor del horizontal: "+str(horizontal.get()))

ver=StringVar()
hor=StringVar()
ver.set("Valor del vertical: "+str(vertical.get()))
hor.set("Valor del horizontal: "+str(horizontal.get()))
l1=Label(root,textvariable=ver).pack()
l2=Label(root, textvariable=hor).pack()

btn = Button(root, text="Enviar valor slider", command=enviar).pack()

root.mainloop()