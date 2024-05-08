

from src.components.spotifyAuthentication import authenticationConfig
from src.exceptionFile import my_exception
from src.mylogger import logging
import sys


STAGE_NAME = 'SPOTIFY_AUTHENTICATION'


try:

    logging.info(f'-------------{STAGE_NAME} started -----------')

    print(f'-------------{STAGE_NAME} started -----------')

    authentication = authenticationConfig()

    mytoken = authentication.start_authentication(CLIENT_ID = '198da2205f494f7bb7788e9f927b7ee3', CLIENT_SECRET = '511e99423d3846e7bedf70fd7caacc4b')

    logging.info(f'----------{STAGE_NAME} completed----------------')

    print(f'----------{STAGE_NAME} completed----------------')

except Exception as e:
    raise my_exception(e, sys)
