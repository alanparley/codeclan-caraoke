import unittest

from classes.song import Song


class TestSong(unittest.TestCase):

    def setUp(self):
        self.song = Song("Oasis - Wonderwall")
