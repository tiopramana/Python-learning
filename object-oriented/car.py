class Car:

    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale 

    def drive(self):
        print(f"You driving an {self.model}")

    def stop(self):
        print(f"You stop driving an {self.model}")