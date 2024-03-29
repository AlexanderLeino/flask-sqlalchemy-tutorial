from config import db
from main import ma


class flower(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(200))
    price = db.Column(db.Float)
    qty = db.Column(db.Integer)

    def __init__(self, name, description, price, qty):
        self.name = name
        self.description = description
        self.price = price
        self.qty = qty

class flowerSchema(ma.Schema):
    class Meta: 
        fields = ('id', 'name', 'description', 'price', 'qty')

