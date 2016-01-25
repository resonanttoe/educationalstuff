people = 300
cars = 1
trucks = 23


#when cars greater than people. Take cars, otherwise, don't, if equal, indecision.
if cars > people:
	print "We should take the cards."
elif cars < people:
	print "We should not take the cars."
else:
	print "We can't decide."

#When trucks is greater than cars, too many trucks, when not, suggest trucks, else indecision
if trucks > cars:
	print "That's too many trucks."
elif trucks < cars: 
	print "Maybe we could take the trucks."
else:
	print "We still can't decide."

#When people is greater than trucks or cars is less than trucks, Take trucks otherwise, stay home
if people > trucks or cars < trucks:
	print "Alright, let's just take the trucks."
else:
	print "Fine, let's stay home then."

""" 1. Elif does an El if statement. Failing the first condition, run another if conitional
		2. Stuff! (Shocker)
		3. Done
		"""