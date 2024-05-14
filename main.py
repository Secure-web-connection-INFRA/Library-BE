import os
from flask import Flask

from src.routes.auth_routes import auth_blueprint
from src.routes.lib_routes import lib_blueprint
from src.db.config import queryDB

def create_app() -> Flask:
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.urandom(16)
    queryDB()
    register_blueprints(app)
    return app

def register_blueprints(app: Flask) -> None:
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    app.register_blueprint(lib_blueprint, url_prefix='/lib')

if __name__ == '__main__':
    app = create_app()
    app.run(host='127.0.0.1', port=5000, debug=True)
