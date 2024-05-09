

import sys
import pandas as pd
from src.mylogger import logging
from src.exceptionFile import my_exception
from sklearn.preprocessing import MinMaxScaler





class dataTransformationConfig:

    def __init__(self):

        pass


    def start_dataTransformation(self, df):
        
        try:

            logging.info('Entered data_transformation method...!')

            print('Entered data_transformation method...!\n')

            scaler = MinMaxScaler()

            music_features = df[['Danceability', 'Energy', 'Key', 'Loudness', 'Mode', 'Speechiness', 'Acousticness', 'Instrumentalness', 'Liveness', 'Valence', 'Tempo']].values
            
            music_features_scaled = scaler.fit_transform(music_features)

            logging.info('Successfully transformed data and converted to dataframe...!')

            print('Successfully transformed data and converted to dataframe...!\n')

            logging.info('Saved dataframe as a CSV format in artifacts directory...!')

            print('Saved dataframe as a CSV format in artifacts directory...!\n')

            music_features_scaled = pd.DataFrame(music_features_scaled)

            music_features_scaled.to_csv('music_features_scaled')

            logging.info('Existed data_transformation method...!\n')

            print('Existed data_transformation method...!\n')

            return music_features_scaled

        except Exception as e:
            raise my_exception(e, sys)


