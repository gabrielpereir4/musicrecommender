import api, track
import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyOAuth

class Playlist:
    def __init__(self, id):
        self._id = id
        self.sp = None
        self.playlist_tracks = []
        self.track_details = False

    # Getters/Setters

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id
        self.get_playlist_tracks()


    # Métodos


    def authenticate(self):
        access_token = api.main()
        sp = spotipy.Spotify(auth=access_token)
        self.sp = sp
        return sp

    
    def print_all_tracks(self, complete=False):
        if not complete:
            for t in self.playlist_tracks:
                print(t.track_info())
            print(f"\nPlaylist is {len(self.playlist_tracks)} musics long!\n")
        else:
            for t in self.playlist_tracks:
                print(t.track_complete_info())
            print(f"Playlist is {len(self.playlist_tracks)} musics long!\n")



    def get_playlist_tracks(self):
        if self.sp is None:
            self.sp = self.authenticate()

        playlist_tracks_unc = self.sp.playlist_items(self.id, fields='items(track(id, name, artists, album(id, name)))')
        for t in playlist_tracks_unc['items']:
            # t_obj é atributo track de playlist_tracks_unc, para poder acessar os seus atributos com mais facilidade
            t_obj = t['track']
            artists = ', '.join([artist['name'] for artist in t_obj['artists']])
            self.playlist_tracks.append(track.Track(t_obj['id'], t_obj['name'], artists, t_obj['album']['id'], t_obj['album']['name']))
        return self.playlist_tracks


    def get_track_details(self):
        if self.playlist_tracks is None:
            return False

        for t in self.playlist_tracks:
            
            track_obj = self.sp.track(t.id) if t.id != 'Not available' else None
            popularity = track_obj['popularity'] if track_obj else None

            audio_features = self.sp.audio_features(t.id)[0] if t.id != 'Not available' else None

            t.set_track_details(audio_features['tempo'], audio_features['energy'], popularity)

        self.track_details = True
            



    def analyze_playlist(self):
        tempolist = []
        energylist = []

        for t in self.playlist_tracks:
            tempolist.append(t.bpm)
            energylist.append(t.energy)

        avgtempo = round((sum(tempolist)/len(tempolist)), 2)
        print(f"Average BPM of this playlist is: {avgtempo}")
        fastest = max(tempolist)
        fastest_id = tempolist.index(fastest)
        print(f"Fastest song is {self.playlist_tracks[fastest_id].track_complete_info()}")
        slowest = min(tempolist)
        slowest_id = tempolist.index(slowest)
        print(f"Slowest song is {self.playlist_tracks[slowest_id].track_complete_info()}")
        mostenergy = max(energylist)
        mostenergy_id = energylist.index(mostenergy)
        print(f"Most energetic song is {self.playlist_tracks[mostenergy_id].track_complete_info()}")
        leastenergy = min(energylist)
        leastenergyid = energylist.index(leastenergy)
        print(f"Least energetic song is '{self.playlist_tracks[leastenergyid].track_complete_info()}") 