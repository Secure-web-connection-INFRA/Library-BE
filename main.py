from flask import Flask
from dotenv import load_dotenv
import os
from src.utils.email import Email
from src.routes.auth_routes import auth_blueprint
from src.routes.lib_routes import lib_blueprint
from flask_cors import CORS

load_dotenv()
app = Flask(__name__)
CORS(app,resources={r"/*": {"origins": ["http://ec2-3-25-55-200.ap-southeast-2.compute.amazonaws.com"]}})

app.config.from_object('src.config.EmailConfig')
Email(app)
app.register_blueprint(auth_blueprint, url_prefix='/auth')
app.register_blueprint(lib_blueprint, url_prefix='/lib')

if __name__ == '__main__':
    app.run(debug=True)

