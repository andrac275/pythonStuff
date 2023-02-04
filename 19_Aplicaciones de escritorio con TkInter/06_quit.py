from tkinter import *

root= Tk()
root.title("Hola mundo")

exit = Button(root, text="Cerrar aplicacion", command=root.quit)
exit.pack()

root.mainloop()