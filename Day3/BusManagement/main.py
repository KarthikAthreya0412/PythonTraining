from bus import Bus
from driver import Driver
from passenger import Passenger
from route import Route

driver1 = Driver("Ramesh", "D101", "LIC123")

route1 = Route("Adayar", "KK Nagar", "Anna Nagar", ["Chennai Central", "Broadway"])

bus101 = Bus("101", 40)
bus101.assign_driver(driver1)
bus101.assign_route(route1)

p1 = Passenger("Amar", "T001", "Chennai Central")
p2 = Passenger("Ram", "T002", "Broadway")
p3 = Passenger("Sankar", "T003", "Anna Nagar")

bus101.add_passenger(p1)
bus101.add_passenger(p2)
bus101.add_passenger(p3)

bus101.display_status()

bus101.remove_passenger("T001")  
bus101.remove_passenger("T002")  

print("\nTrip ended. Clearing passengers...")
bus101.passengers.clear()

bus101.display_status()
