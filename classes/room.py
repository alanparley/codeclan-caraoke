class Room:

    def __init__(self, name):
        self.name = name
        self.songs = []
        self.guests = []

    def guest_count(self):
        return len(self.guests)

    def song_count(self):
        return len(self.songs)

    def add_song(self, song):
        self.songs.append(song)

    def add_guest(self, guest):
        self.guests.append(guest)

    def remove_guest(self, guest):
        self.guests.remove(guest)
