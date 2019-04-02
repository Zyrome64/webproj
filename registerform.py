from flask_wtf import FlaskForm,  RecaptchaField
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email
from flask_wtf.file import FileField, FileAllowed, FileRequired




SECRET_KEY = 'secret'

RECAPTCHA_PUBLIC_KEY = '6LeYIbsSAAAAACRPIllxA7wvXjIE411PfdB2gt2J'
RECAPTCHA_PRIVATE_KEY = '6LeYIbsSAAAAAJezaIq3Ft_hSTo0YtyeFG-JgRtu'



class RegisterForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    email = StringField('Email:', validators=[Email()])
    name = StringField('Имя:', validators=[DataRequired()])
    photo = FileField(validators=[FileRequired()])

    recaptcha = RecaptchaField()
    submit = SubmitField('Зарегестрироваться')
