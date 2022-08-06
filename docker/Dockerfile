# Seleccionar de que imagen partimos... puede ser la latest 'node' o una en concreto: 'node:18'
FROM node:18

#Que cree una carpeta en la maquina del contenedor para guardar ahi nuestra app...
RUN mkdir -p /home/app

#Todo lo que hay en la carpeta donde esta el dockerfile, lo copia dentro del contenedor /home/app
COPY . /home/app

#Exponer puerto para que se puedan connectar des de fuera.
EXPOSE 3000

#Ejecutar un comando mas argumentos al arrancar el container...
    #Al hacer el copy, se ha puesto en HomeApp el index.js
CMD ["node" , "/home/app/index.js"]