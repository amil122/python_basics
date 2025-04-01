
# class Car:
#     def __init__(self, make, model):
#         self.__make = make  # Private attribute
#         self.__model = model  # Private attribute
#         self.__fuel_level = 100  # Private attribute, initialized to full

#     def drive(self, distance):
#         fuel_needed = distance / 10  # Assuming 10 km per liter
#         if fuel_needed <= self.__fuel_level:
#             print(f"Driving {distance} km...")
#             self.__fuel_level -= fuel_needed
#         else:
#             print("Not enough fuel!")

#     def refuel(self, liters):
#         print(f"Refueling with {liters} liters...")
#         self.__fuel_level += liters

#     def get_fuel_level(self):
#         return self.__fuel_level

# # Creating an instance of the Car class
# my_car = Car(make="Toyota", model="Camry")

# # Trying to access private attributes directly would result in an AttributeError
# # print(my_car.__make)  # This would raise an AttributeError

# # Accessing attributes and methods through public interfaces
# print(f"Initial Fuel Level: {my_car.get_fuel_level()}%")
# my_car.drive(distance=50)
# print(f"Current Fuel Level: {my_car.get_fuel_level()}%")
# my_car.refuel(liters=20)
# print(f"New Fuel Level: {my_car.get_fuel_level()}%")
