from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList, FormField, SelectField, RadioField, PasswordField
from wtforms.fields import EmailField
from wtforms.validators import DataRequired as DataR
from wtforms import validators

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
    espanniol = StringField('Español', [validators.DataRequired(message='El campo es requerido')])
    ingles = StringField('Inglés', [validators.DataRequired(message='El campo es requerido')])
    lenguaje = RadioField('Idioma', choices=[('es', 'Español'), ('en', 'Inglés')])
    campo = StringField('Campo', [validators.DataRequired(message='El campo es requerido')])

class LoginForm(Form):
    username = StringField('Usuario', [validators.DataRequired(message="El campo usuario es requerido"),
                validators.length(min=5, max=10, message="Ingresa min 5 max 10")])
    password = PasswordField('Contraseña', [validators.DataRequired(message="El campo contraseña es requerido"),
                validators.length(min=5, max=10, message="Ingresa min 5 max 10")])