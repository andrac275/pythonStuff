import modulos as mdl  #El fichero que esta en esta carpeta se llama modulos.py, por eso se importa 
# con el nombre 'modulos' (por el nombre del fichero)
#dicho archivo tiene una lista de mascotas y un metodo de saludo

#El 'modulos as mdl' se utiliza para RENOMBRAR. Asi en lugar de tener que escribir modulos.saludo('Andrac')
#basta con mdl.saludo('Andrac')

#IMPORTAR SOLO UNA PARTE
from modulos import saludo     #Esta linea solo importa el saludo, no todo el modulo.

#IMPORTAR VARIAS COSAS (pero NO todo)
from modulos import saludo, mascotas     #Esta linea importa el saludo y la lista de mascotas

print(mdl.mascotas)

mdl.saludo('Andrac')