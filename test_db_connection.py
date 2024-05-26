import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os
import logging
# Load environment variables from .env file
load_dotenv()

# Database configuration
db_config = {
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASS'),
    'host': os.getenv('DB_HOST'),  # RDS endpoint
    'database': os.getenv('DB_NAME'),
    'raise_on_warnings': True
}

try:
    # Connect to the database
    connection = mysql.connector.connect(**db_config)
    if connection.is_connected():
        logging.info("Successfully connected to the database")
        db_info = connection.get_server_info()
        logging.info("MySQL server version:", db_info)
        cursor = connection.cursor()
        cursor.execute("SELECT DATABASE();")
        record = cursor.fetchone()
        logging.info("Connected to database:", record)
    else:
        logging.info("Failed to connect to the database")

except Error as e:
    logging.info(f"Error while connecting to MySQL: {e}")

finally:
    if 'cursor' in locals() and cursor is not None:
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        logging.info("MySQL connection is closed")

