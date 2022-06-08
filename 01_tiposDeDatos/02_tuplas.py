#Parecido a las listas, pero en lugar de [] se usan parentesis.
#Las tuplas no se pueden modificar... Aqui se enseñan algunos metodos de estas
#Como no se pueden modificar, no tienen el append que tenian las listas

tupla = ('hola' , 'mundo' ,'somos' , 'tupla', 'hola')
print(tupla)

#count
print("Count de hola: ", tupla.count('hola'))

#index
print('index de elemento somos: ', tupla.index('somos'))

#Acceder elemento concreto
print('Acceder elemento 3: ', tupla[3])

#Tuplas son inmodificables, no tienen append... pero se pueden transformar
#en una lista y despues modificarlas.
#tupla.append('asdfasdf')   #Esta linea peta

listaDeTupla = list(tupla)
print("Ya no es una tupla! Es una lista: " ,listaDeTupla)
listaDeTupla.append('asdfasdf')
print(listaDeTupla)