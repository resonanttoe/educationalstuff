#Imports argv module from Sys library
from sys import argv

#assigns script and filename to argv[0,1] respectively
script, filename = argv

#assigns the txt variable the open file of argv[1]
txt = open(filename)

#prints the string with filename
print "Here's your file %r:" % filename
#prints the contents of txt variable
print txt.read()

#prints string
print "Type that filename again:"
#asks for filename as raw input assigns to file_again
file_again = raw_input("> ")

#txt again assigned to open of file_again.
txt_again = open(file_again)

#prints text file opened from another variable.
print txt_again.read()
txt.close()
txt_again.close()