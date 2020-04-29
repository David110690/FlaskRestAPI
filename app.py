from flask import Flask, jsonify
from flask import request
app = Flask(__name__)

from products import products

@app.route('/')
def ping():
    return jsonify({"message":"pong"})

@app.route("/products")
def getProducts():
    return jsonify({"products":products, "message": "Products List"})

@app.route("/products/<string:product_name>")
def getProduct(product_name):
    productsFound = [product for product in products if product['nombre'] == product_name]
    if (len(productsFound) > 0):
        return jsonify({"product": productsFound})
    return jsonify({"mensage": "producto no encontrado"})


@app.route("/products", methods=["POST"])
def addProduct():
    new_product = {
        "nombre" : request.json["nombre"],
        "precio": request.json["precio"],
        "cantidad": request.json["cantidad"]
    }
    products.append(new_product)

    return jsonify({"message": "producto agregado", "productos":products})


@app.route("/products/<string:product_name>", methods=["PUT"])
def editProduct(product_name):
    productsFound = [product for product in products if product['nombre'] == product_name]
    if (len(productsFound) > 0):
        productsFound[0]["nombre"]=request.json["nombre"]
        productsFound[0]["precio"]=request.json["precio"]
        productsFound[0]["cantidad"]=request.json["cantidad"]
        return jsonify({"mensage": "producto actualizado", "product": productsFound[0]})
    return jsonify({"mensage": "producto no encontrado"})

@app.route("/products/<string:product_name>", methods=["DELETE"])
def deliteProduct(product_name):
    productsFound = [product for product in products if product['nombre'] == product_name]
    if (len(productsFound) > 0):
        products.remove(productsFound[0])
        return jsonify({"mensage": "producto eliminado", "products": products})
    return jsonify({"mensage": "producto no encontrado"})


if __name__ == '__main__':
    app.run(debug=True)