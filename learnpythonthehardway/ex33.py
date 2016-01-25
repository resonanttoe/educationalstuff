i = 0
j = 6
step = 2

def numbers(i,j,step):
	numbers = []
	for num in range(i, j):
		print "At the top i is %d" % num
		numbers.append(num)

		print "Numbers now: ", numbers
		print "At the bottom i is %d" % num 

print "The Numbers: ", numbers(i, j, step)

