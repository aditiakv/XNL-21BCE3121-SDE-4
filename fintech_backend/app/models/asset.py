from ..utils.database import db

class Asset(db.Model):
    __tablename__ = 'assets'
    asset_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    symbol = db.Column(db.String(10), unique=True, nullable=False)
    price = db.Column(db.Numeric(10, 2), nullable=False)
    market_cap = db.Column(db.Numeric(15, 2), nullable=False)
    transactions = db.relationship('Transaction', backref='asset', lazy=True)

    def to_dict(self):
        return {
            'asset_id': self.asset_id,
            'name': self.name,
            'symbol': self.symbol,
            'price': float(self.price),
            'market_cap': float(self.market_cap)
        }