i = 0
while i < 5:
    print(i)
    i += 1  # o i=i+1
print('Valor de i fuera del bucle: ', i)
print()

i = 0
while i < 5:
    print(i)
    if i == 3:
        print('Ha hecho el break!!!')
        #El break rompe el bucle y se sale, parando la ejecucion del mismo
        break
    i += 1  # o i=i+1
print()

i = 0
while i < 5:
    i += 1 
    if i == 3:
        print('Ha hecho el continue!!!')
        #El continue hace que se vuelva a comprobar la guarda. No imprimira '3' porque
        #vuelve a la guarda y no hace el print de abajo valiendo i=3
        continue    
    print(i)
print()