from flask import Flask,render_template,request,redirect,url_for,flash
from flask_mysqldb import MySQL 

app = Flask(__name__)
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='DB_Floreria'

app.secret_key = 'mysecretkey'

mysql =MySQL(app)

@app.route('/')
def index():
    curSelect=mysql.connection.cursor()
    curSelect.execute('select * from tbFlores')
    consulta = curSelect.fetchall()
    
    return render_template('index.html',listFlor=consulta)

@app.route('/guardar',methods=['POST'])
def guardar():
    if request.method == 'POST':
        
        Vnombre=request.form['txtNombre']
        Vcantidad=request.form['txtCantidad']
        Vprecio=request.form['txtPrecio']
        
        curguar=mysql.connection.cursor()
        curguar.execute('insert into tbFlores(nombre,cantidad,precio) values(%s,%s,%s)',(Vnombre,Vcantidad,Vprecio))
        mysql.connection.commit()
    
    flash('Flor agregada correctamente')
    return redirect(url_for('index'))

@app.route('/borrar/<id>')
def borrar(id):
    curEditar= mysql.connection.cursor()
    curEditar.execute('select * from tbFlores where id= %s ',(id,))
    consulID=curEditar.fetchone()
    return render_template('Eliminar.html',flor=consulID)


@app.route('/eliminar/<id>',methods=['POST']) 
def eliminar(id):
    if request.method == 'POST':
        
        cureli=mysql.connection.cursor()
        cureli.execute('delete from tbFlores where id= %s',(id))
        mysql.connection.commit()
        
        flash('Flor eliminada en DB')
        return redirect(url_for('index'))

@app.route('/regresar')
def regresar():
    return render_template('index.html')
    
    
if __name__=='__main__':
    app.run(port=4000,debug=True)
    
