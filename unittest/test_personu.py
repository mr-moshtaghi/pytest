import unittest
from personu import Person


#
# class TestPerson(unittest.TestCase):
#
#     def test_full_name(self):
#         p1 = Person("sajjad", "moshtaghi")
#         p2 = Person("jack", "stark")
#
#         self.assertEqual(p1.full_name(), "sajjad moshtaghi")
#         self.assertEqual(p2.full_name(), "jack stark")
#
#     def test_email(self):
#         p1 = Person("sajjad", "moshtaghi")
#         p2 = Person("jack", "stark")
#
#         self.assertEqual(p1.email(), "sajjadmoshtaghi@gmail.com")
#         self.assertEqual(p2.email(), "jackstark@gmail.com")


# ======================================================================================

#
# class TestPerson(unittest.TestCase):
#     p1 = Person("sajjad", "moshtaghi")
#     p2 = Person("jack", "stark")
#
#     def test_full_name(self):
#         self.assertEqual(self.p1.full_name(), "sajjad moshtaghi")
#         self.assertEqual(self.p2.full_name(), "jack stark")
#
#     def test_email(self):
#         self.assertEqual(self.p1.email(), "sajjadmoshtaghi@gmail.com")
#         self.assertEqual(self.p2.email(), "jackstark@gmail.com")
#

# ============================================================================


class TestPerson(unittest.TestCase):
    def setUp(self):
        self.p1 = Person("sajjad", "moshtaghi")
        self.p2 = Person("jack", "stark")

    def tearDown(self):
        print("Done.....")

    def test_full_name(self):
        self.assertEqual(self.p1.full_name(), "sajjad moshtaghi")
        self.assertEqual(self.p2.full_name(), "jack stark")

    def test_email(self):
        self.assertEqual(self.p1.email(), "sajjadmoshtaghi@gmail.com")
        self.assertEqual(self.p2.email(), "jackstark@gmail.com")


if __name__ == '__main__':
    unittest.main()
