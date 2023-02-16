from tkinter import *
from tkinter import ttk #el treeview se encuentra dentro del objeto ttk

#Treeview tiene pinta de ser para hacer tablas.

root = Tk()
root.title("Ejemplo Treeview")

tree = ttk.Treeview(root)
tree['columns']=('Nombre', 'Telefono','Empresa')
##Especificar los INDICES de las columnas
#tree.column('#0')#La primera siempre esta y por defecto es un #0. Se pone asi y ya
tree.column('#0',width=0, stretch=NO)#Esto hace lo mismo que la linea anterior pero hace desaparecer la primera columna
    #es en caso que no queramos que esté si no nos hace falta.
tree.column('Nombre')
tree.column('Telefono')
tree.column('Empresa')

#Nombres que van a tener cada una de las columnas usando el indice de arriba y despues se indica el texto
###tree.heading('indiceArribaDeArriba',text='nombreDeLaColumna')
#tree.heading('#0',text='id')#Esta es la obligatoria
tree.heading('#0')#Esta es la obligatoria
tree.heading('Nombre',text='Nombre')
tree.heading('Telefono',text='Telefono')
tree.heading('Empresa',text='Empresa')

#Agregar el widget tree a la grilla
tree.grid(column=0, row=0)

#(padre,posicion,identificador,valores,textoDentroColumnaID)
tree.insert('',END, 'lala',values=('Uno','Dos','Tres'),text='Chanchito feliz')
tree.insert('',END, 'lele',values=('Cuatro','Cinco','Seis'),text='Chanchito triste')
tree.insert('lele',END, 'lili',values=('4','5','6'),text='Hijo')
    #No se ve bien pero al ejecutar el script, si le damos a la 'C' de Cuatro, despliega esta lista hija con 4,5,6

root.mainloop()
