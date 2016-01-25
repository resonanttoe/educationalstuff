#number of cars
cars = 100
#number of occupant spance available in each car
space_in_a_car = 4
#number of drivers
drivers = 30
#number of passengers
passengers = 90
#Each car needs a driver, left over cars after all are filled with drivers
cars_not_driven = cars - drivers
#Number of cars actually driven
cars_driven = drivers
#The amount of space in a driven car for passengers (All seats filled)
carpool_capacity = cars_driven * space_in_a_car
#The amount of passengers uniformly distributed across the amount of cars driven
average_passengers_per_car = passengers / cars_driven

#print statements for all of the above.
print "There are", cars, "cars available"
print "There are only", drivers, "drivers available"
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."