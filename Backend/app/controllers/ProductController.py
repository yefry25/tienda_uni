from flask import Blueprint, request, jsonify

bp = Blueprint('ProductController', __name__)

@bp.route('/addProduct', methods=['POST'])
def addProduct():
    from app.Services.ProductService import CreateProduct
    data = request.json
    result, statusCode = CreateProduct(data)
    return jsonify(result), statusCode

@bp.route('/deleteProduct/<int:id>', methods=["DELETE"])
def deleteProduct(id):
    from app.Services.ProductService import DeleteProduct
    result, statusCode = DeleteProduct(id)
    return jsonify(result), statusCode

@bp.route('/products', methods=["GET"])
def GetProducts():
    from app.Services.ProductService import GetProducts
    result, statusCode = GetProducts()
    return jsonify(result), statusCode

@bp.route('/getProductById/<int:id>', methods=['GET'])
def getById(id):
    from app.Services.ProductService import GetProductById
    result, statusCode = GetProductById(id)
    return jsonify(result), statusCode

@bp.route('/updateProduct/<int:id>', methods=['PUT'])
def updateProduct(id):
    from app.Services.ProductService import UpdateProduct
    data = request.json

    result, statusCode = UpdateProduct(id, data)
    return jsonify(result), statusCode