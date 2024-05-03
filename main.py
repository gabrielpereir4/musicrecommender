import api
import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def get_playlist(playlist_id):
    access_token = api.main()
    sp = spotipy.Spotify(auth=access_token)

    playlist_tracks = sp.playlist_items(playlist_id, fields='items(track(id, name, artists, album(id, name)))')
    # Extract relevant information and store in a list of dictionaries
    music_data = []
    #print(playlist_tracks)
    for track_info in playlist_tracks['items']:
        track = track_info['track']
        track_name = track['name']
        artists = ', '.join([artist['name'] for artist in track['artists']])
        album_name = track['album']['name']
        album_id = track['album']['id']
        track_id = track['id']
        # Get popularity of the track
        try:
            track_info = sp.track(track_id) if track_id != 'Not available' else None
            popularity = track_info['popularity'] if track_info else None
        except:
            popularity = None

        print("Oie!")
        audio_features = sp.audio_features(track_id)[0] if track_id != 'Not available' else None
        print("Tchauu")
        #print(f"{track_name} - {artists} ({album_name}), {audio_features}")
        track_data = {
            "Track Name": track_name,
            "Artists": artists,
            "Album": album_name,
            "Track Tempo": audio_features['tempo'],
            "Track Popularity": popularity,
            "Track Energy": audio_features['energy']
        }
        music_data.append(track_data)
        print("Adding song!")

    print("Playlist Analyzed.")
    return music_data

def analyze_playlist(music_dt):
    tempolist = []
    energylist = []

    for track in music_dt:
        tempolist.append(track['Track Tempo'])
        energylist.append(track['Track Energy'])

    avgtempo = round((sum(tempolist)/len(tempolist)), 2)
    print(f"Average BPM of this playlist is: {avgtempo}")
    fastest = max(tempolist)
    fastest_id = tempolist.index(fastest)
    print(f"Fastest song is '{music_dt[fastest_id]['Track Name']}' by {music_dt[fastest_id]['Artists']} ({fastest} BPM)")
    slowest = min(tempolist)
    slowest_id = tempolist.index(slowest)
    print(f"Slowest song is '{music_dt[slowest_id]['Track Name']}' by {music_dt[slowest_id]['Artists']} ({slowest} BPM)")
    mostenergy = max(energylist)
    mostenergy_id = energylist.index(mostenergy)
    print(f"Most energetic song is '{music_dt[mostenergy_id]['Track Name']}' by {music_dt[mostenergy_id]['Artists']} ({mostenergy})")
    leastenergy = min(energylist)
    leastenergyid = energylist.index(leastenergy)
    print(f"Least energetic song is '{music_dt[leastenergyid]['Track Name']}' by {music_dt[leastenergyid]['Artists']} ({leastenergy})")    #print(music_data)

def main(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main('Gabriel!')
    data = get_playlist('60hGEgBjnyhW4kohGxW4xv')
    analyze_playlist(data)

