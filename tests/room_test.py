import unittest

from classes.room import Room
from classes.guest import Guest
from classes.song import Song


class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room = Room("The Karaoke Bar")
        self.guest_1 = Guest("Jasper", 21, 50.00)
        self.guest_2 = Guest("Magnus", 17, 35.00)
        self.song_1 = Song("Queen", "Bohemian Rhapsody")
        self.song_2 = Song("Oasis", "Wonderwall")

        guests = [self.guest_1, self.guest_2]

    def test_room_has_name(self):
        self.assertEqual("The Karaoke Bar", self.room.name)

    def test_can_add_song_to_room(self):
        self.room.add_song(self.song_1)
        self.room.add_song(self.song_2)
        self.assertEqual(2, self.room.song_count())

    def test_can_add_guest_to_room(self):
        self.room.add_guest(self.guest_1)
        self.assertEqual(1, self.room.guest_count())

    def test_can_remove_guest_from_room(self):
        self.room.guests.append(self.guest_1)
        self.room.guests.append(self.guest_2)
        self.room.remove_guest(self.guest_1)
        self.assertEqual(1, self.room.guest_count())

    def test_guest_is_old_enough_returns_true(self):
        self.assertEqual(True, self.room.guest_is_old_enough(self.guest_1))

    def test_guest_is_old_enough_returns_false(self):
        self.assertEqual(False, self.room.guest_is_old_enough(self.guest_2))
