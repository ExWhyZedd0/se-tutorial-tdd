import unittest
from calculator.operations import divide
class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(-1, 1), -2)
        self.assertEqual(subtract(0, 0), 0)

    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-2, 3), -6)
        self.assertEqual(multiply(0, 3), 0)

    def test_divide(self):
        self.assertEqual(divide(9, 3), 3)
        self.assertEqual(divide(-6, 3), -2)
        self.assertEqual(divide(0, 1), 0)
        with self.assertRaises(ZeroDivisionError):
            divide(1, 0)

if __name__ == '__main__':
    unittest.main()