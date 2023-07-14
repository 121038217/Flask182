
from flask import Flask,render_template,request,redirect,url_for,flash
from flask_mysqldb import MySQL 
#Importamos MySQL
#request (solicitudes)
#render_template Generar la vista al momento de abrir el proyecto

#Declarando app y darle un nombre
#inicializacion del servidor Flask
app = Flask(__name__)
app.config['MYSQL_HOST']="localhost" #especificar el servidor en donde estamos trabajando
app.config['MYSQL_USER']="root" #especificar el usuario con el que vamos a trabajar
app.config['MYSQL_PASSWORD']="" #especificar contraseña
app.config['MYSQL_DB']="DB_Fruteria" #especificar a que base de datos voy a trabajar

app.secret_key = 'mysecretkey'

mysql = MySQL(app)

@app.route('/') 
def index():
    curSelect=mysql.connection.cursor()
    curSelect.execute('select * from tbFrutas')
    consulta= curSelect.fetchall()
    #print(consulta)                                 
                                      
    return render_template('index.html',listFrut=consulta)

@app.route('/guardar',methods=['POST']) 
def guardar():
    if request.method == 'POST':
        
        Vfruta= request.form['txtFruta']
        Vtemporada= request.form['txtTemporada']
        Vprecio= request.form['txtPrecio']
        vstock= request.form['txtStock']
        
        Curguar = mysql.connection.cursor() 
        #variable tipo cursor que tiene las herramientas para ejecutar las conexiones 
        Curguar.execute('insert into tbFrutas(fruta,temporada,precio,stock) values(%s,%s,%s,%s)',(Vfruta,Vtemporada,Vprecio,vstock)) 
        #en Curguar ejecutamos sql
        mysql.connection.commit()
     
    flash('Fruta Agregado Correctamente')   
    return redirect(url_for('index'))
    #guardamos al index

@app.route('/editar/<id>')
def editar(id):
    curEditar= mysql.connection.cursor() #creamos una consulta
    curEditar.execute('select * from tbFrutas where id= %s ',(id,)) #escribimos la consulta
    consulID=curEditar.fetchone() #para atraer un solo registro con fetchone
    return render_template('EditarFruta.html',fruta=consulID)

@app.route('/actualizar/<id>',methods=['POST']) 
def actualizar(id):
    if request.method == 'POST':
        
        Vfruta= request.form['txtFruta']
        Vtemporada= request.form['txtTemporada']
        Vprecio= request.form['txtPrecio']
        vstock= request.form['txtStock']

        curAct=mysql.connection.cursor()
        curAct.execute('update tbFrutas set fruta=%s, temporada=%s, precio=%s, stock=%s where id= %s',(Vfruta,Vtemporada,Vprecio,vstock,id))
        mysql.connection.commit()
        
        flash('Fruta Actualizado en BD')  #Agregamos un menaje con flash 
        return redirect(url_for('index'))

@app.route('/borrar/<id>')
def borrar(id):
    curEditar= mysql.connection.cursor() #creamos una consulta
    curEditar.execute('select * from tbFrutas where id= %s ',(id,)) #escribimos la consulta
    consulID=curEditar.fetchone() #para atraer un solo registro con fetchone
    return render_template('eliminar.html',fruta=consulID)

@app.route('/eliminar/<id>',methods=['POST']) 
def eliminar(id):
    if request.method == 'POST':

        cureli=mysql.connection.cursor()
        cureli.execute('delete from tbFrutas where id= %s',(id))
        mysql.connection.commit()
        
        flash('Fruta Actualizado en BD')  #Agregamos un menaje con flash 
        return redirect(url_for('index'))


#Linea para ejecutar el servidor
if __name__== '__main__':
    app.run(port= 3000,debug=True)