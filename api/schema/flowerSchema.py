from flask import g
# from config.config import ma
class ProductSchema(g.ma.Schema):
    class Meta: 
        fields = ('id', 'name', 'description', 'price', 'qty')

product_schema = ProductSchema()
products_schema = ProductSchema(many=True)



# class flowerSchema(g.ma.Schema):
#     class Meta: 
#         fields = ('id', 'name', 'description', 'price', 'qty')
