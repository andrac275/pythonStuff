#'create database NOMBRE' para crear una base de datos con un nombre
#create database prueba;

#'drop database NOMBRE' para borrar la base de datos con dicho nombre
#drop database prueba;

#'use NOMBRE' es para indicar a mysql, que base de datos estamos usando, antes de ponerse a trabajar
use prueba;

#'create table NOMBRE (nombreCampo tipo, nombreCampo2 tipo2...)' para crear una tabla
#create table Usuario(id int, email varchar(255), username varchar(50));

#'drop table NOMBRE' para borrar la tabla
#drop table Usuario;

#######################################
#'alter table NombreTabla ACCION NOMBRE' se utiliza para modificar una tabla. Se le pueden añadir columnas, modificar columnas o borrarlas

#'alter table NombreTabla add NombreAtributo TIPO' añade una columna con X nombre de un tipo
alter table usuario add edad int;

#'alter table NombreTabla drop column NombreAtributo' borra una columna/atributo
#alter table usuario drop column edad;

#'alter table NombreTabla modify column NombreAtributo nuevoTipo
	#Esta linea hace que el varchar de 255 del create table sea ahora de 50
alter table usuario modify column email varchar(50);