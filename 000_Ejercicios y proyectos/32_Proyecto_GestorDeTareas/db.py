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
        id INTEGER PRIMARY KEY AUTO_INCREMENT,
        created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        description TEXT NOT NULL,
        completed BOOLEAN NOT NULL
    )
""")
conn.commit()


