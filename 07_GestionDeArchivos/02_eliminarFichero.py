#Para ELIMINAR FICHEROSs hace falta una libreria... os.

import os
#Comprobar, antes de borrar, si existe para que no de errores
nombreFichero= 'lalalala.txt'

if os.path.exists(nombreFichero):
    os.remove(nombreFichero)
else:
    print('El archivo',nombreFichero,'no existe')

#Para ELIMINAR CARPETAS, con rmdir
nombreCarpeta='carpetaBorrar'
if os.path.exists(nombreCarpeta):
    os.rmdir(nombreCarpeta)
else:
    print('La carpeta',nombreCarpeta,'no existe')