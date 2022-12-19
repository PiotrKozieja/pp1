class Music():
    def __init__(self, Performer, Song, Album, Year):
        self.Performer = Performer
        self.Song = Song
        self.Album = Album
        self.Year = Year
    def __str__(self):
        return(f"Performer: {self.Performer}\nSong: {self.Song}\nAlbum: {self.Album}\nYear: {self.Year}" )
utwor1 = Music("abcPerformer","ABCSONG","ABCALBUM","1234")
print(utwor1)