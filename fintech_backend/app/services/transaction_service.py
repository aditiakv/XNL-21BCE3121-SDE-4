# fintech_backend/app/services/transaction_service.py
from ..models.transaction import Transaction
from ..models.user import User
from ..models.asset import Asset
from ..utils.database import db

def get_transaction(transaction_id):
    """
    Retrieve a transaction by its ID.
    """
    transaction = Transaction.query.get(transaction_id)
    return transaction.to_dict() if transaction else None

def create_transaction(data):
    """
    Create a new transaction.
    """
    user_id = data.get('user_id')
    asset_id = data.get('asset_id')
    amount = data.get('amount')
    type = data.get('type')
    timestamp = data.get('timestamp')

    # Check if the user and asset exist
    user = User.query.get(user_id)
    asset = Asset.query.get(asset_id)

    if not user:
        raise ValueError(f"User with ID {user_id} does not exist.")
    if not asset:
        raise ValueError(f"Asset with ID {asset_id} does not exist.")

    # Create the transaction
    transaction = Transaction(
        user_id=user_id,
        asset_id=asset_id,
        amount=amount,
        type=type,
        timestamp=timestamp
    )

    # Add and commit the transaction to the database
    db.session.add(transaction)
    db.session.commit()

    return transaction.to_dict()

def get_transactions_by_user(user_id):
    """
    Retrieve all transactions for a specific user.
    """
    transactions = Transaction.query.filter_by(user_id=user_id).all()
    return [transaction.to_dict() for transaction in transactions]

def get_transactions_by_asset(asset_id):
    """
    Retrieve all transactions for a specific asset.
    """
    transactions = Transaction.query.filter_by(asset_id=asset_id).all()
    return [transaction.to_dict() for transaction in transactions]

def delete_transaction(transaction_id):
    """
    Delete a transaction by its ID.
    """
    transaction = Transaction.query.get(transaction_id)
    if transaction:
        db.session.delete(transaction)
        db.session.commit()
        return True
    return False