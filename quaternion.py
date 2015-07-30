from vector import vector
class Q(vector):
	"""Quarternions are special kind of vectors. They are 4D arrays in
complex plane. They are special forms of vectors and are used in 
transformation"""

	def __rotation_matrix_to_Qvect__(self, rotmat):
		# There maybe a cleverer way to compute the Qvecs
		# This one is basic textbook method
		import math
		
		r11 = rotmat[0][0]
		r22 = rotmat[1][1]
		r33 = rotmat[2][2]

		r12 = rotmat[0][1]	
		r21 = rotmat[1][0]	
		
		r13 = rotmat[0][2]	
		r31 = rotmat[2][0]	
		
		r23 = rotmat[1][2]	
		r32 = rotmat[2][1]

		d = 1.0
		qvect = [0.0, 0.0, 0.0, 0.0]	
		
		if r22 > -r33 and r11 > -r22 and r11 > -r33:
			d = math.sqrt(1.0+r11+r22+r33)
			qvect = [d*d, r23-r32, r31-r13, r12-r21]
		elif r22 < -r33 and r11 > r22 and r11 > r33:
			d = math.sqrt(1.0+r11-r22-r33)
			qvect = [r23-r32, d*d, r12+r21, r13+r31]
		elif r22 > r33 and r11 < r22 and r11 < -r33:
			d = math.sqrt(1.0-r11+r22-r33)
			qvect = [r31-r13, r12+r21, d*d, r23+r32]
		elif r22 < r33 and r11 < -r22 and r11 < r33:
			d = math.sqrt(1.0-r11-r22+r33)
			qvect = [r12-r21, r31+r13, r23+r32, d*d]

		self.data = map(lambda x: x*d/2.0, qvect)
		return
			

	# Constructor
	def __init__(self, listarr):
		import numpy as np
		try:
			if type(listarr) == type(np.matrix([])) or \
					type(listarr) == type(np.array([])):
				rotmat = np.array(listarr)
				if rotmat.shape != (3, 3):
					raise IndexError('Rotation matrix must be 3x3 in size.')
				self.__rotation_matrix_to_Qvect__(rotmat)
			elif len(listarr) == 0:
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
		"""Returns the rotation matrix as numpy.array after norm"""
		import numpy as np
		qnorm = self.norm()
		q0, q1, q2, q3 = qnorm
		rotmat=[[q0*q0+q1*q1-q2*q2-q3*q3, 2*q1*q2-2*q0*q3, 2*q1*q3-2*q0*q2],
				[2*q1*q2-2*q0*q3, q0*q0-q1*q1+q2*q2-q3*q3, 2*q2*q3+2*q0*q1],
				[2*q1*q3+2*q0*q2, 2*q2*q3-2*q0*q1, q0*q0-q1*q1-q2*q2+q3*q3]]
		return np.array(rotmat)
