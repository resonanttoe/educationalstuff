class LazyRules:
	rules_filename = 'plural4-rules.txt'


	def __init__(self):
		'''What runs at first time the class is called/instantiated.'''
		self.pattern_file = open(self.rules_filename)
		self.cache = []

	def __iter__(self):
		'''Clobber iter, replace with this.'''
		self.cache_index = 0
		return self


	def __next__(self):
		'''Clobber Next, replace with this.'''
		self.cache_index += 1
		if len(self.cache) >= self.cache_index:
			return self.cache[self.cache_index - 1]


		if self.pattern_file.closed:
			raise StopIteration

		line = self.pattern_file.readline()
		if not line:
			self.pattern_file.close()
			raise StopIteration
		pattern, search, replace = line.split(None, 3)
		funcs = build_match_and_apply_functions(
						pattern, search, replace)
		self.cache.append(funcs)
		return funcs


rules = LazyRules()