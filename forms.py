from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList, FormField, SelectField, RadioField
from wtforms.fields import EmailField
from wtforms.validators import DataRequired


class UserForm(Form):
    matricula = StringField('Matricula')
    nombre = StringField('Nombre')
    aPaterno = StringField('Apaterno')
    aMaterno = StringField('Amaterno')
    email = EmailField('Correo')


class NumberForm(Form):
        numero = StringField('numeros', validators=[DataRequired()], render_kw={"required": True, "type": "number", "min": "1", "class": "form-control mb-2"})
    
