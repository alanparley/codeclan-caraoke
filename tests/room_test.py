import unittest

from classes.room import Room
from classes.guest import Guest
from classes.song import Song


class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room = Room("The Karaoke Bar")
        self.guest_1 = Guest("Jasper")
        self.guest_2 = Guest("Magnus")
        self.song_1 = Song("Atomic")

        guests = [self.guest_1, self.guest_2]

    def test_room_has_name(self):
        self.assertEqual("The Karaoke Bar", self.room.name)

    def test_can_add_song_to_room(self):
        self.room.add_song(self.song_1)
        self.assertEqual(1, self.room.song_count())

    def test_can_add_guest_to_room(self):
        self.room.add_guest(self.guest_1)
        self.assertEqual(1, self.room.guest_count())

    def test_can_remove_guest_from_room(self):
        self.room.guests.append(self.guest_1)
        self.room.guests.append(self.guest_2)
        self.room.remove_guest(self.guest_1)
        self.assertEqual(1, self.room.guest_count())
