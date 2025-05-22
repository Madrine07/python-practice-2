from flask import Flask
from app.extensions import db, migrate, jwt
from flask_bcrypt import Bcrypt
from app.controllers.products.products_controller import products

# Initialize Bcrypt outside the create_app function
bcrypt = Bcrypt()

def create_app():
    # Application factory function
    app = Flask(__name__)
    app.config.from_object('config.Config')
    
    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    
# Import models 
    from app.models.product import Product
   

    # Register blueprints
    app.register_blueprint(products)
   

    # Home route
    @app.route("/")
    def home():
        return "E Commerce API"

    return app