import unittest

from classes.guest import Guest


class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest_1 = Guest("Alan", 43, 100.00)
        self.guest_2 = Guest("Young Lad", 16, 10)

    def test_find_guest_by_name(self):
        self.assertEqual("Alan", self.guest_1.name)

    def test_find_guest_by_age(self):
        self.assertEqual(16, self.guest_2.age)

    def test_guest_has_cash(self):
        self.assertEqual(100.00, self.guest_1.cash)
