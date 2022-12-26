class Music:
    def __init__(self, author, song, album, year):
        self.author = author
        self.song = song 
        self.album = album
        self.year = year
    def __str__(self):
        return(f"Author:{self.author}\nSong:{self.song}\nAlbum: {self.album}\nYear: {self.year}")
song1 = Music("Ed Sheeran","Hearts Don't Break Around Here","Divide",2017)
song2 = Music("Sebastian","JPCHWDP","JEBACKAPUSI",2017)
print(song1)
print()
print(song2)