from flask import *

from loja import app, db, bcrypt
from .formulario import RegistrationForm
from .models import User
import os


@app.route('/')
def home():
  return "seja bem vindo ao sistema em flask"

@app.route('/registrar', methods=['GET', 'POST'])
def registrar():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        hash_password = bcrypt.generate_password_hash(form.password.data)
        user = User(name = form.name.data, username = form.username.data, email = form.email.data,
        password = hash_password, profile = form.username.data)
        db.session.add(user)
        flash('Obrigado por se registrar')
        return redirect(url_for('login'))
    return render_template('admin/registrar.html', title="Pagina de Registros", form=form)
