from __init__ import vector
import unittest

a = vector([2, 4, 7])		# Data stored as float

# Sequence operations
class TestSequence(unittest.TestCase):
	def test_len(self):
		self.assertEqual(len(a), 3)

	def test_getitem(self):
		self.assertEqual(a[2], 7.0)

	def test_iterator(self):
		self.assertEqual(list(a), [2.0, 4.0, 7.0])

# Unary operations
class TestUnary(unittest.TestCase):
	def test_reprstr(self):
		self.assertEqual(repr(a), 'vector( 2.0, 4.0, 7.0 )')
		self.assertEqual(str(a), 'vector( 2.0, 4.0, 7.0 )')

	def test_floatabs(self):
		import math
		mag = math.sqrt(2.0**2+4.0**2+7.0**2)
		self.assertEqual(float(a), mag)
		self.assertEqual(abs(a), mag)

	def test_posneg(self):
		self.assertEqual(+a, a)
		self.assertEqual(-(-a), a)

suite = unittest.TestLoader().loadTestsFromTestCase(TestSequence)
unittest.TextTestRunner(verbosity=2).run(suite)

suite = unittest.TestLoader().loadTestsFromTestCase(TestUnary)
unittest.TextTestRunner(verbosity=2).run(suite)

#------------------------------ Will convert this in next commit.
#------------------------------ Exception handling needs to be unittested.

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
