from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is: %s and you are %r " % (first, raw_input("Who are you?"))
print "Your second variable is:", second
print "Your third variable is:", third
