from flask import jsonify
from model.models import flower
from schema.flowerSchema import products_schema, product_schema

# from flask import request , jsonify, Blueprint
# from schema.flowerSchema import product_schema, products_schema
# from config import db
# import werkzeug

# flower = Blueprint("flower", __name__)


# @flower.route('/product', methods=['POST'])
# def add_product(): 
#     name = request.json['name']
#     description = request.json['description']
#     price = request.json['price']
#     qty = request.json['qty']

#     new_product = models.flower(name, description, price, qty)
#     add_result = db.session.add(new_product)
#     print("ADD RESULT", add_result)
#     db.session.commit()

#     return product_schema.jsonify(new_product)


# Get All Products
.route('/product', methods=["GET"])
def get_products():
    all_products = flower.query.all()
    # Must use .dump because its returning an array of dicitionaries
    result = products_schema.dump(all_products)
    return jsonify(result)

# # Get Onemodels.flower
# @flower.route("/product/<id>",methods=["GET"])
# def getProduct(id): 
#     product =models.flower.query.get(id)
#     return product_schema.jsonify(product)

# # Updatemodels.flower
# @flower.route("/product/<id>", methods=["PUT"])
# def updateProduct(id): 
#     product =models.flower.query.get(id)
#     name = request.json['name']
#     description = request.json['description']
#     price = request.json['price']
#     qty = request.json['qty']

#     product.name = name
#     product.description = description
#     product.price = price 
#     product.qty = qty

#     db.session.commit()
#     return product_schema.jsonify(product)

# @flower.route("/product/<id>", methods=['DELETE'])
# def delete_product(id):
#     product =models.flower.query.get(id)
#     db.session.delete(product)
#     db.session.commit()
#     return product_schema.jsonify(product)

# @flower.errorhandler(werkzeug.exceptions.BadRequest)
# def handle_bad_request(e):
#     print("BADDD REQUEST", e)
#     return 'Sorry the information you entered doesnt align with the current schema for this table', 500

# flower.register_error_handler(500, handle_bad_request)