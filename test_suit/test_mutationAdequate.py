import unittest
from isTriangle import Triangle

class TriangleMutationTest(unittest.TestCase):
    def test_floating_point_values(self):
        """ Test cases with floating point values """
        # Test case: All sides are different floating-point values, should classify as SCALENE
        self.assertEqual(Triangle.classify(3.5, 4.5, 5.5), Triangle.Type.SCALENE)
        # Test case: Two sides are equal floating-point values, should classify as ISOSCELES
        self.assertEqual(Triangle.classify(2.5, 2.5, 3.5), Triangle.Type.ISOSCELES)
        # Test case: All sides are equal floating-point values, should classify as EQUILATERAL
        self.assertEqual(Triangle.classify(6.6, 6.6, 6.6), Triangle.Type.EQUILATERAL)

    def test_invalid_triangles(self):
        """ Test cases where the triangle should be classified as INVALID """
        # Test case: One side is zero, should classify as INVALID
        self.assertEqual(Triangle.classify(0, 1, 2), Triangle.Type.INVALID)
        # Test case: One side is negative, should classify as INVALID
        self.assertEqual(Triangle.classify(-1, 5, 6), Triangle.Type.INVALID)
        # Test case: Degenerate triangle (sum of two sides equals the third), should classify as INVALID
        self.assertEqual(Triangle.classify(1, 2, 3), Triangle.Type.INVALID)
        # Test case: Sum of two sides is less than the third side, should classify as INVALID
        self.assertEqual(Triangle.classify(10, 1, 1), Triangle.Type.INVALID)

    def test_edge_cases(self):
        """ Test edge cases for triangle classification """
        # Test case: All sides are equal to 1, should classify as EQUILATERAL
        self.assertEqual(Triangle.classify(1, 1, 1), Triangle.Type.EQUILATERAL)
        # Test case: Two sides are equal and the third side is slightly smaller, should classify as ISOSCELES
        self.assertEqual(Triangle.classify(5, 5, 4.9), Triangle.Type.ISOSCELES)
        # Test case: Two sides are equal and the third side is slightly larger, should classify as INVALID
        self.assertEqual(Triangle.classify(5, 5, 10.1), Triangle.Type.INVALID)

    def test_large_values(self):
        """ Test cases with large values """
        # Test case: Large values that form a valid SCALENE triangle
        self.assertEqual(Triangle.classify(1000000, 999999, 999998), Triangle.Type.SCALENE)
        # Test case: Large values that form a valid EQUILATERAL triangle
        self.assertEqual(Triangle.classify(1000000, 1000000, 1000000), Triangle.Type.EQUILATERAL)
        # Test case: Large values that do not form a valid triangle
        self.assertEqual(Triangle.classify(1000000, 1, 1), Triangle.Type.INVALID)

    def test_extreme_edge_cases(self):
        """ Test cases with extreme edge values """
        # Test case: Very small positive values that form a valid EQUILATERAL triangle
        self.assertEqual(Triangle.classify(0.0001, 0.0001, 0.0001), Triangle.Type.EQUILATERAL)
        # Test case: Very small positive values that do not form a valid triangle
        self.assertEqual(Triangle.classify(0.0001, 0.0001, 0.0003), Triangle.Type.INVALID)

if __name__ == '__main__':
    unittest.main()