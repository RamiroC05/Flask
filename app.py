from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app=Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'PROGRAMACION2023'
app.config['MYSQL_DB'] = 'sistemadeventas'

conexion = MySQL(app)


@app.route("/")
def index():
    categorias=listabebidas()
    return render_template('home.html', categorias=categorias)

def listabebidas():
    data = {}
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT * FROM categorias"
        cursor.execute(sql)
        categorias = cursor.fetchall()
    except Exception as e:
        print("Error MySQL:", str(e))
    return(categorias)

@app.route("/categ", methods=['POST'])
def seleccion():
    if request.method == 'POST':

        id= request.form['pc']
        
        cursor = conexion.connection.cursor()
        sql= "SELECT * FROM producto WHERE id_cat_corresp = %s " 
        cursor.execute(sql,(id,))
        resultados = cursor.fetchall()

        return render_template('seleccionado.html', resultados=resultados)


if __name__=='__main__':
    app.run()