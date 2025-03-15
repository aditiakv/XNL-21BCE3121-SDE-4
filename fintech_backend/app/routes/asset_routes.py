from flask import Blueprint, jsonify
from ..models.asset import Asset

# Define the blueprint
asset_blueprint = Blueprint('asset', __name__)

# Define your routes here
@asset_blueprint.route('/assets', methods=['GET'])
def get_assets():
    assets = Asset.query.all()
    return jsonify([asset.to_dict() for asset in assets]), 200

@asset_blueprint.route('/assets/<int:asset_id>', methods=['GET'])
def get_asset(asset_id):
    asset = Asset.query.get(asset_id)
    if asset:
        return jsonify(asset.to_dict()), 200
    return jsonify({"error": "Asset not found"}), 404