from flask import Flask, render_template, flash
from flask import request, make_response
from forms import UserForm as user
from forms import NumberForm as number
from forms import LangForm as lang
from forms import LoginForm as login

from flask_wtf.csrf import CSRFProtect
from Calculos import Calculos

app = Flask(__name__)
app.config['SECRET_KEY'] = 'bea8352d90147ae15aaabf8e5342e85bc899056399aa20e7be005a1849db0a2d'
csrf = CSRFProtect()

@app.route("/formprueba")
def formprueba():
    return render_template('formprueba.html')

@app.route("/alumnos", methods=['GET', 'POST'])
def alumnos():
    reg_alum = user(request.form)
    datos = list()
    if request.method == 'POST' and reg_alum.validate():
        datos.append(reg_alum.matricula.data)
        datos.append(reg_alum.nombre.data)
        print(reg_alum.matricula.data)
        print(reg_alum.nombre.data)

    return render_template('alumnos.html', form = reg_alum, datos = datos)

@app.route("/cookie", methods=['GET', 'POST'])
def cookie():
    reg_user = login(request.form)
    response = make_response(render_template('cookie.html', form = reg_user))

    if request.method == 'POST' and reg_user.validate():
        user = reg_user.username.data
        password = reg_user.password.data
        datos = user + '@' + password
        success_message = 'Bienvenido {}'.format(user)
        response.set_cookie('datos_usuario', datos)
        flash(success_message)
    return response

@app.route("/cajasdinamicas", methods=['GET'])
def cajasd():
    return render_template('cajasdinamicas.html')

@app.route("/numeros", methods=['POST'])
def numeros():
    numeros = int(request.form.get('numeros'))
    reg_number = number(request.form)
    return render_template('numeros.html', numeros = numeros, form = reg_number)

@app.route("/resultado", methods=['POST'])
def resultado():
    numerosString = request.form.getlist('numero')
    numeros = list(map(int, numerosString))
    objCalc = Calculos(numeros)
    maximo = objCalc.calcularMaximo()
    minimo = objCalc.calcularMinimo()
    promedio = objCalc.calcularPromedio()
    masComun = objCalc.calcularMasComun()
    return render_template('resultado.html', maximo = maximo, minimo = minimo, promedio = round(promedio, 2), masComun = masComun)

@app.route("/traductor", methods=['POST', 'GET'])
def traductor():
    reg_lang = lang(request.form)
    if request.method == 'POST' and reg_lang.validate():
        with open('traducciones.txt', 'a') as f:
            f.write(f"{reg_lang.espanniol.data.lower()}={reg_lang.ingles.data.lower()}\n")
        return render_template('traductor.html', form = reg_lang)
    else:
        return render_template('traductor.html', form = reg_lang)

if __name__ == "__main__":
    csrf.init_app(app)
    app.run(debug=True, port=8000)