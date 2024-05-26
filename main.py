from flask import Flask
from dotenv import load_dotenv
import logging

# Configure logging
logging.basicConfig(filename='/path/to/your/logfile.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

from src.utils.email import Email
from src.routes.auth_routes import auth_blueprint
from src.routes.lib_routes import lib_blueprint

load_dotenv()
app = Flask(__name__)

app.config.from_object('src.config.EmailConfig')
Email(app)
app.register_blueprint(auth_blueprint, url_prefix='/auth')
app.register_blueprint(lib_blueprint, url_prefix='/lib')

if __name__ == '__main__':
    app.run(debug=True)

