from config import get_connection
from mysql.connector import Error

def add_order_item(order_id, product_id, quantity, item_price):
    if not order_id or not product_id or not quantity or not item_price:
        raise ValueError("Insufficient data")

    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO order_items (order_id, product_id, quantity, item_price) VALUES (%s, %s, %s, %s)",
            (order_id, product_id, quantity, item_price)
        )
        conn.commit()
        print("Order item added successfully")
    except Error as e:
        raise ValueError(f"Error adding order item: {e}")
    finally:
        cursor.close()
        conn.close()


def get_order_items(order_id):
    if not order_id:
        raise ValueError("Order ID is required")

    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT oi.item_id, p.product_name, oi.quantity, oi.item_price
            FROM order_items oi
            JOIN products p ON oi.product_id = p.product_id
            WHERE oi.order_id = %s
        """, (order_id,))
        items = cursor.fetchall()
        if not items:
            raise ValueError(f"No items found for order ID: {order_id}")
        return items
    except Error as e:
        raise ValueError(f"Error fetching order items: {e}")
    finally:
        cursor.close()
        conn.close()


def delete_order_item(item_id):
    if not item_id:
        raise ValueError("Item ID is required")

    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM order_items WHERE item_id = %s", (item_id,))
        conn.commit()
        if cursor.rowcount == 0:
            raise ValueError(f"No order item found with ID: {item_id}")
        print("Order item deleted successfully")
    except Error as e:
        raise ValueError(f"Error deleting order item: {e}")
    finally:
        cursor.close()
        conn.close()
