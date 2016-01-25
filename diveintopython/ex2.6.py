def fib(n):
	print 'n =', n
	if n > 1:
		return n * fib(n - 1)
	else:
		print 'end of the line'
		return 1

def main():
	print fib(10)

if __name__ == '__main__':
  main()