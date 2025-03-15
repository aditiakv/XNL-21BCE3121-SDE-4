# fintech_backend/app/models/transaction.py
from datetime import datetime
from ..utils.database import db

class Transaction(db.Model):
    __tablename__ = 'transactions'
    transaction_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    asset_id = db.Column(db.Integer, db.ForeignKey('assets.asset_id'), nullable=False)
    amount = db.Column(db.Numeric(10, 2), nullable=False)
    type = db.Column(db.String(10), nullable=False)  # 'buy' or 'sell'
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    def to_dict(self):
        return {
            'transaction_id': self.transaction_id,
            'user_id': self.user_id,
            'asset_id': self.asset_id,
            'amount': float(self.amount),  # Convert Decimal to float for JSON serialization
            'type': self.type,
            'timestamp': self.timestamp.isoformat()
        }