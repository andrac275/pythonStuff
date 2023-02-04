from tkinter import *

root=Tk()
root.title("Calculadora pies a metros")

def calcular(*args):
    try:
        value = float(pies.get())
        m = int(0.3048 * value * 10000 +0.5) / 10000
        metros.set(m)
    except ValueError: #Si no se puede hacer casting a float, pone en la etiqueta 'ERROR'
        metros.set('ERROR')

frame = Frame(root, pady=3, padx=12)
frame.grid(column=0,row=0)

pies = StringVar()
pies_input= Entry(frame, width = 7, textvariable = pies)
pies_input.grid(column=1, row=0)

metros = StringVar()
Label(frame, textvariable=metros).grid(column=1,row=1)

Button(frame, text="Calcular", command=calcular).grid(column=2, row=2)

Label(frame,text="Pies").grid(column=0,row=0)
Label(frame,text="es igual a").grid(column=0,row=1)
Label(frame,text="metros").grid(column=2,row=1)

pies_input.focus()  #Focus por defecto selecciona el campo de texto pies_input al abrir la aplicacion
root.bind("<Return>",calcular)  #bind es un listener. Cuando se pula "Return" (Return es ENTER) se ejecuta 'calcular'. 
    #Hay que poner en calcular *args para que funcione, porque espera algo.


root.mainloop()