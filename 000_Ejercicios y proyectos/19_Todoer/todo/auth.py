import functools

#Blueprint: Permite crear blueprints para despues poder configurarlos, es una manera de hacer login.
#flash: permite enviar mensajes genericos a las plantillas, por ejemplo si te equivocas al hacer login.
#g: es una variable que deja disponibles distintas variables a utilizar
#render_template: para renderizar plantillas
#request: para recibir datos de un formulario
#url_for: para crear urls
#session: tener una referencia del usuario en el contexto actual de la DB
from flask import(
    Blueprint, flash, g, render_template, request, url_for,session
)

#checkPasswordHash comprueba si dos contraseñas son iguales
#generatePasswordHash para encriptar la contraseña que se envia
from werkzeug.security import check_password_hash, generate_password_hash

#get_db para poder interactuar con la base de datos
from todo.db import get_db

bp = Blueprint('auth',__name__,url_prefix='/auth')

@bp.route('/register', methods = ['GET','POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db,c = get_db()
        error = None
        c.execute(
            'select id from user where username = %s'
        )

        if not username:
            error = 'Username es requerido'
        if not password:
            error = 'Password es requerido'
        elif c.fetchone() is not None:
            error = 'Usuario {} se enceuntra registrado.' .format(username)
        
        if error is None:
            c.execute(
                'insert into user (username,password) values (%s,%s)'
                (username, generate_password_hash(password))
            )
            db.commit()

            return redirect(url_for('auth.login'))

        #Muestra el error si no se ha entrado por el return anterior
        flash(error)
    #Este return por si el usuario esta haciendo un GET en lugar de un POST
    return render_template('auth/register.html')