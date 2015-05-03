from __init__ import vector
import unittest

a = vector([2, 4, 7])
b = vector([3, 4, 0])
c = vector([0, 0, 0])
d = vector([])
e = vector([1, 2, 3, 4, 5])
i = vector([1, 0, 0])
j = vector([0, 1, 0])
k = vector([0, 0, 1])

# Constructor errors
class TestConstructor(unittest.TestCase):
	def test_constuctor_error(self):
		with self.assertRaises(TypeError):
			vector([[2, 3], [4, 5, 6]])	
		with self.assertRaises(ValueError):
			vector(['a','v','b'])	

# Sequence operations
class TestSequence(unittest.TestCase):
	def test_len(self):
		self.assertEqual(len(a), 3)

	def test_getitem(self):
		self.assertEqual(a[2], 7.0)

	def test_getitem_error(self):
		with self.assertRaises(TypeError):
			a['i']
		with self.assertRaises(IndexError):
			a[4]

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

# Binary operations
class TestBinary(unittest.TestCase):
	def test_addsub(self):
		self.assertEqual(b+a, vector([5, 8, 7]))
		self.assertEqual(b-a, vector([1, 0, -7]))
	
	def test_addsub_error(self):
		with self.assertRaises(TypeError):
			a+d
			a+e

	def test_muldiv(self):
		self.assertEqual(a*b, 22.0)
		self.assertEqual(a*0.9, vector([1.8, 3.6, 6.3]))
		self.assertEqual(0.9*a, vector([1.8, 3.6, 6.3]))
		self.assertEqual(a/2, vector([1, 2, 3.5]))

	def test_muldiv_error(self):
		with self.assertRaises(TypeError):
			a*'a'
			a*self
		with self.assertRaises(TypeError):
			a/'a'

	def test_crossprod(self):
		self.assertEqual(i%j, k)
		self.assertEqual(j%k, i)
		self.assertEqual(k%i, j)
		self.assertEqual(j%i, -k)
		self.assertEqual(k%j, -i)
		self.assertEqual(i%k, -j)

	def test_crossprod_error(self):
		with self.assertRaises(ValueError):
			a % d
			a % e

# Comparisons and boolean outputs
class TestBoolean(unittest.TestCase):
	def test_bool(self):
		self.assertFalse(c)
		self.assertFalse(d)
		self.assertTrue(a)

	def test_comparison(self):
		self.assertFalse(a==b)
		self.assertTrue(a!=b)
		self.assertTrue(a>b)
		self.assertFalse(a<b)
		self.assertTrue(b<=a)
		self.assertFalse(b>=a)
		self.assertTrue(not d)
		self.assertFalse(not a)

class TestNumPy(unittest.TestCase):
	def test_tonumpy(self):
		import numpy as np
		self.assertEqual(vector(a.tonumpy('float64')\
			- np.float64([2.0, 4.0, 7.0])), c)

	def test_tonumpy_error(self):
		with self.assertRaises(TypeError):
			a.tonumpy('random_dtype')

class TestNonNative(unittest.TestCase):
	def test_norm(self):
		self.assertEqual((3*i).norm(), i)
		self.assertEqual(abs(a.norm()), 1.0)
		self.assertEqual(a.norm().norm(), a.norm())

#--------------------------------------------------------------------------
# All test suits are called here
#--------------------------------------------------------------------------
suitefn = unittest.TestLoader().loadTestsFromTestCase
runfn = unittest.TextTestRunner(verbosity=2).run

runfn(suitefn(TestConstructor))
runfn(suitefn(TestSequence))
runfn(suitefn(TestUnary))
runfn(suitefn(TestBinary))
runfn(suitefn(TestBoolean))
runfn(suitefn(TestNumPy))
runfn(suitefn(TestNonNative))
