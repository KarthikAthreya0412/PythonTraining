from config import get_connection
from mysql.connector import Error

def add_customer(name, email):
    try:
        conn=get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO customers (name, email) VALUES (%s, %s)", (name, email))
        conn.commit()
        print("Customer added successfully")
    except Error as e:
        raise ValueError(f"Error adding customer: {e}")
    finally:
        cursor.close()
        conn.close()

def view_order_history(customer_id):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT o.order_id, o.order_date, o.total_amount
            FROM orders o
            WHERE o.customer_id = %s
            ORDER BY o.order_date DESC
        """, (customer_id,))
        result = cursor.fetchall()
        if not result:
            raise ValueError("No order history found for this customer")
        return result
    except Error as e:
        raise ValueError(f"Error fetching order history: {e}")
    finally:
        cursor.close()
        conn.close()
