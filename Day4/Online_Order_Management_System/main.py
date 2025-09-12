from customers import add_customer, view_order_history
from products import add_product
from orders import place_order, generate_invoice, generate_sales_report
from datetime import date

# Add customers
add_customer("Harri", "harri@gmail.com")
add_customer("Kisan", "kisan@gmail.com")
view_order_history(1)

# Add products
add_product("Laptop", 55000, 10)
add_product("Mouse", 700, 50)

# Place order
items = [(1, 1), (2, 2)]  # (product_id, quantity)
order_id = place_order(1, items)

# Generate invoice
invoice = generate_invoice(order_id)
print(invoice)

# Generate sales report
report = generate_sales_report("2025-09-01", "2025-09-12")
print(report)
