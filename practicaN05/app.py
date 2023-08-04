
from flask import Flask,render_template,request,redirect,url_for,flash
from flask_mysqldb import MySQL 
from flask import Response
from io import BytesIO
from reportlab.pdfgen import canvas 
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Image

#Importamos MySQL
#request (solicitudes)
#render_template Generar la vista al momento de abrir el proyecto

#Declarando app y darle un nombre
#inicializacion del servidor Flask
app = Flask(__name__)
app.config['MYSQL_HOST']="localhost" #especificar el servidor en donde estamos trabajando
app.config['MYSQL_USER']="root" #especificar el usuario con el que vamos a trabajar
app.config['MYSQL_PASSWORD']="" #especificar contraseña
app.config['MYSQL_DB']="dbflask" #especificar a que base de datos voy a trabajar

app.secret_key = 'mysecretkey' #Agregamos un token

mysql = MySQL(app)

#Declaracion de rutas

#ruta Index o ruta principal (http:://localhost:5000)
#La ruta se compone de nombre de la ruta y la funcion que va a ejecutar
@app.route('/') 
def index():
    curSelect=mysql.connection.cursor()
    curSelect.execute('select * from new_table')
    consulta= curSelect.fetchall()
    #print(consulta)                                 
                                      
    return render_template('index.html',listAlbums=consulta)

@app.route('/guardar',methods=['POST']) 
def guardar():
    if request.method == 'POST':
        
        Vtitulo= request.form['txtTitulo']
        Vartista= request.form['txtArtista']
        Vanio= request.form['txtAnio']
        #print(titulo,artista,anio)
        
        CS = mysql.connection.cursor() 
        #variable tipo cursor que tiene las herramientas para ejecutar las conceciones
        CS.execute('insert into new_table(titulo,artista,anio) values(%s,%s,%s)',(Vtitulo,Vartista,Vanio)) #en CS ejecutamos sql
        mysql.connection.commit()
     
    flash('album Agregado Correctamente')   
    return redirect(url_for('index'))
    #guardamos al index
    
@app.route('/editar/<id>')
def editar(id):
    curEditar= mysql.connection.cursor() #creamos una consulta
    curEditar.execute('select * from new_table where id= %s ',(id,)) #escribimos la consulta
    consulID=curEditar.fetchone() #para atraer un solo registro con fetchone
    return render_template('editarAlbum.html',album=consulID)

@app.route('/actualizar/<id>',methods=['POST']) 
def actualizar(id):
    if request.method == 'POST':
        
        Vtitulo= request.form['txtTitulo']
        Vartista= request.form['txtArtista']
        Vanio= request.form['txtAnio']
        #print(titulo,artista,anio)

        curAct=mysql.connection.cursor()
        curAct.execute('update new_table set titulo=%s, artista=%s, anio=%s where id= %s',(Vtitulo,Vartista,Vanio,id))
        mysql.connection.commit()
        
        flash('album Actualizado en BD')  #Agregamos un menaje con flash 
        return redirect(url_for('index'))

@app.route('/borrar/<id>')
def borrar(id):
    curEditar= mysql.connection.cursor() #creamos una consulta
    curEditar.execute('select * from new_table where id= %s ',(id,)) #escribimos la consulta
    consulID=curEditar.fetchone() #para atraer un solo registro con fetchone
    return render_template('Eliminar.html',album=consulID)

@app.route('/eliminaralb/<id>',methods=['POST']) 
def eliminaralb(id):
    if request.method == 'POST':

        curAct=mysql.connection.cursor()
        curAct.execute('delete from new_table where id= %s',(id))
        mysql.connection.commit()
        
        flash('album Actualizado en BD')  #Agregamos un menaje con flash 
        return redirect(url_for('index'))

@app.route('/generar_pdf')
def generar_pdf():
    # Obtenemos la lista de álbumes de la base de datos, similar a lo que hacías en la ruta index.
    curSelect = mysql.connection.cursor()
    curSelect.execute('select * from new_table')
    consulta = curSelect.fetchall()

    # Creamos un objeto de BytesIO para almacenar el contenido del PDF.
    buffer = BytesIO()

    # Creamos el objeto de lienzo (canvas) para el PDF.
    c = canvas.Canvas(buffer,pagesize=letter)

    # Configuramos el tamaño de página y las posiciones iniciales.
    width, height = letter
    x, y = 50, height - 100
    
      # Agregamos los logos al PDF.
    logo_path = 'path/to/logo.png'  # Reemplaza con la ruta de tu archivo de logo
    logo_width, logo_height = 100, 100
    c.drawImage(logo_path, x, y + 30, width=logo_width, height=logo_height)
    c.drawImage(logo_path, width - x - logo_width, y + 30, width=logo_width, height=logo_height)

    # Escribimos el título de la tabla.
    c.setFont('Helvetica-Bold', 20)
    c.drawCentredString(width / 2, y, "Álbumes Guardados")
    y -= 30

    # Escribimos los datos de los álbumes en la tabla.
    c.setFont('Helvetica', 12)
    for album in consulta:
        c.drawString(x, y, f"ID: {album[0]}, Título: {album[1]}, Artista: {album[2]}, Año: {album[3]}")
        y -= 20

    # Guardamos el lienzo (canvas) y terminamos la generación del PDF.
    c.save()

    # Obtenemos el contenido del PDF desde el objeto de BytesIO.
    pdf_content = buffer.getvalue()
    buffer.close()

    # Creamos la respuesta con el contenido del PDF.
    response = Response(pdf_content, content_type='application/pdf')
    response.headers['Content-Disposition'] = 'attachment; filename=albums_guardados.pdf'
    return response

#Linea para ejecutar el servidor
if __name__== '__main__':
    app.run(port= 5000,debug=True) #port: Es el puerto del servidor entre 5000 y 8000
    #debug=true es para no estar abriendo el servidor seguido y ver los cambios en automatico
    