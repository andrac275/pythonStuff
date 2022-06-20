#Crear una clase
class Usuario:
    #El init es para cuando no damos valores por defecto, sino que se pasaran despues
    #al instanciar los objetos

    #El def _init_ es algo que SIEMPRE se ejecuta al crear un objeto de la clase Usuari
    #El self es opcional, pero nombre y apellido, si hay que ponerlo en __init__(self, nombre, apellido):
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
    
    #Metodos
    def mostrarNombreCompleto(self):
        return self.nombre + self.apellido
    
    def saludo(self):
        print('Te saludo! Mi nombre es: ' + self.nombre)

#Al generar el objeto, se pasan esos dos argumentos
usuario = Usuario('Andrac' , 'Rawrgon')
print(usuario.nombre, usuario.apellido)

usuario2 = Usuario('Escalope' , 'RadaRada')
print(usuario2.nombre, usuario2.apellido)

print('Hola, mi nombre es: ' + usuario.mostrarNombreCompleto())
usuario.saludo()

##BORRAR PROPIEDADES U OBJETOS!!!!
del usuario.nombre
#Descomementar la siguiente linea da error porque ya no existe nombre
#print(usuario.nombre)

del usuario
#Descomentar la siguiente linea da error porque usuario no existe ya
#print(usuario)