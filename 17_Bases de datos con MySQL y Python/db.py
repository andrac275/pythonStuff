from unittest import result
import mysql.connector

midb  = mysql.connector.connect(
    host="localhost",
    user="Andrac",
    password= "asdfasdfasdf", #La password
    database = "prueba"
)

#Un cursor es un objeto que permite interactuar con la base de datos
 #mediante el lenguaje mysql

cursor = midb.cursor()

#Execute es para hacer una consulta con el cursor en la base de datos

#cursor.execute('select * from Usuario')

#Fetchall es para recoger TODOS los resultados de la consulta... que lo hemos guardado en la variabel resultado

# resultado = cursor.fetchall()
# print(resultado)

#Fetchone devuelve solo un resultado. El primero que encuentre. Si hay mas cosas, solo devolverá una. Aqui devolveria solo un usuario
    #aunque en la BD haya mas de uno.

# resultadoUnico = cursor.fetchone()
# print(resultadoUnico)

#############################################

#Para INSERTAR DATOS en la base de datos...
#1.Ver definiciones de tablas: Como alomejor no sabemos como se crea algo, se puede usar la siguiente opcion para que la consola muestre lo que hace falta

# cursor.execute('show create table Usuario')
# resultado = cursor.fetchall()
# print(resultado)
    #Ahora ya sabemos que hace falta un email, un username y la edad asi que lo creamos en el punto 2.

#2.Guardar en una variable la consulta

# sql = 'insert into Usuario (email,username,edad) values(%s,%s,%s)'
# values=('micorreo@gmail.com','userPython',45)

#3.Con la consulta y los datos, se crea la consulta a ejecutar
# cursor.execute(sql, values)

#4. Se hace commit en la DB para que se guarde el usuario creado
# midb.commit()

# print(cursor.rowcount)

#Listar datos
# cursor.execute('select * from Usuario')
# resultado = cursor.fetchall()
# print(resultado)

###############################################

#Para ACTUALIZAR DATOS en la BD...

# sql = ('update Usuario set email= %s where id = %s')
# values=('asdas@asdas.com', 10)
# cursor.execute(sql, values)
# midb.commit()

#Listar datos
# cursor.execute('select * from Usuario')
# resultado = cursor.fetchall()
# print(resultado)

###############################################

#Para ELIMINAR DATOS en la BD...

# sql = ('delete from Usuario where id = %s')
# #IMPORTANTE!: Si solo pasamos un unico valor al 'sql' de arriba, se tiene que dejar como
#     #'values=(10,)' porque si ponemos 'values=(10)' sin la coma, da error. Es una TUPLA
#     #asi que requiere de dos valores y se hace asi si o si.
# values=(9,)
# cursor.execute(sql, values)
# midb.commit()

#Listar datos
# cursor.execute('select * from Usuario')
# resultado = cursor.fetchall()
# print(resultado)

###############################################

#Para LIMITAR al listar  DATOS en la BD, se usa limit...
    #'select * from Usuario limit NUMEROELEMENTOS'
    #NUMEROELEMENTOS: numero de elementos que queremos listar, para no listarlo todo.
        #Si se deja a 1, muestra 1; si se pone 2, muestra 2, etc

#Listar datos
cursor.execute('select * from Usuario limit 2')
resultado = cursor.fetchall()
print(resultado)