from sys import argv

script = argv

#defines function that takes two arguments and outputs several print statements
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You ahve %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party"
	print "Get a blanket.\n"

print "We can just give the function umbers directly:"
#calls function with static assignments to arguments
cheese_and_crackers(20, 30)

print "OR, we can use variables from our script:"
#Variable assignments for the three function runs below
amount_of_cheese = 10
amount_of_crackers = 50

#calls function using above variable assignments as arguments
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math inside too:"
#Calls function with simple arthimetic for arguments (30 and 11)
cheese_and_crackers(10 + 20, 5 + 6)

print "And we can combine the two variables and math"
#Calls function with variables for each argument plus repsecitve numbers
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 40)

def magic_homework(exercisenum, emotinput):
	print "You are on exercise %s" % exercisenum
	print "You're feeling %s" % emotinput

emotinput = raw_input("How ya feelin'? ")
magic_homework(script, emotinput)
magic_homework(19, "Fine")


