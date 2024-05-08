
import sys
import base64
import requests
from src.exceptionFile import my_exception
from src.mylogger import logging

import spotipy
from spotipy.oauth2 import SpotifyOAuth


#-------------------------- CREATING A CLASS FOR SPOTIFY AUTHENTICATION --------------------------------#

class authenticationConfig:

    def __init__(self):

        pass

    def start_authentication(self, CLIENT_ID, CLIENT_SECRET)->str:

        try:

            logging.info('Entered start_authentication method...!')

            print('Entered start_authentication method...!')

            client_credentials = f"{CLIENT_ID}:{CLIENT_SECRET}"

            encoded_client_credentials = base64.b64encode(client_credentials.encode())

            token_URL = 'https://accounts.spotify.com/api/token'

            headers = {
            'Authorization' : f'Basic {encoded_client_credentials.decode()}'
            }

            data = {
            'grant_type' : 'client_credentials'
            }

            logging.info('Requesting the access token...!')

            response = requests.post(token_URL, data = data, headers = headers)

            if response.status_code == 200:
                access_token = response.json()['access_token']
                logging.info('Access token obtained successfully...!')
                print('Access token obtained successfully...!')

            else:
                logging.info('Error obtaining access token...!')
                print('Error obtaining access token...!')
                exit()

            logging.info('Exited start_authentication method...!')

            print('Exited start_authentication method...!')


            return str(access_token)

        except Exception as e:
            raise my_exception(e, sys)


