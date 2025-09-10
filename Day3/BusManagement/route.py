class Route:
    def __init__(self, route_name, start_location, end_location, stops=None):
        self.route_name = route_name
        self.start_location = start_location
        self.end_location = end_location
        self.stops = stops if stops else []

    def display_route(self):
        print(f"Route: {self.route_name}")
        print(f"From: {self.start_location} To: {self.end_location}")
        if self.stops:
            print("Stops:", ", ".join(self.stops))
