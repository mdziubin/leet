class Car:
    def __init__(self, color, year, make) -> None:
        self.color = color
        self.year = year
        self.make = make

    def drive(self):
        """
        Drives the car
        """
        print("Driving")


car = Car("red", "2002", "Honda")
car.drive()
print(car)
