from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList, FormField, SelectField, RadioField, PasswordField
from wtforms.fields import EmailField
from wtforms.validators import DataRequired as DataR
from wtforms import validators
bandasOpciones = ['Negro', 'Marrón', 'Rojo', 'Naranja', 'Amarillo', 'Verde', 'Azul', 'Violeta', 'Gris', 'Blanco']

def mi_validacion(form, field):
    if len(field.data) == 0:
        raise validators.ValidationError('El campo no tiene datos')

class UserForm(Form):
    matricula = StringField('Matricula',
                [validators.DataRequired(message='El campo matricula es requerido'),
                validators.length(min=5, max=10, message="Ingresa min 5 max 10")])
    nombre = StringField('Nombre',
                [validators.DataRequired(message='El campo Nombre es requerido')])
    aPaterno = StringField('Apaterno', [mi_validacion])
    aMaterno = StringField('Amaterno')
    email = EmailField('Correo')


class NumberForm(Form):
    numero = StringField('numeros', validators=[DataR()], render_kw={"required": True, "type": "number", "min": "1", "class": "form-control mb-2"})
    
class LangForm(Form):
    espanniol = StringField('Español', [validators.DataRequired(message='Este campo es requerido')])
    ingles = StringField('Inglés', [validators.DataRequired(message='Este campo es requerido')])

class TradForm(Form):
    espanniolSalida = StringField('Español')
    inglesSalida = StringField('Inglés')
    lenguaje = RadioField('Idioma', [validators.DataRequired(message='Este campo es requerido')], choices=[('es', 'Español'), ('en', 'Inglés')])

class LoginForm(Form):
    username = StringField('Usuario', [validators.DataRequired(message="El campo usuario es requerido"),
                validators.length(min=5, max=10, message="Ingresa min 5 max 10")])
    password = PasswordField('Contraseña', [validators.DataRequired(message="El campo contraseña es requerido"),
                validators.length(min=5, max=10, message="Ingresa min 5 max 10")])

class ResForm(Form):
    banda_uno = SelectField('Banda 1', [validators.DataRequired(message="El campo es requerido")], render_kw={"class": "form-select mb-2"}, choices=bandasOpciones)
    banda_dos = SelectField('Banda 2', [validators.DataRequired(message="El campo es requerido")], render_kw={"class": "form-select mb-2"}, choices=bandasOpciones)
    banda_tres = SelectField('Banda 3', [validators.DataRequired(message="El campo es requerido")], render_kw={"class": "form-select mb-2"}, choices=bandasOpciones)
    tolerancia = RadioField('Tolerancia', [validators.DataRequired(message="El campo es requerido")], render_kw={"class": "mb-3"}, choices=list(zip([5, 10], ["Dorado 5%", "Plata 10%"])), widget=None)