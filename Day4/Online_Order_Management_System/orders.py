from config import get_connection
from mysql.connector import Error

def place_order(customer_id, items):
    if not customer_id or not items:
        raise ValueError("insufficient data")

    try:
        conn = get_connection()
        cursor = conn.cursor()
        total_amount = 0.0

        cursor.execute(
            "INSERT INTO orders (customer_id, order_date, total_amount) VALUES (%s, NOW(), %s)",
            (customer_id, total_amount)
        )
        order_id = cursor.lastrowid

        for product_id, quantity in items:
            cursor.execute("SELECT price, stock FROM products WHERE product_id = %s", (product_id,))
            product = cursor.fetchone()
            if not product:
                raise ValueError(f"Invalid product ID: {product_id}")

            price, stock = product
            if stock < quantity:
                raise ValueError(f"Insufficient stock for product ID: {product_id}")

            item_price = price * quantity
            total_amount += item_price

            cursor.execute(
                "INSERT INTO order_items (order_id, product_id, quantity, item_price) VALUES (%s, %s, %s, %s)",
                (order_id, product_id, quantity, item_price)
            )

            cursor.execute(
                "UPDATE products SET stock = stock - %s WHERE product_id = %s",
                (quantity, product_id)
            )

        cursor.execute("UPDATE orders SET total_amount = %s WHERE order_id = %s", (total_amount, order_id))
        conn.commit()
        print(f"Order {order_id} placed successfully")
        return order_id

    except Error as e:
        raise ValueError(f"Error placing order: {e}")
    finally:
        cursor.close()
        conn.close()


def generate_invoice(order_id):
    if not order_id:
        raise ValueError("insufficient data")

    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT o.order_id, o.order_date, o.total_amount, c.name, c.email
            FROM orders o
            JOIN customers c ON o.customer_id = c.customer_id
            WHERE o.order_id = %s
        """, (order_id,))
        order = cursor.fetchone()
        if not order:
            raise ValueError(f"No order found with ID: {order_id}")

        cursor.execute("""
            SELECT p.product_name, oi.quantity, oi.item_price
            FROM order_items oi
            JOIN products p ON oi.product_id = p.product_id
            WHERE oi.order_id = %s
        """, (order_id,))
        items = cursor.fetchall()

        return {"order": order, "items": items}

    except Error as e:
        raise ValueError(f"Error generating invoice: {e}")
    finally:
        cursor.close()
        conn.close()


def generate_sales_report(start_date, end_date):
    if not start_date or not end_date:
        raise ValueError("Start date and end date are required")

    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT o.order_id, o.order_date, o.total_amount, c.name
            FROM orders o
            JOIN customers c ON o.customer_id = c.customer_id
            WHERE o.order_date BETWEEN %s AND %s
            ORDER BY o.order_date ASC
        """, (start_date, end_date))
        report = cursor.fetchall()
        if not report:
            raise ValueError("No sales found in the given date range")
        return report

    except Error as e:
        raise ValueError(f"Error generating sales report: {e}")
    finally:
        cursor.close()
        conn.close()
