#'create database NOMBRE' para crear una base de datos con un nombre
#create database prueba;

#'drop database NOMBRE' para borrar la base de datos con dicho nombre
#drop database prueba;

#'use NOMBRE' es para indicar a mysql, que base de datos estamos usando, antes de ponerse a trabajar
use prueba;

#'create table NOMBRE (nombreCampo tipo, nombreCampo2 tipo2...)' para crear una tabla
create table Usuario(id int, email varchar(255), username varchar(50));

#'drop table NOMBRE' para borrar la tabla
#drop table Usuario;


