from tkinter import *

root=Tk()
root.title("Ejemplo radioButton")

r=IntVar()#Esto es para guardar el valor del radio button.
r.set('1')  #El 'set' es para marcar por defecto un radiobutton. lo que hace es mirar el value de los radiobutton y si coincide
    #entonces lo marca. Poner '1' marcara el RadioBut de la linea 12, poner 'asdf' no marca ninguno porque no coincide con ningun value

#'variable' es la variable que observa y a la que le asignara el valor de value, en este caso mira 'r'. 
# 'value' le da el valor a la variable 'r'
Radiobutton(root, text="Opcion 1", variable = r, value = 1).pack()
Radiobutton(root, text="Opcion 2", variable = r, value = 2).pack()

l= Label(root, textvariable=r)
l.pack()

root.mainloop()
