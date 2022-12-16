from flask import *
from loja import db, app, photos
from .forms import Addprodutos
from .models import Marcas, Categorias, Addproduto
import secrets

@app.route('/addmarca', methods=['GET', 'POST'])
def addmarca():
  if 'email' not in session:
    flash(f'Por favor fazer seu login primeiro', 'warning')
    return redirect(url_for('login'))

  if request.method == 'POST':
    getmarca = request.form.get('marca')
    marca = Marcas(name = getmarca)
    db.session.add(marca)
    flash(f'A marca {getmarca} foi cadastrada com sucesso', 'success')
    db.session.commit()
    return redirect(url_for('addmarca'))
  return render_template('produtos/addmarca.html', marcas='marcas')

@app.route('/addcat', methods=['GET', 'POST'])
def addcat():
  if 'email' not in session:
    flash(f'Por favor fazer seu login primeiro', 'warning')
    return redirect(url_for('login'))

  if request.method == 'POST':
    getmarca = request.form.get('categoria')
    cat = Categorias(name = getmarca)
    db.session.add(cat)
    flash(f'A Categoria {getmarca} foi cadastrada com sucesso', 'success')
    db.session.commit()
    return redirect(url_for('addcat'))
  return render_template('produtos/addmarca.html')

@app.route('/addprod', methods=['GET', 'POST'])
def addproduto():
  if 'email' not in session:
    flash(f'Por favor fazer seu login primeiro', 'warning')
    return redirect(url_for('login'))

  marcas = Marcas.query.all()
  categorias = Categorias.query.all()
  form = Addprodutos(request.form)
  if request.method == 'POST':
    
    name = form.name.data
    price = form.price.data
    discount = form.discount.data
    stock = form.stock.data
    colors = form.colors.data
    discription = form.discription.data
    image_1 = photos.save(request.files.get('image_1'), name=secrets.token_hex(10)+".")
    image_2 = photos.save(request.files.get('image_2'), name=secrets.token_hex(10)+".")
    image_3 = photos.save(request.files.get('image_3'), name=secrets.token_hex(10)+".")
    
    marca = request.form.get('marca')
    categoria = request.form.get('categoria')

    addprod = Addproduto(name= name, price= price, discount= discount, stock= stock, colors= colors, discription= discription, marca_id= marca, categoria_id=categoria, image_1= image_1, image_2= image_2, image_3= image_3)
    db.session.add(addprod)
    db.session.commit()
    flash(f'Produto {name} foi cadastrada com sucesso', 'successs')
    return redirect(url_for('admin'))

    
  return render_template('produtos/addproduto.html', form=form, title='Cadastra produtos', marcas= marcas, categorias= categorias)