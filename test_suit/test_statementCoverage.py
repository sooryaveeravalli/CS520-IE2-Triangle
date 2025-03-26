import unittest
from isTriangle import Triangle

class TriangleTest(unittest.TestCase):
    def testEquilateral(self):
        # Test case: All sides are equal, should classify as EQUILATERAL
        actual = Triangle.classify(3, 3, 3)
        expected = Triangle.Type.EQUILATERAL
        self.assertEqual(actual, expected)
    
    def testNegativeSides(self):
        # Test case: One side is negative, should classify as INVALID
        actual = Triangle.classify(-3, 3, 3)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
    
    def testInValidSides(self):
        # Test case: Sides do not form a valid triangle, should classify as INVALID
        actual = Triangle.classify(1, 2, 3)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def testScalene(self):
        # Test case: All sides are different, should classify as SCALENE
        actual = Triangle.classify(3, 4, 5)
        expected = Triangle.Type.SCALENE
        self.assertEqual(actual, expected)

    def testIsosceles(self):
        # Test case: Two sides are equal, should classify as ISOSCELES
        actual = Triangle.classify(2, 2, 3)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)

    def testIsosceles2(self):
        # Test case: Two sides are equal (different configuration), should classify as ISOSCELES
        actual = Triangle.classify(3, 4, 4)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)

    def testIsosceles3(self):
        # Test case: Two sides are equal (another configuration), should classify as ISOSCELES
        actual = Triangle.classify(5, 4, 5)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)

    def testInValidSides2(self):
        # Test case: Sides do not form a valid triangle, should classify as INVALID
        # Covers the case where the sum of two sides is not greater than the third side
        actual = Triangle.classify(2, 2, 5)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()