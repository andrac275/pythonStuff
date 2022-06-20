#LEEME ANDREU: https://pypi.org/
#Es una pagina web de modulos creados por la comunidad (a lo marketplace), tiene un buscador para encontrar modulos de python
#Para este tutorial se va a utilizar el 'Camelcase 0.2' que si se busca en la pagina aparece 'pip install camelcase'
#Esto se copia en la consola y se instala este paquete en concreto.

#Mencionar que pip, que es lo que se usa para instalar paquetes externos, tiene una barbaridad enorme de paquetes...
#Asi que lo mejor es usar la pagina de arriba: https://pypi.org/

#El modulo camelcase bajado de la pagina con el pip, lo que hace es poner la primera letra de cada
#palabra en mayuscula. Mira el print y lo entenderas...

#Esto es un ejemplo simple para aprender que la pagina pypi tiene muchos modulos, como se instalan y
# que leyendo la documentacion de la pagina donde lo descargas, puedes ver como usar el modulo tambien.
from camelcase import CamelCase

c = CamelCase()
s = 'esta oracion necesita camelCase!'

camelcased = c.hump(s)

print(camelcased)

#VER MODULOS INSTALADOS
#Escribir en la consola
    #pip list

#BORRAR MODULOS INSTALADOS
#Una vez sabemos qué tenemos instalado con el comando anterior, se puede borrar un modulo con su nombre
#Ejemplo
    #pip uninstall camelcase