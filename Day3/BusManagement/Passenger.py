class Passenger:
    def __init__(self, name, ticket_number, destination):
        self.name = name
        self.ticket_number = ticket_number
        self.destination = destination

    def display_details(self):
        print(f"Passenger Name: {self.name}")
        print(f"Ticket Number: {self.ticket_number}")
        print(f"Destination: {self.destination}")
