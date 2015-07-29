from __init__ import Q
import unittest

a = Q([2, 4, 7, 9])
b = Q([-3, -4, -0, -8])
c = Q([0, 0, 0, 0])
d = Q([])

i = Q([0, 1, 0, 0])
j = Q([0, 0, 1, 0])
k = Q([0, 0, 0, 1])
one = Q([1, 0, 0, 0])

# Constructor errors
class TestConstructor(unittest.TestCase):
	def test_constuctor_error(self):
		with self.assertRaises(IndexError):
			Q([[2, 3], [4, 5, 6]])	
		with self.assertRaises(ValueError):
			Q(['a','v','b'])	
		with self.assertRaises(IndexError):
			Q([1, 2, 3, 4, 5])

# Sequence operations
class TestSequence(unittest.TestCase):
	def test_getitem(self):
		self.assertEqual(a[2], 7.0)

	def test_getitem_error(self):
		with self.assertRaises(TypeError):
			a['i']
		with self.assertRaises(IndexError):
			a[4]

	def test_iterator(self):
		self.assertEqual(list(a), [2.0, 4.0, 7.0, 9.0])

# Unary operations
class TestUnary(unittest.TestCase):
	def test_reprstr(self):
		self.assertEqual(repr(a), 'Q-vector( +2.0 +4.0i +7.0j +9.0k )')
		self.assertEqual(str(b), 'Q-vector( -3.0 -4.0i +0.0j -8.0k )')

	def test_floatabs(self):
		import math
		mag = math.sqrt(2.0**2+4.0**2+7.0**2+9.0**2)
		self.assertEqual(float(a), mag)
		self.assertEqual(abs(a), mag)

	def test_posneg(self):
		self.assertEqual(+a, a)
		self.assertEqual(-(-a), a)

# Binary operations
class TestBinary(unittest.TestCase):
	def test_addsub(self):
		self.assertEqual(b+a, Q([-1, 0, 7, 1]))
		self.assertEqual(b-a, -Q([5, 8, 7, 17]))
	
	def test_muldiv(self):
		self.assertEqual(a*b, Q([82, -76, -25, -15]))
		self.assertEqual(a*0.9, Q([1.8, 3.6, 6.3, 8.1]))
		self.assertEqual(0.9*a, Q([1.8, 3.6, 6.3, 8.1]))
		self.assertEqual(a/2, Q([1, 2, 3.5, 4.5]))

	def test_muldiv_error(self):
		with self.assertRaises(TypeError):
			a*'a'
			a*self
		with self.assertRaises(TypeError):
			a/'a'

	def test_prod(self):
		self.assertEqual(i*j, k)
		self.assertEqual(j*k, i)
		self.assertEqual(k*i, j)
		self.assertEqual(j*i, -k)
		self.assertEqual(k*j, -i)
		self.assertEqual(i*k, -j)
		self.assertEqual(i*i, -one)
		self.assertEqual(j*j, -one)
		self.assertEqual(k*k, -one)
		self.assertEqual(i*j*k, -one)


# Comparisons and boolean outputs
class TestBoolean(unittest.TestCase):
	def test_bool(self):
		self.assertFalse(c)
		self.assertFalse(d)
		self.assertTrue(a)

	def test_comparison(self):
		self.assertFalse(a==b)
		self.assertTrue(c==d)
		self.assertTrue(a!=b)
		self.assertTrue(a>b)
		self.assertFalse(a<b)
		self.assertTrue(b<=a)
		self.assertFalse(b>=a)
		self.assertTrue(not d)
		self.assertFalse(not a)

class TestNonNative(unittest.TestCase):
	def test_norm(self):
		self.assertEqual((3*i).norm(), i)
		self.assertEqual(abs(a.norm()), 1.0)
		self.assertEqual(a.norm().norm(), a.norm())
	
	def test_conjugate(self):
		self.assertEqual(a.conj(), Q([2, -4, -7, -9]))

	def test_inverse(self):
		res = [0.0133333333333, -0.0266666666667, -0.0466666666667, -0.06]
		zero = a.inv()-Q(res)
		dtol = 0.000000000001
		self.assertTrue(abs(zero)<dtol)
		self.assertEqual(a*a.inv(), one)

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
runfn(suitefn(TestNonNative))
