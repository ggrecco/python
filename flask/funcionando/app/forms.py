from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.models import Usuario

class RegistrationForm(FlaskForm):
    username = StringField('Usuario', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Senha', validators=[DataRequired()])
    password2 = PasswordField('Repita a senha', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = Usuario.query.filter_by(nome=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

            def validate_email(self, email):
                user = Usuario.query.filter_by(email=email.data).first()
                if user is not None:
                    raise ValidationError('Please use a different email address.')


class DeletarForm(FlaskForm):
    submit = SubmitField('Deletar')


class LoginForm(FlaskForm):
    username = StringField('Usuário', validators=[DataRequired()])
    password = PasswordField('Senha', validators=[DataRequired()])
    remember_me = BooleanField('Lembrar')
    submit = SubmitField('Entrar')


class EditProfileForm(FlaskForm):
    username = StringField('Nome de Usuario', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired()])
    email2 = StringField('Repita o e-mail', validators=[DataRequired(), EqualTo('email')])
    submit = SubmitField('alterar')


class ScrapyForm(FlaskForm):
    linguagem = StringField('Linguagem', validators=[DataRequired()])
    submit = SubmitField('Pesquisar')


class ServidorForm(FlaskForm):
    servidor = StringField('Servidor', validators=[DataRequired()])
    url = StringField('Url', validators=[DataRequired()])
    registro = SubmitField('Registrar')