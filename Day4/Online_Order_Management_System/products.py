from config import get_connection
from mysql.connector import Error

def add_product(name, price, stock):
    if not name or price is None or stock is None:
        raise ValueError("insufficient data")

    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO products (product_name, price, stock) VALUES (%s, %s, %s)",
            (name, price, stock),
        )
        conn.commit()
        print("Product added successfully")
    except Error as e:
        raise ValueError(f"Error adding product: {e}")
    finally:
        cursor.close()
        conn.close()
