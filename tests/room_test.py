import unittest

from classes.room import Room
from classes.guest import Guest
from classes.song import Song


class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room = Room("The Karaoke Bar")
        self.guest_1 = Guest("Alan")
        # self.song_1 = Song("The Beatles - Help")

    def test_room_has_name(self):
        self.assertEqual("The Karaoke Bar", self.room.name)

    def test_can_add_song_to_room(self):
        new_song = Song("Atomic")
        self.room.add_song(new_song)
        self.assertEqual(1, self.room.song_count())

    def test_can_add_guest_to_room(self):
        new_guest = Guest("Alan")
        self.room.add_guest(new_guest)
        self.assertEqual(1, self.room.guest_count())
