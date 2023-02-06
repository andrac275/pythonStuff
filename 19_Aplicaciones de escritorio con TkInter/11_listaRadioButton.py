from tkinter import *

root=Tk()
root.title("Ejemplo lista radioButton")

#Esto para el listado de radioButtons
CHANCHITOS=[
    ('Feliz','Feliz'),
    ('Triste','Triste'),
    ('Amargado','Amargado'),
    ('Wolfgang','Wolfgang')
]

chanchito = StringVar()
chanchito.set('Wolfgang')

for text,chancho in CHANCHITOS:
    Radiobutton(root,text=text, variable=chanchito, value=chancho).pack()

l= Label(root, textvariable=chanchito)
l.pack()

root.mainloop()
