from flask import Flask, render_template, request

app = Flask(__name__)

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


@app.route('/', methods=["GET", "POST"])
def main():
    if request.method == "POST":
        if request.form.get("main"):
            concessao.append(request.form.get("main"))
    return render_template("mains.html", main=main)


@app.route('/concessao', methods=["GET", "POST"])
def principal():
    if request.method == "POST":
        if request.form.get("principal"):
            concessao.append(request.form.get("principal"))
    return render_template("concessao.html", concessao=concessao)


@app.route('/recurso', methods=["GET", "POST"])
def sobre():
    if request.method == "POST":
        if request.form.get("aluno") and request.form.get("nota"):
            registros.append({"aluno": request.form.get(
                "aluno"), "nota": request.form.get("nota")})
    return render_template("recurso.html", registros=registros)


@app.route('/recurso_tipo', methods=["GET", "POST"])
def recursotipo():
    if request.method == "POST":
        if request.form.get("recurso") and request.form.get("recurso"):
            recursos.append({"recurso": request.form.get(
                "recurso"), "recurso": request.form.get("recurso")})
    return render_template("recursotipo.html", recursos=recursos)


@app.route('/novo_recurso_tipo', methods=["GET", "POST"])
def novorecursotipo():
    if request.method == "POST":
        if request.form.get("recursotipo") and request.form.get("recursotipo"):
            recursos.append({"recursotipo": request.form.get(
                "recursotipo"), "recursotipo": request.form.get("recursotipo")})
    return render_template("novorecursotipo.html", recursostp=recursostp)


@app.route('/cadastro_concessao', methods=["GET", "POST"])
def cadastroconc():
    if request.method == "POST":
        if request.form.get("cad_conc") and request.form.get("cad_conc"):
            recursos.append({"cad_conc": request.form.get(
                "cad_conc"), "cad_conc": request.form.get("cad_conc")})
    return render_template("cadastroconcessao.html", cadconc=cadconc)


@app.route('/novo_recurso', methods=["GET", "POST"])
def novorecurso():
    if request.method == "POST":
        if request.form.get("novo_rec") and request.form.get("novo_rec"):
            recursos.append({"novo_rec": request.form.get(
                "novo_rec"), "novo_rec": request.form.get("novo_rec")})
    return render_template("novorecurso.html", nrecurso=nrecurso)


@app.route('/nota_fiscal', methods=["GET", "POST"])
def notafiscal():
    if request.method == "POST":
        if request.form.get("n_fisc") and request.form.get("n_fisc"):
            recursos.append({"n_fisc": request.form.get("n_fisc"),
                           "n_fisc": request.form.get("n_fisc")})
    return render_template("notafiscal.html", nfiscal=nfiscal)


@app.route('/cadastro_nf', methods=["GET", "POST"])
def cadastronf():
    if request.method == "POST":
        if request.form.get("cad_nf") and request.form.get("cad_nf"):
            recursos.append({"cad_nf": request.form.get("cad_nf"),
                           "cad_nf": request.form.get("cad_nf")})
    return render_template("cadastronf.html", cadnf=cadnf)


@app.route('/marcas', methods=["GET", "POST"])
def marca():
    if request.method == "POST":
        if request.form.get("marcas") and request.form.get("marcas"):
            recursos.append({"marcas": request.form.get("marcas"),
                           "marcas": request.form.get("marcas")})
    return render_template("marcas.html", marcas=marcas)


@app.route('/nova_marca', methods=["GET", "POST"])
def novamarca():
    if request.method == "POST":
        if request.form.get("n_marcas") and request.form.get("n_marcas"):
            recursos.append({"n_marcas": request.form.get(
                "n_marcas"), "n_marcas": request.form.get("n_marcas")})
    return render_template("novamarca.html", novamarcas=novamarcas)
