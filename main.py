import api, playlist
import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def main(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main('Gabriel!')
    p = playlist.Playlist(id='2Bumv19tnmTT72ZTjhx0VL')
    p.get_playlist_tracks()
    p.get_track_details()
    p.print_all_tracks(True)
    p.analyze_playlist()