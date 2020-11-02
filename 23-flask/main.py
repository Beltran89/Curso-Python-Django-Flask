from flask import Flask,flash, redirect,url_for, render_template, request
from datetime import datetime
from flask_mysqldb import MySQL

app = Flask(__name__)

app.secret_key='clave_secreta_flask'
#Conexion BD

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] =''
app.config['MYSQL_DB'] = 'proyectoflask'

mysql= MySQL(app)

#Context processors
@app.context_processor
def date_now():
    return {
        'now': datetime.utcnow()
    }

#EndPoints

@app.route('/')
def index():
    edad = 15
    personas = ["paco", "manolo", "pepe", "ruben"]
    
    return render_template('index.html',
                            dato1="Valor1",
                            dato2="Valor2",
                            lista=["uno", "dos", "tres"],
                            edad=edad,
                            personas = personas)


@app.route('/informacion')
@app.route('/informacion/<string:nombre>/<string:apellido>/<int:edad>')
def informacion(nombre = None, apellido=None, edad=None):
    texto=""
    
    if nombre !=None and apellido!=None and edad !=None:
        texto= f"Bienvenido {nombre} {apellido} con la edad de {edad}"
        
    return render_template('informacion.html', 
                            texto=texto)



@app.route('/contacto')
@app.route('/contacto/<string:nombre>')
def contacto(nombre=''):
    return render_template('contacto.html')

@app.route('/lenguajes-de-programacion')
@app.route('/lenguajes-de-programacion/<redireccion>')
def lenguajes(redireccion = None):
    
    if redireccion is not None:
        return redirect(url_for('contacto'))
    
    return render_template('lenguajes.html')

@app.route('/crear-coche', methods=['GET', 'POST'])
def crear_coche():
    if request.method == 'POST':
        marca = request.form['marca']
        modelo = request.form['modelo']
        precio = request.form['precio']
        ciudad = request.form['ciudad']
        
        
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO coches VALUES(null, %s, %s, %s, %s )",(marca, modelo, precio, ciudad))
        cursor.connection.commit()
        
        flash("Has Creado el Coche correctamente")
        
        return redirect(url_for('index'))
    
    return render_template('crear_coche.html')

@app.route('/coches')
def coches():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM coches")
    coches = cursor.fetchall()
    cursor.close
    
    return render_template('coches.html', coches=coches)
    
@app.route('/coche/<coche_id>')
def coche(coche_id):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM coches WHERE id= %s",(coche_id))
    coche = cursor.fetchall()
    cursor.close
    
    return render_template('coche.html', coche=coche[0])
    
@app.route('/borrar-coche/<coche_id>')
def borrar_coche(coche_id):
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM coches WHERE id= %s",(coche_id))
    mysql.connection.commit()
    
    flash("EL coche ha sido eliminado!!!!")
    
    return redirect(url_for('coches'))

@app.route('/editar-coche/<coche_id>', methods=['GET', 'POST'])
def editar_coche(coche_id):
    if request.method == 'POST':
        marca = request.form['marca']
        modelo = request.form['modelo']
        precio = request.form['precio']
        ciudad = request.form['ciudad']
        
        cursor = mysql.connection.cursor()
        cursor.execute("UPDATE coches SET marca=%s, modelo=%s, precio=%s, localidad=%s WHERE id =%s",(marca, modelo, precio, ciudad, coche_id))
        cursor.connection.commit()

        flash("HAS EDITADO CORRECTAMENTE!!!!")
        
        return redirect(url_for('coches'))
        
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM coches WHERE id= %s",(coche_id))
    coche = cursor.fetchall()
    cursor.close
    
    return render_template('crear_coche.html', coche=coche[0])


if __name__ == '__main__':
    app.run(debug=True)
