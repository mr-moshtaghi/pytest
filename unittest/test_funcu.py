import unittest
import funcu


class FuncTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(funcu.add(7, 3), 10)
        self.assertEqual(funcu.add(15, -4), 11)
        self.assertEqual(funcu.add(11, 0), 11)

    def test_subtract(self):
        self.assertEqual(funcu.subtract(7, 3), 4)
        self.assertEqual(funcu.subtract(15, -4), 19)
        self.assertEqual(funcu.subtract(11, 0), 11)

    def test_multiply(self):
        self.assertEqual(funcu.multiply(7, 3), 21)
        self.assertEqual(funcu.multiply(5, -4), -20)
        self.assertEqual(funcu.multiply(11, 0), 0)

    def test_division(self):
        self.assertEqual(funcu.division(12, 3), 4)
        self.assertEqual(funcu.division(15, -3), -5)
        self.assertEqual(funcu.division(10, 5), 2)
        self.assertRaises(ZeroDivisionError, funcu.division, 4, 0)


if __name__ == "__main__":
    unittest.main()
