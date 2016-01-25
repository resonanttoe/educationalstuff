### Animal is-a object
class Animal(object):
	pass

### Dog is-a animal
class Dog(Animal):
	def __init__(self, name):
	### Dog has-a name
	self.name = name

### Cat is-a animal
class Cat(Animal):
	def __init__(self, name):
		### Cat has-a name
		self.name = name

### Person is-a object
class Person(object):
	def __init__(self, name):
	### Person has-a name
	self.name = name

	### Person has-a pet
	self.pet = None


### Employee is-a person
class employee(Person):
	def __init(self, name, salary):
		###Person has a name and salary
		super(Employee, self).__init__(name)
		##Super person has a salary too
		self.salary = salary

### Fish is-a object
class Fish(object):
	pass

### Salmon is-a fish
class Salmon(Fish):
	pass

### Halibut is-a fish
class Halibut(Fish):
	pass

### rover is-a Dog
rover = Dog("Rover")

### Satan is-a cat
satan = Cat("Satan")

### Mary is-a person
mary = Person("Mary")

### Mary has-a pet, satan
mary.pet = satan

### Frank is-a employee with a salary of 120000
frank = Employee("Frank", 120000)

### Frank has-a pet, rover
frank.pet = rover

### Flipper is a Fish
flipper = Fish()

### crouse is a Salmon
crouse = Salmon()

### Harry is a Halibut
harry Halibut()