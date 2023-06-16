
from flask import Flask

#Declarando app y darle un nombre
#inicializacion del servidor Flask
app = Flask(__name__)
app.config['MYSQL_HOST']="localhost" #especificar el servidor en donde estamos trabajando
app.config['MYSQL_HOST']="root" #especificar el usuario con el que vamos a trabajar
app.config['MYSQL_HOST']="" #especificar contraseña
app.config['MYSQL_HOST']="dbflask" #especificar a que base de datos voy a trabajar

#Declaracion de rutas

#ruta Index o ruta principal (http:://localhost:5000)
#La ruta se compone de nombre de la ruta y la funcion que va a ejecutar
@app.route('/') 
def index():
    return "Hola Mundo"

@app.route('/guardar') 
def guardar():
    return "Se guardo el album en la BD"

@app.route('/eliminar') 
def eliminar():
    return "Se elimino el album en la BD"



#Linea para ejecutar el servidor
if __name__== '__main__':
    app.run(port= 5000,debug=True) #port: Es el puerto del servidor entre 5000 y 8000
    #debug=true es para no estar abriendo el servidor seguido y ver los cambios en automatico
    