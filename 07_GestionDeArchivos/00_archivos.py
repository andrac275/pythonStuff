archivo = open('archivoAleer.txt')    #open es para escoger un archivo para abrirlo.
#archivoLectura = open('archivoAleer.txt','r')  #'r' es read, y viene por defecto, como arriba
#archivoAppend = open('archivoAleer.txt','a')    #'a' es append, sirve para modificar y añadir cosas, por ejemplo al final
#archivoWrite = open('archivoAleer.txt','w') #'w' es write, es para modificar todo. Si no existe, lo crea.
#archivoCrear = open('lalalala.txt','x') #'x' es para crear un archivo si no está creado. Si ya lo está da error.
print('READ---------------------')
print(archivo.read())   #read para leer TODO el contenido
archivo.close()

print('READLINE---------------------')
archivo = open('archivoAleer.txt') 
print(archivo.readline())
archivo.close()

print('BUCLE FOR---------------------')
archivo = open('archivoAleer.txt') 
for linea in archivo:
    print(linea)
archivo.close()

