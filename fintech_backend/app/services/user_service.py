from ..models.user import User
from ..utils.database import db

def get_user(user_id):
    user = User.query.get(user_id)
    return user.to_dict() if user else None

def create_user(data):
    user = User(name=data['name'], email=data['email'], password_hash=data['password_hash'])
    db.session.add(user)
    db.session.commit()
    return user.to_dict()