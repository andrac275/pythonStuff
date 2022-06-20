class Animal:
    def __init__(self,nombre,onomatopeya):
        self.nombre=nombre
        self.onomatopeya = onomatopeya

    def saludo(self):
        #El self.tipo es de las clase hijo, pero cuando se generan las instancias hijo, tienen tipo.
        print('Hola, soy un', self.tipo, 'y mi onomatopeya es el',self.onomatopeya)


#Para extender se utiliza el __init__ en la clase hijo PERO usar init hace que se ignore el init de la 
#clase padre, por tanto, a parte de hacer el init, hay que pasar los atributos... y eso se puede hacer de 
#3 maneras. La clase Gato extiende con Animal.__init__ , la clase Perro con la palabra super

class Gato(Animal):  
    tipo = 'gato'  
    def __init__(self,nombre,onomatopeya):
        #Si se pasa la clase padre, hay que pasar el self.
        Animal.__init__(self,nombre,onomatopeya)


class Perro(Animal):
    tipo = 'perro'
    def __init__(self,nombre,onomatopeya):
        #Si se utiliza el super, no es necesario pasar el self.
        super().__init__(nombre, onomatopeya)

class Canario(Animal):
    tipo = 'canario'
    
#############################
gato =Gato('Fluffy', 'maullido')
gato.saludo()

perro = Perro('Firulais', 'ladrido')
perro.saludo()

bird = Canario('Perles', 'chirpchirp')
bird.saludo()