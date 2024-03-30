from flask import g

class flower(g.db.Model): 
    id = g.db.Column(g.db.Integer, primary_key=True)
    name = g.db.Column(g.db.String(100), unique=True)
    description = g.db.Column(g.db.String(200))
    price = g.db.Column(g.db.Float)
    qty = g.db.Column(g.db.Integer)

    def __init__(self, name, description, price, qty):
        self.name = name
        self.description = description
        self.price = price
        self.qty = qty


class Product(g.db.Model): 
    id = g.db.Column(g.db.Integer, primary_key=True)
    name = g.db.Column(g.db.String(100), unique=True)
    description = g.db.Column(g.db.String(200))
    price = g.db.Column(g.db.Float)
    qty = g.db.Column(g.db.Integer)

    def __init__(self, name, description, price, qty):
        self.name = name
        self.description = description
        self.price = price
        self.qty = qty

# Product Schema
class ProductSchema(g.ma.Schema):
    class Meta: 
        fields = ('id', 'name', 'description', 'price', 'qty')
