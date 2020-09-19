import unittest

from classes.guest import Guest


class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Alan", 20)
