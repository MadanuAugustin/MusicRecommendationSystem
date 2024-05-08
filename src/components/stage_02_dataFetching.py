
import sys
import spotipy
import pandas as pd
from src.mylogger import logging
from src.exceptionFile import my_exception


class dataFetchingConfig:

    def __init__(self):

        pass


    def data_fetching(self, playlist_id, access_token):

        try:

            logging.info('Entered data_fetching method...!')

            print('Entered data_fetching method...!')

            # setting up Spotipy with access token
            sp = spotipy.Spotify(auth = access_token)

            # fetching the tracks from the playlist
            playlist_tracks = sp.playlist_tracks(playlist_id, fields = 'items(track(id, name, artists, album(id, name)))')


            # extracting relevant information and storing them in a list of dictionaries

            music_data = []

            for track_info in playlist_tracks['items']:
        
                track = track_info['track']

                track_name = track['name']

                artists = ', '.join([artist['name'] for artist in track['artists']])

                album_name = track['album']['name']

                album_id = track['album']['id']

                track_id = track['id']


                # fetching audio features for the track

                audio_features = sp.audio_features(track_id)[0] if track_id != 'Not available' else None

                # fetching release date of the album

                try:
                    album_info = sp.album(album_id) if album_id != 'Not available' else None
                    release_date = album_info['release_date'] if album_info else None

                except:
                    release_date = None


                # fetching popularity of the track

                try:
                    track_info = sp.track(track_id) if track_id != 'Not available' else None
                    popularity = track_info['popularity'] if track_info else None

                except:
                    popularity = None

                # fetching additional track information

                track_data = {
                    'Track_Name' : track_name,
                    'Artists' : artists,
                    'Album_Name' : album_name,
                    'Album_ID' : album_id,
                    'Track_ID' : track_id,
                    'Popularity' : popularity,
                    'Release_date' : release_date,
                    'Duration(ms)' : audio_features['duration_ms'] if audio_features else None,
                    'Explicit' : track_info.get('explicit', None),
                    'External_URLs' : track_info.get('external_urls', {}).get('spotify', None),
                    'Danceability' : audio_features['danceability'] if audio_features else None,
                    'Energy' : audio_features['energy'] if audio_features else None,
                    'Key' : audio_features['key'] if audio_features else None,
                    'Loudness' : audio_features['loudness'] if audio_features else None,
                    'Mode' : audio_features['mode'] if audio_features else None,
                    'Speechiness' : audio_features['speechiness'] if audio_features else None,
                    'Acousticness' : audio_features['acousticness'] if audio_features else None,
                    'Instrumentalness' : audio_features['instrumentalness'] if audio_features else None,
                    'Liveness' : audio_features['liveness'] if audio_features else None,
                    'Valence' : audio_features['valence'] if audio_features else None,
                    'Tempo' : audio_features['tempo'] if audio_features else None  
                    }


                music_data.append(track_data)


            # creating dataframe from the above dictionary
            logging.info('Created dataframe of the fetched data...!')
            print('Created dataframe of the fetched data...!')

            df =  pd.DataFrame(music_data)

            logging.info('Saved dataframe as a CSV format in artifacts directory...!')
            print('Saved dataframe as a CSV format in artifacts directory...!')

            df.to_csv('artifacts//spotifyData.csv', header=True)

            logging.info('Exited data_fetching method...!')

            print('Exited data_fetching method...!')

            return df
        
        except Exception as e:
            raise my_exception(e, sys)