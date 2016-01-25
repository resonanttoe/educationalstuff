from sys import argv

script, file = argv

txt = open(file, 'r')
print txt.read()
txt.close()