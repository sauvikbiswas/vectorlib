__author__ = 'Sauvik Biswas'
__revision__  = '1'
__rel_status__ = 'dev'
__version__ = '1.0.%s-%s' % (__revision__, __rel_status__)
__licence__ = 'MIT'
__email__   = 'sauvik.biswas@gmail.com'
__desc__    = 'Vector operations in nD space but primarily for usage in \
				3D space.'

class vector(object):
	"""Vector objects are essentially 1D arrays. Most native operations on
vectors can be performed using simple Python native syntax. Operators 
can handle vectors of n dimensions (except for cross product)."""

	# Data containers
	__name__ = 'vector'

	# Constructor & Destructor
	def __init__(self, listarr):
		try:
			self.data = map(float, listarr)
			return
		except ValueError:
			raise ValueError('Cannot obtain a float representation')

	def __del__(self):
		try:
			del(self.data)
		except NameError:
			raise NameError('Data not defined in this vector object')

	# Sequence Operators
	def __getitem__(self, key):
		"""vectorobj[i] returns the coefficient of the (i+1)th dimension"""
		try:
			return self.data[key]
		except TypeError:
			raise TypeError('Index keys can only be of type \'int\'')
		except IndexError:
			raise IndexError('Index out of vector dimension')
	
	def __len__(self):
		"""len(vectorobj) returns the dimension of the vector"""
		return len(self.data)

	def __iter__(self):
		"""Iterator object for iterating through the data"""
		for coeff in self.data:
			yield coeff

	# Unary Operators
	def __str__(self):
		"""str(vectorobj) returns a string representation of the vector"""
		return 'vector( '+', '.join(map(str, self.data))+' )'

	def __repr__(self):
		"""Same string representation. repr(vectorobj) = str(vectorobj)"""
		return str(self)

	def __abs__(self):
		"""abs(vectorobj) returns the magnitude of the vector"""
		from math import sqrt
		return reduce(lambda x, y: sqrt(x**2 + y**2), self.data)

	def __float__(self):
		"""Returns the magnitude. float(vectorobj) = abs(vectorobj)"""
		return self.__abs__()

	def __long__(self):
		"""Returns the magnitude. long(vectorobj) = abs(vectorobj)"""
		return self.__abs__()

	def __neg__(self):
		"""-vectorobj returns a vector pointing in the opposite direction"""
		return vector(map(lambda x: -x, self.data))		

	def __pos__(self):
		"""+vectorobj returns itself"""
		return self
		
	# Binary Operators
	def __add__(self, other):
		"""vectorobj + vectorobj returns a vectorobj"""
		if type(other) == type(self):
			return vector(map(lambda x, y: x+y, self.data, other.data))
		else:
			raise TypeError('The data types cannot be added')

	def __sub__(self, other):
		"""vectorobj - vectorobj returns a vectorobj"""
		return self + (- other)

	def __mul__(self, other):
		"""vectorobj * vectorobj returns their dot product (float).
vecorobj * float(obj) returns a scaled vector object otherwise"""
		try:
			if type(self) == type(other):
				return reduce(lambda x, y: x+y, \
						map(lambda x, y: x*y, self.data, other.data))
			else:
				val = float(other)
				return vector([val*x for x in self.data])
		except (TypeError, ValueError):
				raise TypeError('The data types cannot be multiplied')

	def __rmul__(self, other):
		"""Implementation of float(obj) * vectorobj"""
		return self.__mul__(other)

	def __mod__(self, other):
		"""vectorobj % vectorobj return the cross product. The dimension
of the vectors must be 3"""
		if type(self) == type(other) and self.__len__() == 3 \
				and other.__len__() == 3:
			u1, u2, u3 = self.data
			v1, v2, v3 = other.data
			return vector([(u2*v3 - u3*v2), (u3*v1 - u1*v3), \
					(u1*v2 - u2*v1)])
		else:
			raise ValueError('Cross product is defined for vectors of \
					length 3')

	def __div__(self, other):
		"""vectorobj / float(obj) scales down the vector"""
		try:
			return self.__mul__((1.0 / other))
		except TypeError:
			raise TypeError('Inverse of '+ other.__repr__() + \
					' doesn\'t exist')


	# Comparators and boolean operators
	"""bool(vectorobj) is 0 if the vector is of 0 dimension or 
is of 0 length"""
	def __nonzero__(self):
		if self.__len__() > 0:
			if self.__float__() > 0.0:
				return True
		return False

	def __lt__(self, other):
		"""vectorobj < vectorobj compares their magnitude"""
		return self.__float__() < other.__float__()

	def __gt__(self, other):
		"""vectorobj > vectorobj compares their magnitude"""
		return self.__float__() > other.__float__()

	def __le__(self, other):
		"""vectorobj <= vectorobj compares their magnitude"""
		return not self.__gt__(other)	

	def __ge__(self, other):
		"""vectorobj >= vectorobj compares their magnitude"""
		return not self.__lt__(other)	

	def __eq__(self, other):
		"""vectorobj == vectorobj compares their exact coefficients"""
		if type(self) == type(other) and self.__len__() == other.__len__():
			return reduce(lambda x, y: x and y, \
				map(lambda x, y: x==y, self.data, other.data))
		else:
			return False

	def __ne__(self, other):
		"""vectorobj != vectorobj compares their exact coefficients"""
		return not self.__eq__(other)

	# Not implemented / not applicable

	__hash__ = None

	# Non native methods
	
	def norm(self):
		"""vectorobj.norm() returns a vector of unit length"""
		return self / abs(self)
	
	# Numpy methods
	
	def tonumpy(self, dtype):
		"""vectorobj.tonumpy('float64') returns a numpy array with dtype =
'float64'. The 'float32' and 'float_' dtypes are also supported""" 
		import numpy as np
		if dtype=='float32' or dtype=='float64' or dtype=='float_':
			return getattr(np, dtype)(self.data)
		else:
			raise TypeError('numpy:dtype can be of float32,\
				float64 or float_')

