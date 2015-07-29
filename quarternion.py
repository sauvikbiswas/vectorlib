from vector import vector
class Q(vector):
	"""Quarternions are special kind of vectors. They are 4D arrays in
complex plane. They are special forms of vectors and are used in 
transformation"""

	# Constructor
	def __init__(self, listarr):
		try:
			if len(listarr) == 0:
				self.data = [0.0, 0.0, 0.0, 0.0]
			elif len(listarr) == 3:
				self.data = map(float, [0] + listarr)
			elif len(listarr) == 4:
				self.data = map(float, listarr)
			else:
				raise IndexError('A quarternion can initialised using three\
					(assumes constant coefficient of 0) / four values only')
		except ValueError:
			raise ValueError('Cannot obtain a float representation')
		except TypeError:
			raise TypeError('Only 1D sequences can be vectorised')

	# Display
	def __str__(self):
		"""str(Q-vectorobj) returns a string representation of the vector"""
		return 'Q-vector( '+' '.join(map(lambda x, y: x+y, \
			map('{:+}'.format, self.data), ['','i','j','k']))+' )'

	def __repr__(self):
		"""Same string representation. repr(Q-vectorobj) = \
			str(Q-vectorobj)"""
		return str(self)
	
	# Conjugates, inverse, etc.
	def conj(self):
		"""Returns a conjugate of the quarternion"""
		return Q([self.data[0]]+ map(lambda x: -1.0*x, self.data[1:]))

	def inv(self):
		"""Returns the inverse of the quarternion"""
		return Q(self.conj() / (abs(self)*abs(self)))

	# Unary Operators
	def __neg__(self):
		return Q(-vector(self.data))

	# Binary operations
	def __add__(self, other): # Wraps the data in Q()
		return Q(vector(self.data) + vector(other.data))

	def __sub__(self, other): # Wraps the data in Q()
		return Q(vector(self.data) - vector(other.data))

	def __mul__(self, other):
		"""Return the Hamiltonian product"""
		try:	
			if type(self) == type(other):
				r1 = self.data[0]
				r2 = other.data[0]
				v1 = vector(self.data[1:])
				v2 = vector(other.data[1:])
				rcomp = r1*r2 - v1*v2
				vcomp = r1*v2 + r2*v1 + (v1%v2)
				return Q([rcomp]+vcomp.data)
			else:
				return Q(vector(self.data) * other)
		except (TypeError, ValueError):
				raise TypeError('The data types cannot be multiplied')

	def __mod__(self, other): # Cross product has no meaning
		return NotImplemented

	# No numpy port without vectorising
	def tonumpy(self):
		return NotImplemented
