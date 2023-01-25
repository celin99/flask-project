from flask_mysqldb import MySQL
import mysql.connector
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import urllib.request, json


app = Flask(__name__)

app.config['MYSQL_HOST'] = '172.21.163.219'
app.config['MYSQL_USER'] = 'sci'
app.config['MYSQL_PASSWORD'] = 'Sci@2023*'
app.config['MYSQL_DB'] = 'intra'

mysql = MySQL(app)
    
main = []
concessao = []
registros = []
recursos = []
recursostp = []
cadconc = []
nrecurso = []
nfiscal = []
cadnf = []
marcas = []
novamarcas = []



@app.route('/')
def main():
    return render_template("mains.html", main=main)

@app.route('/show_db', methods=["GET", "POST"])
def show_db():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * from colaboradores')
    rows = cur.fetchall()
    return render_template('show_db.html', rows=rows)


@app.route('/concessao', methods=["GET", "POST"])
def principal():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM sc_concessao")
    concessao = cur.fetchall()
    return render_template("concessao.html", concessao=concessao)

@app.route('/cadastro_concessao', methods=["GET", "POST"])
def cadastroconc():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM sc_concessao")
    cadconc = cur.fetchall()
    return render_template("cadastroconcessao.html", cadconc=cadconc)


@app.route('/recurso')
def sobre():
    return render_template("recurso.html", registros=registros)


@app.route('/recurso_tipo')
def recursotipo():
    return render_template("recursotipo.html", recursos=recursos)


@app.route('/novo_recurso_tipo')
def novorecursotipo():
    return render_template("novorecursotipo.html", recursostp=recursostp)


@app.route('/novo_recurso')
def novorecurso():
    return render_template("novorecurso.html", nrecurso=nrecurso)


@app.route('/nota_fiscal')
def notafiscal():
    return render_template("notafiscal.html", nfiscal=nfiscal)


@app.route('/cadastro_nf')
def cadastronf():
    return render_template("cadastronf.html", cadnf=cadnf)


@app.route('/marcas')
def marca():
    return render_template("marcas.html", marcas=marcas)


@app.route('/nova_marca')
def novamarca():
    return render_template("novamarca.html", novamarcas=novamarcas)

@app.route('/filmes')
def filmes():
    url = "https://api.themoviedb.org/3/discover/movie?certification_country=US&certification.lte=G&sort_by=popularity.desc&api_key=3ddc9b92db4de6c6559569c67bd88a13"
    
    resposta = urllib.request.urlopen(url)
    
    dados = resposta.read()
    
    jsondata = json.loads(dados)

    return render_template("filmes.html", filmes=jsondata['results'])

if __name__ == "__main__":
    app.run(debug=True)

# cur.close()
