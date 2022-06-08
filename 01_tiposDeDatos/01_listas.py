#Listas (o arrays)
lista = [1,2,3]
#append es para añadir elementos a la lista
lista.append(4)
print(lista)

#clear limpia la lista
lista.clear()
print(lista)

lista = [1,2,3]
#copiar lista
lista2 = lista.copy()
lista.append(4)
print(lista, lista2)

#contar los veces que aparece un elemento: count
contar=[1,2,2,3,3,3]
#hay un 1, hay 2 doses, hay 3 treses y hay 0 cuatros. Eso devolverá el count.
print(contar.count(1), contar.count(2), contar.count(3),contar.count(4))

#Tamaño de una lista: len
print(lista, len(lista)) #Devuelve 4 porque lista tiene 4 elementos

#Acceder elementos en concreto. Usando el indice
listaPalabras = ["Hola", "Mundo","Dodogama puto amo","Nergigante huehuehue"]
print(listaPalabras[0])
print(listaPalabras[1])
print(listaPalabras[2])
print(listaPalabras[3])


#ELIMINAR ELEMENTOS DE UNA LISTA
print("Contenido de la lista: " , listaPalabras)
listaPalabras.pop() #Elimina el ultimo elemento de la lista
print(listaPalabras)
listaPalabras.remove("Hola")    #Elimina ese elemento en concreto
print(listaPalabras)
listaPalabras.remove(listaPalabras[0])  #Elimina elemento en la posicion 0
print(listaPalabras)

#Invertir y ordenar listas
listaOrdenar=["Bad" , "Case" , "Of" ,"Erriba" , "Aspaña"]
print("Una lista normal: ",listaOrdenar)
listaOrdenar.reverse()
print("Reverse de la lista: " ,listaOrdenar)
listaOrdenar.sort()
print("Sort de la lista anterior:" ,listaOrdenar)
print("ADVERTENCIA!!!: No ordenar listas con tipos datos distintos")
listaIncorrectaSort=["Hola", 2 , 3 , "Mundo"]
print(listaIncorrectaSort.sort())