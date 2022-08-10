##########################################
print('Ejer 1a. Multiplicar dos numeros sin usar el simbolo de la multiplicacion RECURSIVIDAD')

def multiplicar(num1, num2, resultado):    
    if num2 == 0:
        return 0
    elif num2 == 1:
        resultado = resultado + num1
        return resultado
    elif num2 > 1:
        resultado = resultado + num1
        return multiplicar(num1,num2 - 1, resultado)

num1= 5
num2= 6
resultado = 0
resultado = multiplicar(num1,num2,resultado)
print(num1,'x',num2,'=',resultado)

print('Ejer 1b. Multiplicar dos numeros sin usar el simbolo de la multiplicacion FOR')
num1= 5
num2= 6
resultado = 0
for x in range(num2):
    resultado += num1

print(num1,'x',num2,'=',resultado)

##########################################
print()
print('Ejer 2. Ingresar nombre y apellido e imprimirlo al reves')
nombre = 'Andrac'
apellido = 'Rawrgon'
concatenacion = nombre +' '+apellido
print(concatenacion[::-1])  #En python, poner [::-1] le da la vuelta a un string. Es interesante hacer cambions
#en ese -1 por otros valores y ver como cambian las letras que aparecen.

##########################################
print()
print('Ejer3a. Encontrar el menor número de una lista. RECURSION')
#Funcion recursiva sacar el menor de una lista
def numeroMenor(lista, numMenor):
    if len(lista) ==1:
        siguienteNumero = lista.pop(0)        
        return menorDeDos(numMenor, siguienteNumero)
    elif len(lista) > 1:
        siguienteNumero = lista.pop(0)
        numMenor = menorDeDos(numMenor, siguienteNumero)
        return numeroMenor(lista, numMenor)
#Funcion sacar el numero mas pequeño entre 2 numeros
def menorDeDos(num1, num2):
    if num1 < num2:
        return num1
    return num2

#Ejecucion del ejercicio
lista=[5,4,3,5,2,10,-24]
print('Los valores de la lista son:',lista)

if len(lista) >=1:
    numMenor=lista.pop(0)   #Obtiene primer elemento
    resultado = numeroMenor(lista,numMenor)
    print('El menor es:',resultado)
else:
    print('La lista estaba vacia')

print('Ejer3b. Encontrar el menor número de una lista. FOR')
lista=[5,4,3,5,2,10,-24]
print('Los valores de la lista son:',lista)
numMenor = 'init'
for numeroActual in lista:
    if numMenor == 'init':
        numMenor = numeroActual
    else:
        numMenor = numeroActual if numeroActual < numMenor else numMenor

print('El menor es:',numMenor)

##########################################
print()
print('Ejer4. Escribir una funcion que devuelva el volumen de una esfera por su radio')

def volumenEsfera(radio):
    return 4 / 3 * 3.14 * radio ** 3    #** es para elevar

radio = 6
print(volumenEsfera(radio))

##########################################
print()
print('Ejer5. Escribir una funcion que indique si el usuario es mayor de edad')

class Usuario:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def esMayorDeEdad(self):
        return self.edad >= 18

usuarioMayor = Usuario('Andrac' , 20)
usuarioMenor = Usuario('Niko' , 12)

print(usuarioMayor.esMayorDeEdad())
print(usuarioMenor.esMayorDeEdad())

##########################################
print()
print('Ejer6. Funcion que indique si un numero es par o impar')

def esPar(numero):
    return numero % 2==0

numPar = 4
numInpar = 3

print(numPar, 'es un numero Par???:', esPar(numPar))
print(numInpar, 'es un numero Par???:', esPar(numInpar))

##########################################
print()
print('Ejer7. Funcion que indique cuantas vocales tiene una palabra')

def cuentaVocales(palabra):
    numVocales = 0
    for letra in palabra:        
        if letra == 'a' or letra == 'A':
            numVocales +=1
        elif letra == 'e' or letra == 'E':
            numVocales +=1
        elif letra == 'i' or letra == 'I':
            numVocales +=1
        elif letra == 'o' or letra == 'O':
            numVocales +=1
        elif letra == 'u' or letra == 'U':
            numVocales +=1    
    return numVocales

#Mira esta variante de Nicolas!!!!!
def cuentaVocalesNicolas(palabra):
    numVocales = 0
    for letra in palabra:  
        letraMinus = letra.lower()  #Obliga a que sea minuscula la letra      
        numVocales += 1 if letraMinus == 'a' or letraMinus == 'e' or letraMinus == 'i' or letraMinus == 'o' or letraMinus == 'u' else 0
    return numVocales

palabra = 'Andrac'
numVocales=cuentaVocales(palabra)
numVocales2=cuentaVocalesNicolas(palabra)
print('La palabra:', palabra, 'tiene', numVocales, 'vocales')
print('La palabra:', palabra, 'tiene', numVocales2, 'vocales (variante interesante de Schurmann)')

##########################################
print()
print('Ejer8. Aplicacion que recibe una cantidad infinita de numeros hasta decir basta, luego devuelve la suma de todos los numeros')

lista=[]
print('Ingrese numeros y para salir escriba "Basta"')
while True:
    valor = input('Ingrese un valor: ')
    if valor == 'basta':
        break
    else:
        try:
            valor = int(valor)
            lista.append(valor)
        except:
            print('Dato invalido')
            exit()

sumaTodos = 0
for numero in lista:
    sumaTodos += numero

print('Has introducido:', lista,'y la suma de todos es:', sumaTodos)

##########################################
print()
print('Ejer9. Escribir funcion que reciba nombre y apellido y los agrega a un archivo')

def agregarNombreAArchivo(nombre, apellido):
    archivo = open('nombreCompleto.txt','a')
    archivo.write(nombre+' '+apellido+'\n')
    archivo.close()


agregarNombreAArchivo("Andrac","Shatrik")









