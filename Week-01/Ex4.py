# No of cars
cars = 100

# No of spaces in the car
space_in_a_car = 4.0

# No of drivers
drivers = 30

# No of passengers
passengers = 90

# No of cars not driven
cars_not_driven = cars - drivers

# No of cars driven
cars_driven = drivers

# No carpool capacity
carpool_capacity = cars_driven * space_in_a_car

# no of average passengesr per car
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")