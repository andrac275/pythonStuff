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