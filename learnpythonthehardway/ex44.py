class Parent(object):
	def implicit(self):
		print "Parent implicit()"

	def override(self):
			print "PARENT Override()"


class Child(Parent):
	def override(self):
		print "CHILD override()"


dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

the iterator will run forever on that one... and my function will similarly try to count the entire list