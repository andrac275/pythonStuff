archivo = open('archivoEscribir.txt','a')   #'a' añade al final. Esto se puede usar para añadir registros.
archivo = open('archivoEscribir.txt','w')   #'w' borra todo el fichero. Habria que rellenar todo.

archivo.write('\nEsto es una linea escrita... con el write')

archivo.close()