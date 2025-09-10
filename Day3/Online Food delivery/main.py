from food_item import FoodItem
from user import User
from premium_user import PremiumUser

pizza = FoodItem("Pizza", 250)
burger = FoodItem("Burger", 150)
briyani = FoodItem("Briyani", 200, available=False)
fries = FoodItem("Fries", 100)

h = User("Karthik")
k = PremiumUser("Athreya")

h.order.add_item(pizza)
h.order.add_item(burger)
h.order.add_item(briyani)
h.order.display_order()
h.display_total()

print("\n---\n")

k.order.add_item(pizza)
k.order.add_item(fries)
k.order.remove_item("Fries")
k.order.display_order()
k.display_total()
