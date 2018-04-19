from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.models import User

class LoginForm(FlaskForm):
    # username = StringField('Username', validators=[DataRequired()])
    username = StringField('Usário', validators=[DataRequired()])
    # password = PasswordField('Password', validators=[DataRequired()])
    password = PasswordField('Senha', validators=[DataRequired()])
    # remember_me = BooleanField('Remember Me')
    remember_me = BooleanField('Lembrar')
    # submit = SubmitField('Sign in')
    submit = SubmitField('Entrar')

class RegistrationForm(FlaskForm):
    username = StringField('Usuário', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Senha', validators=[DataRequired()])
    password2 = PasswordField('Repita a Senha', validators=[DataRequired(), EqualTo('password')] )
    submit = SubmitField('Registar')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Por Favor use outro nome de usuário.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Por Favor use outro e-mail.')
