from wtforms import Form, BooleanField, StringField, PasswordField, validators

class RegistrationForm(Form):
    name = StringField('nome', [validators.Length(min=4, max=25)])
    username = StringField('Usuario', [validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('Digite sua senha', [
        validators.DataRequired(),
        validators.EqualTo('Confirma sua senha', message='Sua senha e confirmação não são iguais')
    ])
    confirm = PasswordField('Digite sua senha novamente')
    