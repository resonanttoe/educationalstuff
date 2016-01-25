# x is the variable of the string with a decimal number placed in the middle.
x = "There are %d types of people." % 10

#binary assignment to the string "binary"
binary = "binary"
#do_not assignment to the string "Don't"
do_not = "don't"
#y assignment to the string with the variables of binary and do_not used in the middle.
y = "Those who know %s and those who %s." % (binary, do_not)

#print the string of x as defined above
print x
#print the string of y as defined above
print y

#print the string I said followed by the string representation of x
print "I said: %r." % x
#print the string I also said followed by the string represemntation of y
print "I also said: %s'." % y

#declare hilarious to be false
hilarious = False
#declare joke_evaulation to the string below with a trailing string representation
joke_evaluation = "Isn't that joke so funny?! %r"

#print the variable joke_evalutation with the string representation of Hilarious. 
print joke_evaluation % hilarious

#declare w to be the string below
w = "This is the left of..."
#declare e to be to the string below
e = "A string with a right side."

#print the concatenation of w  and e.
print w + e