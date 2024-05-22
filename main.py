from flask import Flask
from dotenv import load_dotenv

from src.utils.email import Email
from src.routes.auth_routes import auth_blueprint
from src.routes.lib_routes import lib_blueprint

load_dotenv()
app = Flask(__name__)

def create_app():
    app.config.from_object('src.config.EmailConfig')
    Email(app)
    register_blueprints()

def register_blueprints():
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    app.register_blueprint(lib_blueprint, url_prefix='/lib')

app.register_blueprint(lib_blueprint, url_prefix='/lib')

@app.route("/hi")
def hi():
    return "hi"

if __name__ == '__main__':
    create_app()
    app.run()
