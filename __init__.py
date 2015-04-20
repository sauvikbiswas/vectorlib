# This code is undocumented.
# I will add some documentation to it later.
# There are a lot of builtins that have not been implemented.
# These will be assigned the Notimplemented onbject later.

class vector(object):

	# Data containers
	data = []
	__name__ = 'vector'

	# Constructor
	def __init__(self, listarr):
		try:
			self.data = map(float, listarr)
			return
		except ValueError:
			raise ValueError('Cannot obtain a float representation')

	# Sequence Operators
	def __getitem__(self, key):
		try:
			return self.data[key]
		except TypeError:
			raise TypeError('Index keys can only be of type \'int\'')
		except IndexError:
			IndexError('Index out of vector dimension')
	
	def __len__(self):
		return len(self.data)

	# Unary Operators
	def __str__(self):
		return 'vector( '+', '.join(map(str, self.data))+' )'

	def __repr__(self):
		return str(self)

	def __abs__(self):
		from math import sqrt
		return reduce(lambda x, y: sqrt(x**2 + y**2), self.data)

	def __float__(self):
		return self.__abs__()

	def __long__(self):
		return self.__abs__()

	def __neg__(self):
		return vector(map(lambda x: -x, self.data))		

	def __pos__(self):
		return self
		
	# Binary Operators
	def __add__(self, other):
		if type(other) == type(self):
			return vector(map(lambda x, y: x+y, self.data, other.data))
		else:
			raise TypeError('The data types cannot be added')

	def __sub__(self, other):
		return self + (- other)

	def __mul__(self, other):
		try:
			val = float(other)
			return vector([val*x for x in self.data])
		except ValueError:
			if type(self) == type(other):
				return reduce(lambda x, y: x+y, \
						map(lambda x, y: x*y, self.data, other.data))
			else:
				raise TypeError('The data types cannot be multiplied')

	def __rmul__(self, other):
		return self.__mul__(other)

	def __mod__(self, other):
		if type(self) == type(other) and self.__len__() == 3 \
				and other.__len__() == 3:
			u1, u2, u3 = self.data
			v1, v2, v3 = other.data
			return vector([(u2*v3 - u3*v3), (u3*v1 - u1*v3), \
					(u1*v2 - u2*v1)])
		else:
			raise ValueError('Cross product is defined for vectors of \
					length 3')

	def __div__(self, other):
		try:
			return self.__mul__((1.0 / other))
		except TypeError:
			raise TypeError('Inverse of '+ other.__repr__() + \
					' doesn\'t exist')


	# Comparators and boolean operators
	def __nonzero__(self):
		if self.__len__() > 0:
			if self.__float__() > 0.0:
				return True
		return False

	def __lt__(self, other):
		return self.__float__() < other.__float__()

	def __gt__(self, other):
		return self.__float__() > other.__float__()

	def __le__(self, other):
		return not self.__gt__(other)	

	def __ge__(self, other):
		return not self.__lt__(other)	

	def __eq__(self, other):
		if type(self) == type(other) and self.__len__() == other.__len__():
			return reduce(lambda x, y: x and y, \
				map(lambda x, y: x==y, self.data, other.data))
		else:
			return False

	def __ne__(self, other):
		return not self.__eq__(other)

	# Non native methods
	
	def norm(self):
		return self / abs(self)
		
