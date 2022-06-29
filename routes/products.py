from flask import Blueprint, jsonify, request
from database.models.ProductModel import Product
from database import db
from schema.productSchema import ProductSchema


# Initialize Schema
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

# Creates products blue print
product_blueprint = Blueprint('product', __name__)


@product_blueprint.route('/product', methods=['GET'])
def find_all():
    all_products = Product.query.all()
    result = products_schema.dump(all_products)
    return jsonify(result)


@product_blueprint.route('/product/<id>', methods=['GET'])
def get_one(id):
    product = Product.query.get(id)
    return product_schema.jsonify(product)


@product_blueprint.route('/product', methods=['POST'])
def create():
    try:
        name = request.json['name']
        description = request.json['description']
        price = request.json['price']
        quantity = request.json['quantity']

        new_product = Product(name, description, price, quantity)

        db.session.add(new_product)
        db.session.commit()

        return product_schema.jsonify(new_product)
    except BaseException as err:
        return jsonify({"error": "Internal Server Error", "statusCode": 500})


@product_blueprint.route('/product/<id>', methods=['PUT'])
def update(id):
    try:
        product = Product.query.get(id)
        product.name = request.json['name'] or product.name
        product.description = request.json['description'] or product.description
        product.price = request.json['price'] or product.price
        product.quantity = request.json['quantity'] or product.quantity

        db.session.commit()

        return product_schema.jsonify(product)
    except BaseException as err:
        return jsonify({"error": "Internal Server Error", "statusCode": 500})


@product_blueprint.route('/product/<id>', methods=['DELETE'])
def delete(id):
    try:
        product = Product.query.get(id)
        db.session.delete(product)
        db.session.commit()
        return jsonify({"name": product.name})
    except BaseException as err:
        return jsonify({"error": "Internal Server Error", "statusCode": 500})
