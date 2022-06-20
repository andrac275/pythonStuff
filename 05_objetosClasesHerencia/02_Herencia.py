class Usuario:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
    
    def saludo(self):
        print('Hola! Mi nombre es:', self.nombre ,'', self.apellido)

#HERENCIA
#Para heredar, se pasa entre parentesis el nombre de la clase padre
class Administrador(Usuario):
    
    def __init__(self,nombre, apellido,edad):
        #Mirar '04_ExtenderConstructorPadre.py' para mas detalles
        ##Alternativa 1:
        #Usuario.__init__(self,nombre,apellido)
        ##Alternativa 2:
        super().__init__(nombre,apellido)
        self.edad = edad

    def superSaludo(self):
        print('Hola, me llamo:' , self.nombre, 'y soy administrador con',self.edad,'anyos')


usuario = Usuario('Andrac','Rawrgon')
usuario.saludo()
admin = Administrador('MrRobot', 'TheAdministrator', 25)
admin.saludo()
admin.superSaludo()

#La siguiente linea da error porque USUARIO no tiene un metodo superSaludo, eso es de ADMINISTRADOR
#usuario.superSaludo()