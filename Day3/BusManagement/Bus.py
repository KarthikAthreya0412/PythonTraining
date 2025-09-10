class Bus:
    def __init__(self, bus_number, capacity):
        self.bus_number = bus_number
        self.capacity = capacity
        self.driver = None
        self.passengers = []

    def assign_driver(self, driver_name):
        self.driver = driver_name

    def add_passenger(self, passenger_name):
        if len(self.passengers) < self.capacity:
            self.passengers.append(passenger_name)
        else:
            print("Cannot add passenger. Bus is full.")

    def remove_passenger(self, passenger_name):
        if passenger_name in self.passengers:
            self.passengers.remove(passenger_name)
        else:
            print("Passenger not found on the bus.")

    def display_status(self):
        print(f"Bus Number: {self.bus_number}")
        print(f"Driver: {self.driver if self.driver else 'No driver assigned'}")
        print(f"Passengers Count: {len(self.passengers)}")
        print("Passenger List:", ", ".join(self.passengers) if self.passengers else "No passengers")
