
from flask import Blueprint,request, jsonify
from app.status_codes import HTTP_400_BAD_REQUEST,HTTP_404_NOT_FOUND, HTTP_409_CONFLICT,HTTP_403_FORBIDDEN, HTTP_500_INTERNAL_SERVER_ERROR,HTTP_201_CREATED,HTTP_200_OK,HTTP_401_UNAUTHORIZED

from app.models.product import Product
from app.extensions import db, bcrypt
from flask_jwt_extended import create_access_token, create_refresh_token
from flask_jwt_extended import get_jwt_identity,  jwt_required

#Product blueprint
products = Blueprint('products', __name__,url_prefix= '/api/v1/products')


@products.route('/products', methods=['POST'])

# Creating new product
def create_product():
    data = request.get_json()
    print("Received data:", data)

    name = data.get('name')
    price = data.get('price')
    description = data.get('description')

# Validation
    if not name or not price:
        return jsonify({"error": "Product name and price are required."}), HTTP_400_BAD_REQUEST

    try:
        new_product = Product(name=name, price=price, description=description)
        db.session.add(new_product)
        db.session.commit()
    except Exception as e:
        return jsonify({"error": str(e)}), HTTP_500_INTERNAL_SERVER_ERROR

    return jsonify({
        "message": "Product created successfully.",
        "product": {
            "id": new_product.id,
            "name": new_product.name,
            "price": new_product.price,
            "description": new_product.description
        }
    }), HTTP_201_CREATED



# Retrieve all products
@products.route('/products', methods=['GET'])
def get_all_products():
    products = Product.query.all()

    products_list = []
    for product in products:
        products_list.append({
            "id": product.id,
            "name": product.name,
            "price": product.price,
            "description": product.description
        })

    return jsonify({"products": products_list}), HTTP_200_OK 

# Update a product by ID
@products.route('/update/<int:id>', methods=['PUT'])
def update_product(id):
    try:
        data = request.get_json()
        product = Product.query.get(id)

        if not product:
            return jsonify({"error": "Product not found."}), 404

        product.name = data.get('name', product.name)
        product.price = data.get('price', product.price)
        product.description = data.get('description', product.description)

        db.session.commit()

        return jsonify({
            "message": f"Product with ID {id} updated successfully.",
            "product": {
                "id": product.id,
                "name": product.name,
                "price": product.price, 
                "description": product.description
            }
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Delete a product by ID
@products.route('/delete/<int:id>', methods=['DELETE'])
def delete_product(id):
    try:
        product = Product.query.get(id)

        if not product:
            return jsonify({"error": "Product not found."}), 404

        db.session.delete(product)
        db.session.commit()

        return jsonify({"message": f"Product with ID {id} deleted successfully."}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500