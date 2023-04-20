import unittest
import func


class FuncTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(func.add(7, 3), 10)
        self.assertEqual(func.add(15, -4), 11)
        self.assertEqual(func.add(11, 0), 11)

    def test_subtract(self):
        self.assertEqual(func.subtract(7, 3), 4)
        self.assertEqual(func.subtract(15, -4), 19)
        self.assertEqual(func.subtract(11, 0), 11)

    def test_multiply(self):
        self.assertEqual(func.multiply(7, 3), 21)
        self.assertEqual(func.multiply(5, -4), -20)
        self.assertEqual(func.multiply(11, 0), 0)

    def test_division(self):
        self.assertEqual(func.division(12, 3), 4)
        self.assertEqual(func.division(15, -3), -5)
        self.assertEqual(func.division(10, 5), 2)
        self.assertRaises(ZeroDivisionError, func.division, 4, 0)


if __name__ == "__main__":
    unittest.main()
