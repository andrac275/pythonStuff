#Diccionarios se crean con {} y permiten acceder a elementos del mismo con los 
#strings de los atributos

#gato es un diccionario...
gato = {
    "Nombre" : "Dollie",
    "Raza" : "Tricolor",
    "Edad" : 5
}

print("Imprimir diccionario: \n" ,gato)

print("Acceder con cajitas a los atributos: \n" , gato["Nombre"] , gato["Raza"] , gato["Edad"])

print("Acceder con get a los atributos: \n", gato.get("Nombre"),gato.get("Raza"),gato.get("Edad"))

#Cambiar valor de elemento del diccionario
gato["Nombre"] = 'Bella'
print('Nuevo nombre de gato: ' , gato)

#Tamaño del diccionario
#Devuelve 3 porque tiene tres elementos: Nombre, Raza, Edad
print(len(gato))

#AÑADIR ELEMENTOS AL DICCIONARIO
#Parecido al modificar pero poniendo un atributo nuevo
gato["Ronronea"] = 'Si'
print('Añadir nuevo elemento:' , gato)

#ELIMINAR ELEMENTO DEL DICCIONARIO
#Con el pop
gato.pop("Ronronea")
print('Eliminar elemento con pop:' ,gato)

#Con el popitem que borra lo ultimo añadido.
gato["Ronronea"] = 'Si'
print(gato)
gato.popitem()
print('Eliminar elemento con popitem:' ,gato)

#Con el 'del'
gato["Ronronea"] = 'Si'
print(gato)
del gato["Ronronea"]
print('Eliminar elemento con del:' ,gato)

#COPIAR DICCIONARIO
gatoCopia=gato.copy()   #Metodo 1
gatoCopia2=dict(gato)   #Metodo 2

#Borrarlo todo
gato.clear()
print('Borrar todo con clear: ' , gato)
print('Gato copiado (antes de borrarlo)' , gatoCopia)
print('Gato copiado con dict(antes de borrarlo)' , gatoCopia2)