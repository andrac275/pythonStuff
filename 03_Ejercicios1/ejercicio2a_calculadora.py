primero = input('Ingresar el primer numero: ')
#Validacion
try:
    primero=int(primero)
except:
    #Si no es un int, asigna a la variable 'chanchito feliz'
    primero = 'chanchito feliz'


segundo = input('Ingresar el segundo numero: ')
try:
    segundo=int(segundo)
except:
    segundo = 'chanchito feliz'

#Si uno de los dos es chanchito feliz es que uno de los dos no es un int
if primero=='chanchito feliz' or segundo=='chanchito feliz':
    print('Ingresaste texto, prueba solo con numeros')
else:    
    print('Suma: ' , primero + segundo)
