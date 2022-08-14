from flask import Flask, request
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

#################################################################

#Las variables sirven para pasar informacion a python a traves de la url. Esto se llamaria con:
#P Ej: http://127.0.0.1:5000/post/50 y le estamos pasando un 50
#Si ponemos @app.route('/post/<int:post_id>') obligariamos a que post_id sea un entero, y diria que no puede concatenar
#string con int, pero bueno, es para saber que se puede obligar a que se pase valores en concreto.
@app.route('/post/<post_id>')
def post(post_id):
    return 'El id del post es: ' + post_id 

###############################################################
#Metodos http web: GET POST PUT DELETE
    #GET: listar
    #POST: Crear
    #PUT: Actualizar
    #PATCH: Similar a PUT, pero solo actualiza mientras que PUT reemplaza.
    #DELETE: Borrar
#Lo siguiente solo permite GET o POST. Se pueden probar escribiendo en consola:
    #Este falla porque no se permite el PUT como methods...
        #curl -X PUT http://localhost:5000/postMethods/1
    #Este funciona porque si se permite el GET:
        #curl -X GET http://localhost:5000/postMethods/1
@app.route('/postMethods/<post_id>' , methods=['GET','POST'])
def postMethods(post_id):
    if request.method == "GET":
        return 'El id del post del metodo GET es: ' + post_id
    elif request.method == "POST":
        return 'Este es el metodo POST'

###########################################################
 #Se pueden hacer llamadas con curl.
    #-d para darle datos, sea un JSON o datos manuales
    #-X para indicar el metodo: GET POST...
    #la url sobre la que se realiza
    #Ej: curl -d "llave1=dato1&llave2=dato2" -X POST http://localhost:5000/lele


@app.route('/lele', methods=['POST'])
    #http://127.0.0.1:5000/lele
def lele():
    print(request.form)
    print(request.form['llave1'])
    print(request.form['llave2'])
    return 'lele'