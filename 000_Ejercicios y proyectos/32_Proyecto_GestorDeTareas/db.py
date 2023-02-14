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

def addTodo():
    todo = e.get()
    c.execute("""
        INSERT INTO todo (description, completed) VALUES (?,?)
    """, (todo, False))
    conn.commit()
    e.delete(0,END)

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

root.mainloop()