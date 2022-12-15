from flask import *

from loja import app, db, bcrypt
from .formulario import RegistrationForm, LoginFormulario
from .models import User
import os


@app.route('/admin')
def admin():
  if 'email' not in session:
    flash(f'Por favor fazer seu login primeiro', 'warning')
    return redirect(url_for('login'))
  return render_template('admin/index.html', title='Pagina Administrativa')

@app.route('/registrar', methods=['GET', 'POST'])
def registrar():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        hash_password = bcrypt.generate_password_hash(form.password.data)
        user = User(name = form.name.data, username = form.username.data, email = form.email.data,
        password = hash_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Obrigado {form.name.data} por se registrar','success')
        return redirect(url_for('login'))
    return render_template('admin/registrar.html', title="Pagina de Registros", form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
  form = LoginFormulario(request.form)
  if request.method == "POST" and form.validate():
    user = User.query.filter_by(email = form.email.data).first()
    if user and bcrypt.check_password_hash(user.password, form.password.data):
      session['email'] = form.email.data
      flash(f'Logado com sucesso {form.email.data}','success')
      return redirect(request.args.get('next') or url_for('admin'))
    else:
      flash(f'Email ou senha invalida!!!','danger')
  return render_template('admin/login.html', form=form, title='Login')