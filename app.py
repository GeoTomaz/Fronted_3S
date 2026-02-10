from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = '0000'

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/calculos')
def calculos():
    return render_template("calculos.html")

@app.route('/funcionarios')
def funcionarios():
    return render_template("funcionarios.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/operacoes')
def operacoes():
    return render_template("operacoes.html")

@app.route('/somar', methods=['GET', 'POST'])
def somar():
    if request.method == 'POST':
        if request.form['form-n1'] and request.form['form-n2']:
            n1 = int(request.form['form-n1'])
            n2 = int(request.form['form-n2'])
            soma = n1 + n2
            flash("soma realizada", 'alert-success')
            return render_template("operacoes.html", n1=n1, n2=n2, soma=soma)
        else:
            # Passo 1: Emitir a mensagem e a categoria do flash
            flash("preencha o campo para realizar a soma", 'alert-danger')

    return render_template("operacoes.html")

@app.route('/subtrair', methods=['GET', 'POST'])
def subtrair():
    if request.method == 'POST':
        if request.form['form-n1'] and request.form['form-n2']:
            n1 = int(request.form['form-n1'])
            n2 = int(request.form['form-n2'])
            subtrair = n1 - n2
            flash("subtração realizada", 'alert-success')
            return render_template("operacoes.html", n1=n1, n2=n2, subtrair=subtrair)
        else:
            # Passo 1: Emitir a mensagem e a categoria do flash
            flash("preencha o campo para realizar a subtração", 'alert-danger')
    return render_template("operacoes.html")

@app.route('/multiplicar', methods=['GET', 'POST'])
def multiplicar():
    if request.method == 'POST':
        if request.form['form-n1'] and request.form['form-n2']:
            n1 = int(request.form['form-n1'])
            n2 = int(request.form['form-n2'])
            multiplicar = n1 * n2
            flash("multiplicação realizada", 'alert-success')
            return render_template("operacoes.html", n1=n1, n2=n2, multiplicar=multiplicar)
        else:
            # Passo 1: Emitir a mensagem e a categoria do flash
            flash("preencha o campo para realizar a multiplicação", 'alert-danger')
    return render_template("operacoes.html")

@app.route('/dividir', methods=['GET', 'POST'])
def dividir():
    if request.method == 'POST':
        if request.form['form-n1'] and request.form['form-n2']:
            n1 = int(request.form['form-n1'])
            n2 = int(request.form['form-n2'])
            dividir = n1 / n2
            flash("divisão realizada", 'alert-success')
            return render_template("operacoes.html", n1=n1, n2=n2, dividir=dividir)
        else:
            # Passo 1: Emitir a mensagem e a categoria do flash
            flash("preencha o campo para realizar a divisão", 'alert-danger')
    return render_template("operacoes.html")

@app.route('/geometria')
def geometria():
    return render_template("geometria.html")

@app.route('/circulo', methods=['GET', 'POST'])
def circulo():
    if request.method == 'POST':
        if request.form['form-n1']:
            n1 = int(request.form['form-n1'])
            area_c = 3.14 * n1 * n1
            perimetro_c = 6.28 * n1
            flash("calculo realizado", 'alert-success')
            return render_template("geometria.html", n1=n1, area_c=area_c, perimetro_c=perimetro_c)
        else:
            # Passo 1: Emitir a mensagem e a categoria do flash
            flash("O campo Lado é obrigatório! Preencha para calcular", 'alert-danger')
    return render_template("geometria.html")

@app.route('/triangulo', methods=['GET', 'POST'])
def triangulo():
    if request.method == 'POST':
        if request.form['form-n1'] and request.form['form-n2']:
            n1 = int(request.form['form-n1'])
            n2 = int(request.form['form-n2'])
            area_t = n1 * n2 / 2
            perimetro_t = n1 + n2 + n2
            flash("calculo realizado", 'alert-success')
            return render_template("geometria.html", n1=n1, n2=n2, area_t=area_t, perimetro_t=perimetro_t)
        else:
            # Passo 1: Emitir a mensagem e a categoria do flash
            flash("O campo Lado é obrigatório! Preencha para calcular", 'alert-danger')
    return render_template("geometria.html")

@app.route('/quadrado', methods=['GET', 'POST'])
def quadrado():
    if request.method == 'POST':
        if request.form['form-n1'] and request.form['form-n2']:
            n1 = int(request.form['form-n1'])
            n2 = int(request.form['form-n2'])
            area_q = n1 * n2
            perimetro_q = n1 * n2
            flash("calculo realizado", 'alert-success')
            return render_template("geometria.html", n1=n1, n2=n2, area_q=area_q, perimetro_q=perimetro_q)
        else:
            # Passo 1: Emitir a mensagem e a categoria do flash
            flash("O campo Lado é obrigatório! Preencha para calcular", 'alert-danger')
    return render_template("geometria.html")

@app.route('/hexagono', methods=['GET', 'POST'])
def hexagono():
    if request.method == 'POST':
        if request.form['form-n1']:
            n1 = int(request.form['form-n1'])

            elevado = n1 * n1
            raiz = elevado * 0.5
            resultado = elevado * raiz
            resultado2 = resultado / 4
            hexagono = resultado2 * 6
            perimetro_h = n1 * 6
            flash("calculo realizado", 'alert-success')
            return render_template("geometria.html", n1=n1, elevado=elevado, raiz=raiz, resultado=resultado, resultado2=resultado2, hexagono=hexagono, perimetro_h=perimetro_h)
        else:
            # Passo 1: Emitir a mensagem e a categoria do flash
            flash("O campo Lado é obrigatório! Preencha para calcular", 'alert-danger')
    return render_template("geometria.html")


#TODO Final do código

if __name__ == '__main__':
    app.run(debug=True)