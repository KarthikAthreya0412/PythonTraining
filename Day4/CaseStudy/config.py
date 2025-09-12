import mysql.connector
 
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Hexaware@123",
        database="db_example"
    )