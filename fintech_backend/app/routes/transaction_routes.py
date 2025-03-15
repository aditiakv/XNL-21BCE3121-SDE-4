# fintech_backend/app/routes/transaction_routes.py
from flask import Blueprint, jsonify, request
from ..services.transaction_service import (
    get_transaction,
    create_transaction,
    get_transactions_by_user,
    get_transactions_by_asset,
    delete_transaction
)

transaction_blueprint = Blueprint('transaction', __name__)

@transaction_blueprint.route('/transactions/<int:transaction_id>', methods=['GET'])
def get_transaction_route(transaction_id):
    transaction = get_transaction(transaction_id)
    if transaction:
        return jsonify(transaction)
    return jsonify({"error": "Transaction not found"}), 404

@transaction_blueprint.route('/transactions', methods=['POST'])
def create_transaction_route():
    data = request.get_json()
    try:
        transaction = create_transaction(data)
        return jsonify(transaction), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@transaction_blueprint.route('/users/<int:user_id>/transactions', methods=['GET'])
def get_transactions_by_user_route(user_id):
    transactions = get_transactions_by_user(user_id)
    return jsonify(transactions)

@transaction_blueprint.route('/assets/<int:asset_id>/transactions', methods=['GET'])
def get_transactions_by_asset_route(asset_id):
    transactions = get_transactions_by_asset(asset_id)
    return jsonify(transactions)

@transaction_blueprint.route('/transactions/<int:transaction_id>', methods=['DELETE'])
def delete_transaction_route(transaction_id):
    if delete_transaction(transaction_id):
        return jsonify({"message": "Transaction deleted"}), 200
    return jsonify({"error": "Transaction not found"}), 404