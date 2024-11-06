from flask import Blueprint, jsonify

bp = Blueprint('CommonController', __name__)

@bp.route('/getCategories', methods=['GET'])
def GetCategories():
    from app.Services.CommonService import GetCategories

    result, statusCode = GetCategories()
    return jsonify(result), statusCode

@bp.route('/getBrands', methods=['GET'])
def GetBrands():
    from app.Services.CommonService import GetBrands

    result, statusCode = GetBrands()
    return jsonify(result), statusCode