from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3

root = Tk()
root.title('CRM: Libreta de clientes')

conn = sqlite3.connect('crm.db')

c=conn.cursor()

c.execute("""
        CREATE TABLE if not exists cliente(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            telefono TEXT NOT NULL,
            empresa TEXT NOT NULL
        );
""")

def insertar(cliente):
    print(cliente)

def nuevo_cliente():
    def guardar():
        if not nombre.get():
            messagebox.showerror('Error','El nombre es obligatorio')
            return
        if not telefono.get():
            messagebox.showerror('Error','El telefono es obligatorio')
            return
        if not empresa.get():
            messagebox.showerror('Error','La empresa es obligatoria')
            return        

        cliente = {
            'nombre' :nombre.get(),
            'telefono' :telefono.get(),
            'empresa' :empresa.get()
        }
        insertar(cliente)
        top.destroy()
        


    top = Toplevel()
    top.title('Nuevo cliente')

    lnombre=Label(top,text="Nombre")
    nombre = Entry(top,width=40)
    lnombre.grid(row=0,column=0)
    nombre.grid(row=0,column=1)

    ltelefono=Label(top,text="Telefono")
    telefono = Entry(top,width=40)
    ltelefono.grid(row=1,column=0)
    telefono.grid(row=1,column=1)

    lempresa=Label(top,text="Empresa")
    empresa = Entry(top,width=40)
    lempresa.grid(row=2,column=0)
    empresa.grid(row=2,column=1)

    btn_guardar=Button(top,text='Guardar',command=guardar)
    btn_guardar.grid(row=3,column=1)

    top.mainloop()

def eliminar_cliente():
    pass

btn = Button(root, text='Nuevo Cliente', command=nuevo_cliente)
btn.grid(column=0,row=0)

btn_eliminar= Button(root, text="Eliminar Cliente", command=eliminar_cliente)
btn_eliminar.grid(column=1, row= 0)

tree = ttk.Treeview(root)
tree['columns'] =('Nombre','Telefono','Empresa')
tree.column('#0',width=0,stretch=NO)
tree.column('Nombre')
tree.column('Telefono')
tree.column('Empresa')

tree.heading('Nombre',text='Nombre')
tree.heading('Telefono',text='Telefono')
tree.heading('Empresa',text='Empresa')
tree.grid(column=0,row=1,columnspan=2)

root.mainloop()