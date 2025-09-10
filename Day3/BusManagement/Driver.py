class Driver:
    def __init__(self, name, employee_id, license_number):
        self.name = name
        self.employee_id = employee_id
        self.license_number = license_number
        self.assigned_bus = None

    def display_details(self):
        print(f"Driver Name: {self.name}")
        print(f"Employee ID: {self.employee_id}")
        print(f"License Number: {self.license_number}")
        if self.assigned_bus:
            print(f"Assigned Bus: {self.assigned_bus}")
        else:
            print("No bus assigned")

    def assign_to_bus(self, bus_number):
        self.assigned_bus = bus_number
