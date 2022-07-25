#'create database NOMBRE' para crear una base de datos con un nombre
create database prueba;

#'drop database NOMBRE' para borrar la base de datos con dicho nombre
drop database prueba;

#'use NOMBRE' es para indicar a mysql, que base de datos estamos usando, antes de ponerse a trabajar
use prueba;

#'create table NOMBRE (nombreCampo tipo, nombreCampo2 tipo2...)' para crear una tabla
create table Usuario(id int, email varchar(255), username varchar(50));

#'drop table NOMBRE' para borrar la tabla
drop table Usuario;

#'alter table NombreTabla ACCION NOMBRE' se utiliza para modificar una tabla. Se le pueden añadir columnas, modificar columnas o borrarlas

#'alter table NombreTabla add NombreAtributo TIPO' añade una columna con X nombre de un tipo
alter table usuario add edad int;

#'alter table NombreTabla drop column NombreAtributo' borra una columna/atributo
alter table usuario drop column edad;

#'alter table NombreTabla modify column NombreAtributo nuevoTipo
	#Esta linea hace que el varchar de 255 del create table sea ahora de 50
alter table usuario modify column email varchar(50);

#Esto es para añadir registros en la tabla:
#insert into NombreTabla (nombreCampo1, nombreCampo2...)
#	values(datoCampo1, datoCampo2...)

insert into usuario (email,username)
values('andraquito@jotmail.como','andraquitoSaurio');

#Esto es para eliminar registros en la tabla:
#'delete from NombreTabla where nombreCampo = 'valor'
	#El 'limit 1' se pone porque estamos intentando eliminar algo que no tiene ID. No se le hizo set antes al añadir el registro.
    #Asi que se tiene que poner dicho 'limit 1'
    
delete from usuario where username = 'andraquitoSaurio' limit 1;
delete from usuario where username = 'pepelele' limit 1;


#Esto es para darle una id si no se le ha dado al hacer el insert arriba
alter table usuario add primary key (id);

#Lo que pasa es que la id queremos que se incremente... y se hace asi
alter table usuario modify column id int auto_increment;

insert into usuario (email,username)
values('andraquito@jotmail.como','andraquitoSaurio');

insert into usuario (email,username)
values('pepito@jotmail.como','pepelele');

insert into usuario (email,username,edad)
values('joanElDeLaBossaGran@jotmail.como','joanGran',42);


#REALIZAR CONSULTAS
#Seleccionar TODO (*) de la tabla usuario
select * from usuario;

#Seleccionar TODO (*) de la tabla usuario donde el username sea pepelele
select * from usuario where username='pepelele';

#Consultar las edades de los usuarios que tengan 36 o menos edad
select * from usuario where edad <= 36;

#UPDATE para actualizar registros
update usuario set edad = 30 where id="5";

##########################################
#Ha creado un user con la id 8 por lo autoincremental...
insert into usuario (email,username,edad)
values('joanElDeLaBossaGran@jotmail.como','joanGran',42);

#Eliminar registros
delete from usuario where id='8'

