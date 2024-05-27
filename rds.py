import pymysql

# RDS settings
rds_host = "library-infra.c94kieyum4j6.ap-southeast-2.rds.amazonaws.com"
db_username = "library-infra"
db_password = "s4058455"
db_name = "library"
db_port = 3306

try:
    # Establish a connection to the RDS MySQL instance
    connection = pymysql.connect(
        host=rds_host,
        user=db_username,
        password=db_password,
        database=db_name,
        port=db_port
    )
    print("Connected to the database successfully!")
    
    # Create a cursor object
    cursor = connection.cursor()
    
    # Execute a sample query
    cursor.execute("SELECT DATABASE();")
    result = cursor.fetchone()
    print("Connected to database:", result)

    # Close the cursor and connection
    cursor.close()
    connection.close()
except pymysql.MySQLError as e:
    print("Error connecting to the database:", e)

