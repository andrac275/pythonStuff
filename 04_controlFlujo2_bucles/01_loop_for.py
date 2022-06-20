usuarios = ['andrac', 'azeriak', 'hunky' , 'muzzlecito']
edades = [24,25,26,35]

for usuario in usuarios:
    print(usuario)

usuario = 'andrac'
for letra in usuario:
    print(letra)

for usuario in usuarios:
    if(usuario == 'hunky'):
        print('He encontrado a hunky y me salgo ya del loop')
        break
    print("No lo he encontrado aun... Me he encontrado con: ", usuario)

print("Funcion de range... Que se dijo que seria util para iterar")
for x in range(3):
    print(x)

print("Funcion range acotada")
for x in range(10,15):
    print(x)

print("Funcion range acotada... Aumentando de 5 en 5")
for x in range(3,30,5):
    print(x)
else:
    print("Hemos terminado!")

for usuario in usuarios:
    for edad in edades:
        print(usuario, edad)