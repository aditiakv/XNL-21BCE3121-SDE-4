from flask import Blueprint, jsonify, request
from ..services.user_service import get_user, create_user

user_blueprint = Blueprint('user', __name__)

@user_blueprint.route('/users/<int:user_id>', methods=['GET'])
def get_user_route(user_id):
    user = get_user(user_id)
    return jsonify(user)

@user_blueprint.route('/users', methods=['POST'])
def create_user_route():
    data = request.get_json()
    user = create_user(data)
    return jsonify(user), 201