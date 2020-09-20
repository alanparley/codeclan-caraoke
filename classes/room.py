class Room:

    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.songs = []
        self.guests = []
        self.guest_limit = 3
        self.entry_cost = 3.75

    def guest_count(self):
        return len(self.guests)

    def song_count(self):
        return len(self.songs)

    def add_song(self, song):
        self.songs.append(song)

    def add_guest(self, guest):
        if len(self.guests) < self.guest_limit:
            self.guests.append(guest)

    def remove_guest(self, guest):
        self.guests.remove(guest)

    def guest_is_old_enough(self, guest):
        return guest.age >= 18

    def guest_can_afford(self, guest):
        return guest.cash >= self.entry_cost

    def room_full(self, guest):
        self.guests.append(guest)
        if len(self.guests) > self.guest_limit:
            return "Room Full"

    def pay_fee(self, guest):
        guest.pay_fee(fee)
        self.till += self.entry_cost
