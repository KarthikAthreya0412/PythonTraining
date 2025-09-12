import inspect
import customers
import products
import orders
import order_items

# ---------------- Customers Tests ----------------
def test_add_customer_query():
    expected_query = "INSERT INTO customers (name, email) VALUES (%s, %s)"
    actual_query = inspect.getsource(customers.add_customer)
    assert expected_query in actual_query

def test_add_customer_signature():
    sig = inspect.signature(customers.add_customer)
    assert list(sig.parameters.keys()) == ["name", "email"]

def test_view_order_history_query():
    expected_query = "SELECT o.order_id, o.order_date, o.total_amount"
    actual_query = inspect.getsource(customers.view_order_history)
    assert expected_query in actual_query

def test_view_order_history_signature():
    sig = inspect.signature(customers.view_order_history)
    assert list(sig.parameters.keys()) == ["customer_id"]

# ---------------- Products Tests ----------------
def test_add_product_query():
    expected_query = "INSERT INTO products (product_name, price, stock) VALUES (%s, %s, %s)"
    actual_query = inspect.getsource(products.add_product)
    assert expected_query in actual_query

def test_add_product_signature():
    sig = inspect.signature(products.add_product)
    assert list(sig.parameters.keys()) == ["name", "price", "stock"]

# ---------------- Orders Tests ----------------
def test_add_order_query():
    expected_query = "INSERT INTO orders (customer_id, order_date, total_amount) VALUES (%s, %s, %s)"
    actual_query = inspect.getsource(orders.add_order)
    assert expected_query in actual_query

def test_add_order_signature():
    sig = inspect.signature(orders.add_order)
    assert list(sig.parameters.keys()) == ["customer_id", "order_date", "total_amount"]

# ---------------- Order Items Tests ----------------
def test_add_order_item_query():
    expected_query = "INSERT INTO order_items (order_id, product_id, quantity) VALUES (%s, %s, %s)"
    actual_query = inspect.getsource(order_items.add_order_item)
    assert expected_query in actual_query

def test_add_order_item_signature():
    sig = inspect.signature(order_items.add_order_item)
    assert list(sig.parameters.keys()) == ["order_id", "product_id", "quantity"]
