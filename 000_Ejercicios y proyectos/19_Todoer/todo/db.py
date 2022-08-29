import mysql.connector

import click    #CLICK es para poder ejecutar des de consola comandos mysql, en lugar de tener que entrar a mysql workbench

#current_app es la app actual de flask
#g es una variable donde estan las variables de nuestra app, a g se le pueden asignar variables
from flask import current_app, g
#with_appcontext es para obtener el contexto y poder llamar el script como por ejemplo el host, el username y la password
from flask.cli import with_appcontext
#schema es un archivo con scripts para crear y configuarar la DB
from .schema import instructions

def get_db():
    if 'db' not in g:
        g.db = mysql.connector.connect(
            host = current_app.config['DATABASE_HOST'],
            user = current_app.config['DATABASE_USER'],
            password = current_app.config['DATABASE_PASSWORD'],
            database = current_app.config['DATABASE']
        )
        g.c = g.db.cursor(dictionary=True)
    return g.db, g.c

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_app(app):
    app.teardown_appcontext(close_db)
    