# Class Definition
class Tools:
    def __init__(self, name="Jenkins", version=20, date="20/11", cartyres=4, car_name="Toyota"):
        self.car_list = []  # Initialize the car list
        self.name = name
        self.version = version
        self.date = date
        self.cartyres = cartyres
        self.car_name = car_name

    def check_and_add_car(self):
        """Check the number of tires and add car name to the list if applicable."""
        if self.cartyres == 4:
            self.car_list.append(self.car_name)
            print("Car list after adding:", self.car_list)
        else:
            print("Only two-wheelers are there.")

# Create an object of the Tools class
toyota = Tools()
toyota.check_and_add_car()
