import os

from flask import Flask

#A la hora de crear una aplicacion con Flask, este necesita una funcion create_app
def create_app():
    app = Flask(__name__)

    app.config.from_mapping(
        #SecretKey lo usa Flask para generar cookies que pasa a los users y poder identificarlos. Por ahora pasamos 'mikey', pero en produciion
        #deberia ser un string mas complicado, ya que se usa como hash este string para generar las cookies.
        SECRET_KEY= 'mikey',
        DATABASE_HOST= os.environ.get('FLASK_DATABASE_HOST'),
        DATABASE_PASSWORD= os.environ.get('FLASK_DATABASE_PASSWORD'),
        DATABASE_USER= os.environ.get('FLASK_DATABASE_USER'),
        DATABASE= os.environ.get('FLASK_DATABASE'),
    )

    @app.route('/hola')
    def hola():
        return 'Chanchito feliz'
    
    return app