from flask import Flask
#el valor de __name__ lo que hace es poner el nombre del archivo cuando lo ejecutamos
    #en este caso holamundo.py
app = Flask(__name__)

#Usar decoradores con la arroba...
    #El codigo que hay después se va a ejecutar cuando llamemos a la raiz /, segun este ejemplo.
    #La raiz es: http://127.0.0.1:5000
@app.route('/')
#Una funcion que retorna holamundo, sin mas.
def index():
    return 'hola mundo'

#Vamos a poner otra carpeta...
@app.route('/lala')
    #http://127.0.0.1:5000/lala
def lala():
    return 'lala'

#Las variables sirven para pasar informacion a python a traves de la url. Esto se llamaria con:
#P Ej: http://127.0.0.1:5000/post/50 y le estamos pasando un 50
#Si ponemos @app.route('/post/<int:post_id>') obligariamos a que post_id sea un entero, y diria que no puede concatenar
#string con int, pero bueno, es para saber que se puede obligar a que se pase valores en concreto.
@app.route('/post/<post_id>')
def post(post_id):
    return 'El id del post es: ' + post_id 
