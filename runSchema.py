# import sqlite3
from dotenv import load_dotenv
load_dotenv()
# from src.config import Config

# # Connect to the SQLite database
# conn = sqlite3.connect(Config.DATABASE_NAME)
# cur = conn.cursor()

# # Read SQL commands from the file
# with open('src/db/schema.sql', 'r') as file:
#     sql_commands = file.read()

# # Execute SQL commands
# cur.executescript(sql_commands)

# # Commit changes and close the connection
# conn.commit()
# cur.close()

import mysql.connector
from mysql.connector import Error
import os

# Assuming DBConfig and CustomException are defined correctly
from src.config import DBConfig
from src.utils.customError import CustomException

# Database configuration
db_config = {
    'user': DBConfig.DB_USER,
    'password': DBConfig.DB_PASS,
    'host': DBConfig.DB_HOST,  # RDS endpoint
    'database': DBConfig.DB_NAME,
    'raise_on_warnings': True
}

try:
    # Read SQL file
    sql_file_path = 'src/db/schema.sql'
    if not os.path.exists(sql_file_path):
        raise CustomException(f"SQL file not found: {sql_file_path}")

    with open(sql_file_path, 'r') as file:
        sql_script = file.read()

    # Connect to the database
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()

    # Execute the SQL script
    for result in cursor.execute(sql_script, multi=True):
        if result.with_rows:
            print(result.fetchall())

    # Commit the transaction
    connection.commit()

except FileNotFoundError as fnf_error:
    print(f"File not found error: {fnf_error}")
except mysql.connector.Error as db_error:
    print(f"Database error: {db_error}")
    raise CustomException(f"Database connection or execution failed: {db_error}")
except CustomException as custom_error:
    print(f"Custom error: {custom_error}")
except Exception as e:
    print(f"Unexpected error: {e}")
finally:
    # Close the connection
    if 'cursor' in locals() and cursor is not None:
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()
