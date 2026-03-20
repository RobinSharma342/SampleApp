from flask import Flask
from app.routes.index_routes import home_bp
from app.routes.address_routes import address_bp
from app.routes.request_routes import request_bp

def create_app():
    app = Flask(__name__)

    app.register_blueprint(home_bp)
    app.register_blueprint(address_bp)
    app.register_blueprint(request_bp)



    return app