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

# Classe para bateria
class Battery():
    def __init__(self, battery_size):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + " -kWh battery.")

       # Descobre qnt q dá pra andar com a bateria
    def get_range(self):
        range = int
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

# Classe do carro elétrico
class EletricCar(Car):
    def __init__ (self, make, model, year):
        # super chama os métodos do parent
        super().__init__(make, model, year)
        self.battery = Battery(int)

# Carro elétrico
my_leaf = EletricCar('nissan', 'leaf', '2025')
print(my_leaf.get_descriptive_name())
my_leaf_battery = Battery(70)
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()

print("")

# Carro antigo
tesla = EletricCar('elon molas', 'tesla', '20')
print(tesla.get_descriptive_name())
tesla_battery = Battery(85)
tesla.battery.describe_battery()
tesla.battery.get_range()