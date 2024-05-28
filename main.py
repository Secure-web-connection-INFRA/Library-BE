from flask import Flask
from dotenv import load_dotenv
import os
from src.utils.email import Email
from src.routes.auth_routes import auth_blueprint
from src.routes.lib_routes import lib_blueprint
from flask_cors import CORS

load_dotenv()
app = Flask(__name__)
# CORS(app,resources={r"/*": {"origins": ["http://localhost:3000/"]}})
#CORS(app)

#CORS(auth_blueprint)
#CORS(lib_blueprint)
#CORS(app, resources={r"/*": {"origins": "*"}})

# Apply CORS to specific blueprints if needed
CORS(auth_blueprint, resources={r"/auth/*": {"origins": "*"}})
CORS(lib_blueprint, resources={r"/lib/*": {"origins": "*"}})

app.config.from_object('src.config.EmailConfig')
Email(app)
app.register_blueprint(auth_blueprint, url_prefix='/auth')
app.register_blueprint(lib_blueprint, url_prefix='/lib')

if __name__ == '__main__':
    app.run(debug=True)

