from flask import Blueprint, jsonify, request, g
import uuid
from models.entities.product import Product
from models.product_model import ProductModel
from domain.GildedRose import GildedRose

main = Blueprint('item_blueprint', __name__)


@main.route("/products/<id>", methods=['GET'])
def get_product(id):
    product = ProductModel.get_product(id)
    return product.to_JSON()


@main.route("/products", methods=['GET'])
def get_products():
    products = ProductModel.get_products()
    product = [product.to_JSON() for product in products]
    return jsonify(product)


@main.route('/products', methods=['POST'])
def add_product():
    try:
        name = request.json['name']
        sellin = int(request.json['sellin'])
        quality = int(request.json['quality'])
        type = request.json['type']
        id = uuid.uuid4()
        product = Product(str(id), name, sellin, quality, type)

        affected_rows = ProductModel.add_product(product)
        if affected_rows == 1:
            return jsonify(product.to_JSON())
        else:
            return jsonify({'message': "Error on insert"}), 500

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/products/<id>', methods=['DELETE'])
def delete_product(id):
    try:
        product = Product(id)

        affected_rows = ProductModel.delete_product(product)

        if affected_rows == 1:
            return jsonify({'message': product.id + " Delete successfull"})
        else:
            return jsonify({'message': "No movie delete"}), 404

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/products/<id>', methods=['PUT'])
def update_product(id):
    try:
        name = request.json['name']
        sellin = int(request.json['sellin'])
        quality = int(request.json['quality'])

        product = ProductModel.get_product(id)

        product.name = name
        product.sellin = sellin
        product.quality = quality

        affected_rows = ProductModel.update_product(product)

        if affected_rows == 1:
            return jsonify(product.to_JSON())
        else:
            return jsonify({'message': "No movie updated"}), 404

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route("/update/quality", methods=['PUT'])
def update_quality():
    items = ProductModel.get_products()
    # Create a list of Item objects
    for item in items:
        item_class = GildedRose.create_item(item.id, item.name, item.sellin, item.quality, item.type)
        if item_class is None:
            print(f"No item class found for type '{item.type}'")

        item_class.update_quality()
        item.quality = item_class.quality
        item.sellin = item_class.sell_in
        ProductModel.update_product(item)

    return jsonify({'message': "Inventory updated"}), 200


## health check
@main.route("/check", methods=['GET'])
def check():
    return jsonify({'message': "checkx"}), 200