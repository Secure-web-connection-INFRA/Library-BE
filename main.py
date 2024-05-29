
from flask import Flask
from dotenv import load_dotenv
from flask_cors import CORS

from src.config import Config
from src.utils.email import Email
from src.routes.auth_routes import auth_blueprint
from src.routes.lib_routes import lib_blueprint


load_dotenv()
app = Flask(__name__)

CORS(app,methods=["GET", "POST", "PUT"],supports_credentials=True,allow_headers=["Authorization", "Content-Type"],resources={
    r"/*": {
        "origins": ["http://localhost:3000", Config.BASEURL],
    }})

app.config.from_object('src.config.EmailConfig')
Email(app)

app.register_blueprint(auth_blueprint, url_prefix='/auth')
app.register_blueprint(lib_blueprint, url_prefix='/lib')

if __name__ == '__main__':
    app.run(debug=True)

