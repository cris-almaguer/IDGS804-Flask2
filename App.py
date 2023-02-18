from flask import Flask, render_template
from flask import request
from forms import UserForm as user
from forms import NumberForm as number
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
    if request.method == 'POST':
        print(reg_alum.matricula.data)
    else:
        print(reg_alum.nombre.data)
    return render_template('alumnos.html', form = reg_alum)

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

if __name__ == "__main__":
    csrf.init_app(app)
    app.run(debug=True, port=8000)