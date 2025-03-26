class Car:
    total_car = 0

    def __init__(self, brand, model):
        self.__brand = brand  # __ jab do underscore use karte hai variable name k pehle iska matlab hai oh variable private hai and iss class k bhar uss variable ko access nhi karsakte. __brand direct access nhi karsakte but iss class me ek method bana k usko iss class k bhar access karsakte hai

        self.__model = model
        Car.total_car += 1

        # self represents the current object.  It allows access to instance variables and methods. Every method inside a class must have self as the first parameter (except static methods).

    def get_brand(self):
        return self.__brand + " !"

    def full_name(self):
        return f"{self.__brand} {self.__model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
    @staticmethod
    def general_description():
        return "Cars are means of transport"
    
    @property
    def model(self):
        return self.__model
    # The @property decorator in Python converts a method into a read-only attribute, allowing access like a variable instead of a method call. It is commonly used for encapsulation to control attribute access.
    
# Python (self): Explicitly passes the instance as the first argument (self) in instance methods.
# Java/C++ (this): Implicitly refers to the current instance inside the class, without needing to pass it as an argument.
# A staticmethod in Python is a method that belongs to a class but doesn’t access or modify instance (self) or class (cls) attributes.    Can be called using the class name without creating an object.    Useful for utility/helper functions related to the class.

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)  # Car class k constructor yani __init__ se brand and model leke aao
        self.battery_size = battery_size

    def fuel_type():
        return "Electric charge"


# my_tesla = ElectricCar("Tesla", "Model S", "85kWh")

# print(isinstance(my_tesla, Car))
# print(isinstance(my_tesla, ElectricCar))

# print(my_tesla.__brand)
# print(my_tesla.fuel_type())

# my_car = Car("Tata", "Safari")
# my_car.model = "City"
# Car("Tata", "Nexon")


# print(my_car.general_description())
# print(my_car.model)


# my_car = Car("Toyota", "Corolla")
# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name())

# my_new_car = Car("Tata", "Safari")
# print(my_new_car.model)



class Battery:
    def battery_info(self):
        return "this is battery"

class Engine:
    def engine_info(self):
        return "This is engine"

class ElectricCarTwo(Battery, Engine, Car):
    pass

my_new_tesla = ElectricCarTwo("Tesla", "Model S")
print(my_new_tesla.engine_info())
print(my_new_tesla.battery_info())