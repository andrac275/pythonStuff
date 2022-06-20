class Animal:
    def __init__(self,nombre,onomatopeya):
        self.nombre=nombre
        self.onomatopeya = onomatopeya

    def saludo(self):
        #El self.tipo es de las clase hijo, pero cuando se generan las instancias hijo, tienen tipo.
        print('Hola, soy un', self.tipo, 'y mi onomatopeya es el',self.onomatopeya)


class Gato(Animal):  
    tipo = 'gato'     

class Perro(Animal):
    tipo = 'perro'

class Canario(Animal):
    tipo = 'canario'
    
gato =Gato('Fluffy', 'maullido')
gato.saludo()

perro = Perro('Firulais', 'ladrido')
perro.saludo()

bird = Canario('Perles', 'chirpchirp')
bird.saludo()