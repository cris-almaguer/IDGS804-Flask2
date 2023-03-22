from flask import Flask, render_template, flash, send_file, make_response, request, redirect
from forms import UserForm as user
from forms import NumberForm as number
from forms import LangForm as lang
from forms import LoginForm as login
from forms import TradForm as trad
from forms import ResForm as res
from flask_wtf.csrf import CSRFProtect
from Calculos import Calculos
import datetime, os

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
        password = reg_user.username.data
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
    reg_trad = trad(request.form)
    if request.method == 'POST' and reg_lang.validate():
        with open('traducciones.txt', 'a') as f:
            f.write(f"{reg_lang.espanniol.data.lower()}={reg_lang.ingles.data.lower()}\n")
        flash('Traducción agregada correctamente')
        return render_template('traductor.html', form = reg_lang, formSalida = reg_trad)
    else:
        return render_template('traductor.html', form = reg_lang, formSalida = reg_trad)

@app.route("/traductor_resultado", methods=['POST', 'GET'])
def traductor_resultado():
    reg_trad = trad(request.form)
    reg_lang = lang(request.form)
    if request.method == 'POST' and reg_trad.validate():
        idioma = request.form.get('lenguaje')
        if idioma == 'es':
            palabra = request.form.get('espanniolSalida')
        else:
            palabra = request.form.get('inglesSalida')
        resultado = buscar_traduccion(palabra, idioma)
        if resultado is '':
            if idioma == 'es':
                mensaje = "No se encontró traducción para {} en inglés.".format(palabra)
            elif idioma == 'en':
                mensaje = "No se encontró traducción para {} en español.".format(palabra)
            flash(mensaje)
        if idioma == 'es':
            return render_template('traductor.html', form = reg_lang, formSalida = reg_trad, ingles = resultado, español = palabra)
        else:
            return render_template('traductor.html', form = reg_lang, formSalida = reg_trad, ingles = palabra, español = resultado)
    return render_template('traductor.html', form = reg_lang, formSalida = reg_trad)

def buscar_traduccion(palabra, lenguaje):
    with open('traducciones.txt', 'r') as f:
        lineas = f.readlines()
        for linea in lineas:
            partes = linea.strip().split('=')
            if len(partes) == 2:
                if lenguaje == 'es' and partes[0].lower() == palabra.lower():
                    return partes[1]
                elif lenguaje == 'en' and partes[1].lower() == palabra.lower():
                    return partes[0]
    return ''

def calcular_resistencia(banda_uno, banda_dos, banda_tres, tolerancia_str): 
    colores = {"Negro": 0, "Marrón": 1, "Rojo": 2, "Naranja": 3, "Amarillo": 4, "Verde": 5, "Azul": 6, "Violeta": 7, "Gris": 8, "Blanco": 9}   
    valor = (colores[banda_uno] * 10 + colores[banda_dos]) * (10 ** colores[banda_tres])

    if tolerancia_str == 'Dorado':
        tolerancia = 5.0
    else:
        tolerancia = 10.0

    maximo = valor * (1 + tolerancia / 100)
    minimo = valor * (1 - tolerancia / 100)

    tolerancia_str = str(int(tolerancia)) + '%'

    if tolerancia == 5.0:
        tolerancia_color = '#AB8000'
    else:
        tolerancia_color = '#BEBEBE'
    return {'valor': round(valor, 2), 'maximo': round(maximo, 2), 'minimo': round(minimo, 2), 'tolerancia': tolerancia_str, 'tolerancia_color': tolerancia_color,'banda_uno': banda_uno, 'banda_dos': banda_dos, 'banda_tres': banda_tres}

def guardar_registros(lista_resultado):
    cadena_texto = ''
    with open('resistencias.txt', 'a', encoding='utf-8') as f:
        for item in range(0, len(lista_resultado)):
            if item == 3:
                cadena_texto += lista_resultado[item] + '\n'
            else:
                cadena_texto += lista_resultado[item] + ', '
        f.write(cadena_texto)

def leer_archivo():
    with open('resistencias.txt', encoding='utf-8') as archivo:
        lineas = archivo.readlines()
    resistencias = []
    for linea in lineas:
        valores = linea.strip().split(', ')
        print(valores)
        resistencia = {
            'banda_uno': valores[0],
            'banda_dos': valores[1],
            'banda_tres': valores[2],
            'tolerancia': valores[3]
        }
        resistencias.append(resistencia)
    return resistencias

@app.route("/resistencia", methods=['POST', 'GET'])
def resistencia():
    reg_res = res(request.form)
    colores = { "Negro": "#000000", "Marrón": "#8B4513", "Rojo": "#FF0000", "Naranja": "#FFA500", "Amarillo": "#FFFF00", "Verde": "#008000", "Azul": "#0000FF", "Violeta": "#EE82EE", "Gris": "#808080", "Blanco": "#FFFFFF" }
    if request.method == 'POST' and reg_res.validate():
        valores_request = request.form.to_dict()
        valores_lista = list(valores_request.values())
        lista_resultado = valores_lista[1:5]
        guardar_registros(lista_resultado=lista_resultado)
        valores_lectura = leer_archivo()
        listado_registros = []
        for item in valores_lectura:
            listado_registros.append(calcular_resistencia(item['banda_uno'], item['banda_dos'], item['banda_tres'], item['tolerancia']))   
        return render_template('resistencia.html', form = reg_res, resultado = listado_registros, colores=colores)
    else:
        valores_lectura = leer_archivo()
        listado_registros = []
        for item in valores_lectura:
            listado_registros.append(calcular_resistencia(item['banda_uno'], item['banda_dos'], item['banda_tres'], item['tolerancia']))
        return render_template('resistencia.html', form = reg_res, resultado = listado_registros, colores=colores)

@app.route("/descargar", methods=['GET'])
def descargar_archivo():
    if request.method == 'GET':
        try:
            if os.path.getsize('resistencias.txt') > 0:
                return send_file('resistencias.txt', as_attachment=True)
            else:
                flash('No hay calculos guardados')
                return redirect('/resistencia')
        except Exception as e:
            flash('Hubo un error inesperado al descargar')
            return redirect('/resistencia')

if __name__ == "__main__":
    csrf.init_app(app)
    app.run(debug=True, port=8001)