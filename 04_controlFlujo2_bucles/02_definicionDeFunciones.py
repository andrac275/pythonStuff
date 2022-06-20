def miFuncion():
    print("Esto es mi primera funcion")

def imprimeDato(dato1):
    print("Mi argumento es:" , dato1)

def nombreCompleto(nombre, apellido):
    print("El nombre completo es: \n"
        "Nombre: " + nombre + " Apellido: " + apellido)

def listaVariable(*nombre):
    print('Esto es una lista de tamaño VARIABLE con el asterisco *: ')
    print('Todos los argumentos, esto es una tupla: ' ,nombre)
    print('Solo el de posicion 1: ', nombre[1])

    print()
    #Se pueden iterar con el for la lista de nombre
    print('Iteracion con el bucle for:')
    for argumento in nombre:
        print('Bucle for: ' ,argumento)

#Si no recordamos los argumentos en que orden iban... Se pueden asignar.
#Aqui debia ser apellido, nombre (segun la definicion de la funcion), pero lo hemos hecho nombre, apellido
def nombreArgumentosOrdenDistinto(apellido, nombre):
    print(nombre, apellido)

#Pasar diccionarios a una funcion. Doble asterisco
    #Se llama kwwargs (keywordargs) por convenio pero llamarlo **asdf y despues  asdf['nombre'],asdf['apellido'],asdf['edad']
    #Funciona igual.
def funcionConDiccionario(**kwargs):
    print(kwargs['nombre'],kwargs['apellido'],kwargs['edad'])

#Llamadas de las funciones anteriores
miFuncion()
miFuncion()
miFuncion()

print()
imprimeDato("Andreu")
imprimeDato(31)

print()
nombreCompleto('Andrac', 'Shatrik')

print()
listaVariable('Andrac' , 'Azeriak' , 'Droteriono')

#Si no recordamos los argumentos en que orden iban... Se pueden asignar.
#Aqui debia ser apellido, nombre (segun la definicion de la funcion), pero lo hemos hecho nombre, apellido
print()
print('Orden argumentos distintos: ')
nombreArgumentosOrdenDistinto(nombre='andrac', apellido='rawrgon')

print()
print('Funcion con diccionarios y argumentos: ')
funcionConDiccionario(nombre='andrac', edad = 31, apellido='RAWRgón')

###############################################
print()
#Argumentos por defecto
def funcionArgumPorDefecto(nombre = 'Joan', apellido = 'Pegolino'):
    print('Mi nombre es: ', nombre, apellido)

print('Funcion argumento por defecto:')
#Joan es el argumento por defecto... Y sabes por qué
funcionArgumPorDefecto()    
funcionArgumPorDefecto('Andrac')
funcionArgumPorDefecto('','Rawrgon')
funcionArgumPorDefecto('Andrac','Rawrgon')

print()
print('Funcion pasando una lista:')
#Pasar lista como parametro
def funcionListaComoArgumento(lista):
    for elemento in lista:
        print(elemento)

funcionListaComoArgumento(['elem1','elem2','elem3'])

###############################################
print()
def concatenaNombres(listaNombres):
    resultado = ''
    for nombre in listaNombres:
        resultado = resultado + ' ' + nombre
    return resultado

print('Funcion concatenar nombres')
nombres = concatenaNombres(['Andrac','Chanchito','Feliz'])
print(nombres)