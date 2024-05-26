import sqlite3
from dotenv import load_dotenv
load_dotenv()
from src.config import Config

# Connect to the SQLite database
conn = sqlite3.connect(Config.DATABASE_NAME)
cur = conn.cursor()

# Read SQL commands from the file
with open('src/db/schema.sql', 'r') as file:
    sql_commands = file.read()
#aas
# Execute SQL commands
cur.executescript(sql_commands)

# Commit changes and close the connection
conn.commit()
cur.close()
