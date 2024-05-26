class Track:
    def __init__(self, id, name, artist, album_id, album):
        self._id = id
        self.name = name
        self.artist = artist
        self._album_id = album_id
        self.album = album
        self.bpm = None
        self.energy = None
        self.popularity = None

    @property
    def id(self):
        return self._id

    def track_info(self):
        return(f"{self.name} --- {self.artist} ({self.album})")
    
    def track_complete_info(self):
        return(f"{self.name} --- {self.artist} ({self.album})\nBPM: {self.bpm} Energy: {self.energy} Popularity: {self.popularity}\n")

    def set_track_details(self, BPM, ENERGY, POPULARITY):
        self.bpm = BPM
        self.energy = ENERGY
        self.popularity = POPULARITY