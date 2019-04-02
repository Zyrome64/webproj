from flask_wtf import FlaskForm,  RecaptchaField
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email
from flask_wtf.file import FileField, FileAllowed, FileRequired




SECRET_KEY = 'secret'

RECAPTCHA_USE_SSL = False
RECAPTCHA_PUBLIC_KEY = '6LeYIbsSAAAAACRPIllxA7wvXjIE411PfdB2gt2J'
RECAPTCHA_PRIVATE_KEY = '6LeYIbsSAAAAAJezaIq3Ft_hSTo0YtyeFG-JgRtu'
RECAPTCHA_OPTIONS = {'theme': 'white'}



class RegisterForm(FlaskForm):
    username = StringField('*Логин', validators=[DataRequired()])
    password = PasswordField('*Пароль', validators=[DataRequired()])
    email = StringField('*Email:', validators=[Email()])
    name = StringField('Name:', validators=[DataRequired()])
    photo = FileField('Image:', validators=[FileRequired(),
        FileAllowed(['jpg', 'png'], 'Images only!')], name="photo")
    accepting = BooleanField('Я даю согласие на обработку персональных данных')
    recaptcha = RecaptchaField()
    submit = SubmitField('Зарегестрироваться')
