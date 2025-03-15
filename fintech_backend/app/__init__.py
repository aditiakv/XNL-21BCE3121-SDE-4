# fintech_backend/app/__init__.py
from flask import Flask
from flask_migrate import Migrate
from .utils.database import db  # Import db from database.py

# Initialize Flask-Migrate
migrate = Migrate()

def create_app():
    # Create the Flask app
    app = Flask(__name__)

    # Load configuration from config.py
    app.config.from_object('fintech_backend.config.Config')

    # Initialize extensions with the app
    db.init_app(app)
    migrate.init_app(app, db)

    # Register blueprints (routes)
    from .routes.user_routes import user_blueprint
    from .routes.transaction_routes import transaction_blueprint
    from .routes.asset_routes import asset_blueprint

    app.register_blueprint(user_blueprint)
    app.register_blueprint(transaction_blueprint)
    app.register_blueprint(asset_blueprint)

    return app