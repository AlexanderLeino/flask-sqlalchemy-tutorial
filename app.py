from flask import Flask, request, jsonify, g
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os 
from flask import jsonify
from api.model.models import flower
from api.schema.flowerSchema import products_schema, product_schema

# Init App
app = Flask(__name__)

# Database
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+mysqlconnector://root:root@localhost:3306/greeneyedb'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Init db


# Init ma
ma = Marshmallow(app)

def get_ma():
    if 'ma' not in g:
        g.ma = ma
        ("print G", g.db
         )
    return g.db

@app.teardown_appcontext
def teardown_db(exception):
    g.pop('ma', None)
#


def get_db():
    print("GETTING DB SET")
    if 'db' not in g:
        g.db = SQLAlchemy(app)
        ("print G", g.db
         )
    return g.db

@app.teardown_appcontext
def teardown_db(exception):
    db = g.pop('db', None)

    if db is not None:
        db.close()
#

# # Product Schema
# class ProductSchema(ma.Schema):
#     class Meta: 
#         fields = ('id', 'name', 'description', 'price', 'qty')


# # Init Schema
# product_schema = ProductSchema()
# products_schema = ProductSchema(many=True)

# # Create a Product
# @app.route('/product', methods=['POST'])
# def add_product(): 
#     name = request.json['name']
#     description = request.json['description']
#     price = request.json['price']
#     qty = request.json['qty']

#     new_product = Product(name, description, price, qty)
#     db.session.add(new_product)
#     db.session.commit()

#     return product_schema.jsonify(new_product)


# @app.route('/', methods=["GET"])
# def find_product():
#     return 
# # Run Server
app.route('/product', methods=["GET"])
def get_products():
    all_products = flower.query.all()
    # Must use .dump because its returning an array of dicitionaries
    result = products_schema.dump(all_products)
    return jsonify(result)
if __name__ == '__main__':
    app.run(debug=True)
    get_db()
    get_ma()
