from __init__ import vector, Q
# vectors can be of any length. They must be constructed using a sequence.
# For our ease, we will use 3D vectors only.

a = vector([2, 4, 7])		# Data stored as float

# Sequence operations
print len(a)				# Should give the vector dim	
print a[2]					# Should give us the 3rd coeff
print list(a)				# Uses the iterator generator

# Unary operations
print a						# Calls repr
print str(a)				# Same as repr
print float(a)				# Magnitude of vector
print abs(a)				# Same as float, long(a) would be same
print +a					# Calls pos
print -a					# Calls neg

b = vector([3, 4, 0])

# Binary operations
print b + a					# Calls add
print b - a					# Calls sub
print a * b					# Calls mul, computes a dot product
print a * 0.9				# Calls mul, scales the vetor
print 0.9 * a				# Calls rmul to override the float's mul def
print a / 0.9				# Calls div
print a % b					# Calls mod, computes a cross product

c = vector([0, 0, 0])
d = vector([])
# Comparisons and boolean outputs
print bool(c), bool(d)		# Calls nonzero, False for 0D and 0 mag vectors
print bool(a)
print a > b					# Calls gt. Only mag compared. Others similar.
print a == b				# Calls eq. True only if all coeffs are same

x = a.tonumpy('float32')
print x	            		# x is a numpy object
print vector(x)	            # You can use numpy 1D arrays to construct a vector

# Quarternions
q0 = Q([2,3,4])				# Real part 0
print q0

q1 = Q([1,2,3,4])			# Q using 4 floatable values
print q1
print +q1
print -q1
print q1.conj()				# Conjugate
print q1.inv()				# Inverse

q2 = Q([4,6,7,8])
print q1 * q2
print q1 * 9
print 9 * q1
print q1 / 8
print vector(q1)
print q1.norm()
