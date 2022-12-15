from flask import *

from loja import db, app
from .models import Marcas, Categorias

@app.route('/addmarca', methods=['GET', 'POST'])
def addmarca():
  if request.method == 'POST':
    getmarca = request.form.get('marca')
    marca = Marcas(name = getmarca)
    db.session.add(marca)
    flash(f'A marca {getmarca} foi cadastrada com sucesso', 'success')
    db.session.commit()
    return redirect(url_for('addmarca'))
  return render_template('produtos/addmarca.html', marcas='marcas')