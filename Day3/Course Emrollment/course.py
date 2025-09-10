class Course:
    def __init__(self, name, code, credits, fee):
        self.name = name
        self.code = code
        self.credits = credits
        self.fee = fee

    def display_details(self):
        print(f"Course: {self.name} | Code: {self.code} | Credits: {self.credits} | Fee: ₹{self.fee}")
