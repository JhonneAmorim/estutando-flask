from flask_wtf.file import FileAllowed, FileField, FileRequired
from wtforms import Form, IntegerField, StringField, BooleanField, TextAreaField, validators


class Addprodutos(Form):
  name = StringField('Nome: ',[validators.DataRequired()])
  price = IntegerField('Preço: ',[validators.DataRequired()])
  discount = IntegerField('Desconto: ',[validators.DataRequired()])
  stock = IntegerField('Estoque: ',[validators.DataRequired()])
  discription = TextAreaField('Descrição: ',[validators.DataRequired()])
  colors = TextAreaField('Cor: ',[validators.DataRequired()])

  image_1 = FileField('Imagem 1: ', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'gif', 'jpeg'])])
  image_2 = FileField('Imagem 2: ', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'gif', 'jpeg'])])
  image_3 = FileField('Imagem 3: ', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'gif', 'jpeg'])])
  