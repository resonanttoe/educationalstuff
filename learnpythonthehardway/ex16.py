from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CRTL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the File..."
target = open(filename, 'w')

#print "Truncating the file. Goodbye!"
#target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("Line 1: ")
line2 = raw_input("Line 2: ")
line3 = raw_input("Line 3: ")

print "Writing to file"

target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")


print "And close"
target.close()