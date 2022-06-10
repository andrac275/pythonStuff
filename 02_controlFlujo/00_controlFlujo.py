#Combinaciones:
#a==b, a!=b, a<b, a>b, a<=b, a>=b

#Punto 1: if
print('Punto 1: if')
if (2<5):
    print('2 menor que 5')

if 2<=5:
    print('2 menor igual que 5')

if 2!=5:
    print('2 distinto de 5')

if 3>3:
    print('3 no es mayor estricto que 3, asi que no se imprime')

if 3>=3:
    print('3 es mayor o igual que 3')




#Punto 2: if..elif..else
print('\n Punto 2: if..elif..else')
if 2 > 5:
    print ('2 menor que 5 en if')
elif 2 == 5:
    print('2 menor que 5 en elif')
elif 2 < 5:
    print('2 menor que 5 en el SEGUNDO elif')
else:
    print('Yo me imprimo solo si todo lo anterior es falso')

if 2 > 5:
    print ('2 menor que 5 en if')
else:
    print('Yo me imprimo solo si todo lo anterior es falso de ABAJO')



##Punto 3: if cortos y ternarios
print('\n Punto 3: if cortos y ternarios')
if 2 < 5 : print('If de una sola linea')

#Evaluacion ternaria
print('\nEvaluacion ternaria (mira el codigo):')
print('La evaluacion es TRUE') if 5<2 else print('La evaluacion es FALSE')
print('La evaluacion es TRUE') if 5>2 else print('La evaluacion es FALSE')

#Punto4: And y Or
print('\n Punto4: And y Or')
if 2<5 and 3>4 :
    print('AMBAS devuelven true')
else:
    print('Una de las dos es falsa')

if 2<5 or 3>4 :
    print('ALMENOS una condicion devuelve true')
else:
    print('Las DOS son falsas')