#Crear una clase

class Usuario:
    nombre = 'Andrac'
    apellido = 'Rawrgon'

usuario = Usuario()

print(usuario)
print(usuario.nombre)
print(usuario.nombre, usuario.apellido)

print('Cambio de atributo:')
usuario.nombre= 'Chanchito'
usuario.apellido = 'Infeliz'
print(usuario.nombre, usuario.apellido)