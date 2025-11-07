class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

# Hodometro quando chegou na loja
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You cant roll the odometer back!")

# Hodometro depois de eu sair dirigindo
    def increment_odometer(self, miles):
        self.odometer_reading += miles

class EletricCar(Car):

    def __init__ (self, make, model, year):
        # super chama os métodos do parent
        super().__init__(make, model, year)
        self.battery_size=40

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-mk/h battery. ")

# Carro elétrico
my_leaf = EletricCar('nissan', 'leaf', '2025')
print(my_leaf.get_descriptive_name())
my_leaf.describe_battery()

print("")

# Carro antigo
my_used_car = Car("Subaru", "Outback", 2016)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500)
my_used_car.increment_odometer(100)
my_used_car.read_odometer()