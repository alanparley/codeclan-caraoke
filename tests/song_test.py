import unittest

from classes.song import Song


class TestSong(unittest.TestCase):

    def setUp(self):
        self.song_1 = Song("Queen", "Bohemian Rhapsody")
        self.song_2 = Song("Oasis", "Wonderwall")

    def test_find_song_by_artist(self):
        self.assertEqual("Queen", self.song_1.artist)

    def test_find_song_by_title(self):
        self.assertEqual("Wonderwall", self.song_2.title)
