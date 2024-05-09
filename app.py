

from src.components.stage_01_spotifyAuthentication import authenticationConfig
from src.components.stage_02_dataFetching import dataFetchingConfig
from src.components.stage_03_dataTransformation import dataTransformationConfig
from src.exceptionFile import my_exception
from src.mylogger import logging
import sys


STAGE_NAME = 'STAGE_01_SPOTIFY_AUTHENTICATION'


try:

    logging.info(f'-------------{STAGE_NAME} started -----------')

    print(f'-------------{STAGE_NAME} started -----------\n\n')

    authentication = authenticationConfig()

    mytoken = authentication.start_authentication(CLIENT_ID = '198da2205f494f7bb7788e9f927b7ee3', CLIENT_SECRET = '511e99423d3846e7bedf70fd7caacc4b')

    logging.info(f'----------{STAGE_NAME} completed----------------')

    print(f'----------{STAGE_NAME} completed----------------\n\n')

except Exception as e:
    raise my_exception(e, sys)


STAGE_NAME = 'STAGE_02_DATA_FETCHING'

try:

    logging.info(f'-------------{STAGE_NAME} started -----------')

    print(f'-------------{STAGE_NAME} started -----------\n\n')

    data = dataFetchingConfig()

    mydf = data.data_fetching(playlist_id = "37i9dQZF1DX76Wlfdnj7AP", access_token = mytoken)

    logging.info(f'----------{STAGE_NAME} completed----------------')

    print(f'-------------{STAGE_NAME} completed -----------\n\n')
    
except Exception as e:
    raise my_exception(e, sys)



STAGE_NAME = 'STAGE_03_DATA_TRANSFORMATION'


try:

    logging.info(f'-------------{STAGE_NAME} started -----------')

    print(f'-------------{STAGE_NAME} started -----------\n\n')

    transformation = dataTransformationConfig()

    music_features_scaled = transformation.start_dataTransformation(mydf)

    logging.info(f'----------{STAGE_NAME} completed----------------')

    print(f'-------------{STAGE_NAME} completed -----------\n\n')
    
except Exception as e:
    raise my_exception(e , sys)
