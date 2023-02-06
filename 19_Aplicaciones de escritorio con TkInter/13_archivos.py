from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog  #Esto es para interactuar con archivos

root = Tk()
root.title('Ejercicios con archivos')

def open():
    global imgTk
    root.filename = filedialog.askopenfilename(title = 'Elige una foto' , filetypes=(("Archivos PNG","*.png"),("Archivos JPG","*.jpg"),("Todos","*")))
    l = Label(root, text=root.filename)
    l.pack()
    img=Image.open(root.filename)
    imgTk=ImageTk.PhotoImage(img)

    l2= Label(root, image=imgTk)
    l2.pack()

btn=Button(root, text="Cargar imagen", command=open)
btn.pack()
root.mainloop()