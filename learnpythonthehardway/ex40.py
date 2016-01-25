class Song(object):

	def __init__(self, lyrics):
		self.lyrics = lyrics

	def sing_me_a_song(self):
		for line in self.lyrics:
			print line

birthday_song = ["Happy birthday to you",
								 "I don't want to get sued",
								 "So I'll stop right there"]


bulls_on_parade = ["They rally around tha family",
									 "With pockets full of shells"]

Song(birthday_song).sing_me_a_song()
Song(bulls_on_parade).sing_me_a_song()


