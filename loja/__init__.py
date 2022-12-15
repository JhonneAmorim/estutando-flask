from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///minhaloja.db'
app.config['SECRET_KEY'] = '123jhonne123'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from loja.admin import rotas
from loja.produtos import rotas