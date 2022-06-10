primero = input('Ingresar el primer numero: ')
#Validacion
try:
    primero=int(primero)
except:
    #Si no es un int, asigna a la variable 'chanchito feliz'
    primero = 'chanchito feliz'
#Esto es para cortar la ejecucion antes y no esperar al final como el 2a
if primero == 'chanchito feliz' :
    print('El primer valor no es un numero')
    exit()


segundo = input('Ingresar el segundo numero: ')
try:
    segundo=int(segundo)
except:
    segundo = 'chanchito feliz'
if segundo == 'chanchito feliz' :
    print('El segundo valor no es un numero')
    exit()

simbolo = input('Ingrese operacion: + - * /   ')

if simbolo == '+':
    print('Suma: ' , primero + segundo)
elif simbolo == '-':
    print('Resta: ' , primero - segundo)
elif simbolo == '*':
    print('Multi: ' , primero * segundo)
elif simbolo == '/':
    print('Division: ' , primero / segundo)
else:
    print('Simbolo incorrecto. Usa + - * /')