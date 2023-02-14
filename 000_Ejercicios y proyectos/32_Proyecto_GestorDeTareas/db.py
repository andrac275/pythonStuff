from tkinter import *
import sqlite3  #esto va incluido en python,, igual que el tkinter, asi no hay que mirar una DB externo.
    #funciona similar a mysql en cuanto a 
    
root = Tk()
root.title("To do list")
root.geometry("500x500")

conn = sqlite3.connect("todo.db")

c= conn.cursor()

#Crear la tabla del todo si no existiera
c.execute("""
    CREATE TABLE if not exists todo(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        description TEXT NOT NULL,
        completed BOOLEAN NOT NULL
    )
""")
conn.commit()

#Currying: es crear una funcion dentro de una funcion para retrasar la ejecucion de la misma
# Esto guarda el valor del id y devuelve el valor actual y no el ultimo valor del id, que es el
# que se iteraba en el bucle for que llama a complete  
def complete(id):
    #Por convenio se genera el mismo nombre de funcion que la externa pero con una barra baja para 
    #diferenciar una de la otra y si sale algun error, saber cual de las dos es.
    def _complete():
        print(id)
    return _complete

def render_todos():
    rows = c.execute("SELECT * FROM todo").fetchall()
    print(rows)

    for i in range(0, len(rows)):
        id = rows[i][0]
        completed = rows[i][3] #La cuarta columna (el 3) pone 0 o  1 para saber si está o no está completado
        description = rows[i][2]
        l=Checkbutton(frame, text = description, width = 42, anchor='w', command = complete(id))
        l.grid(row=i, column = 0, sticky = 'w')

def addTodo():
    todo = e.get()
    if todo:
        c.execute("""
            INSERT INTO todo (description, completed) VALUES (?,?)
        """, (todo, False))
        conn.commit()
        e.delete(0,END)
        render_todos()
    else:
        pass

l = Label(root, text="Tarea")
l.grid(row=0,column=0)

e = Entry(root, width=40)
e.grid(row=0, column=1)

btn=Button(root, text="Agregar", command= addTodo)
btn.grid(row=0,column=2)

frame=LabelFrame(root, text="Mis tareas", padx=5, pady=5)
frame.grid(row=1,column=0, columnspan=3, sticky="nswe",padx=5)

e.focus()

root.bind('<Return>',lambda x : addTodo())

render_todos()

root.mainloop()
