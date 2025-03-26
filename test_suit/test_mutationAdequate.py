import unittest
from isTriangle import Triangle

class TriangleMutationTest(unittest.TestCase):
    def test_floating_point_values(self):
        """ Test cases with floating point values """
        # Test case: All sides are different floating-point values, should classify as SCALENE
        actual = Triangle.classify(3.5, 4.5, 5.5)
        expected = Triangle.Type.SCALENE
        self.assertEqual(actual, expected)
        
        # Test case: Two sides are equal floating-point values, should classify as ISOSCELES
        actual = Triangle.classify(2.5, 2.5, 3.5)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)
        
        # Test case: All sides are equal floating-point values, should classify as EQUILATERAL
        actual = Triangle.classify(6.6, 6.6, 6.6)
        expected = Triangle.Type.EQUILATERAL
        self.assertEqual(actual, expected)

    def test_invalid_triangles(self):
        """ Test cases where the triangle should be classified as INVALID """
        # Test case: One side is zero, should classify as INVALID
        actual = Triangle.classify(0, 1, 2)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
        
        # Test case: One side is negative, should classify as INVALID
        actual = Triangle.classify(-1, 5, 6)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
        
        # Test case: Degenerate triangle (sum of two sides equals the third), should classify as INVALID
        actual = Triangle.classify(1, 2, 3)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
        
        # Test case: Sum of two sides is less than the third side, should classify as INVALID
        actual = Triangle.classify(10, 1, 1)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test_edge_cases(self):
        """ Test edge cases for triangle classification """
        # Test case: All sides are equal to 1, should classify as EQUILATERAL
        actual = Triangle.classify(1, 1, 1)
        expected = Triangle.Type.EQUILATERAL
        self.assertEqual(actual, expected)
        
        # Test case: Two sides are equal and the third side is slightly smaller, should classify as ISOSCELES
        actual = Triangle.classify(5, 5, 4.9)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)
        
        # Test case: Two sides are equal and the third side is slightly larger, should classify as INVALID
        actual = Triangle.classify(5, 5, 10.1)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test_large_values(self):
        """ Test cases with large values """
        # Test case: Large values that form a valid SCALENE triangle
        actual = Triangle.classify(1000000, 999999, 999998)
        expected = Triangle.Type.SCALENE
        self.assertEqual(actual, expected)
        
        # Test case: Large values that form a valid EQUILATERAL triangle
        actual = Triangle.classify(1000000, 1000000, 1000000)
        expected = Triangle.Type.EQUILATERAL
        self.assertEqual(actual, expected)
        
        # Test case: Large values that do not form a valid triangle
        actual = Triangle.classify(1000000, 1, 1)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test_extreme_edge_cases(self):
        """ Test cases with extreme edge values """
        # Test case: Very small positive values that form a valid EQUILATERAL triangle
        actual = Triangle.classify(0.0001, 0.0001, 0.0001)
        expected = Triangle.Type.EQUILATERAL
        self.assertEqual(actual, expected)
        
        # Test case: Very small positive values that do not form a valid triangle
        actual = Triangle.classify(0.0001, 0.0001, 0.0003)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()