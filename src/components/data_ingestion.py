import os
import sys

from src.logging import logging
from src.exception import CustomeException

import pandas as pd
from sklearn.model_selection import train_test_split

from dataclasses import dataclass

#intialize data ingestion

@dataclass

class DataIngestionConfig:
    train_path=os.path.join("artifacts","train.csv")
    test_path=os.path.join("artifacts","test.csv")
    raw_path=os.path.join("artifacts","raw.csv")

# data ingestion class

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()
    
    def intiate_data_ingestion(self):
        logging.info("data ingestion start")


        try:
            df=pd.read_csv(os.path.join("notebooks/data","gemstone.csv"))
            logging.info("Data read as pandas Dataframe")

            os.makedirs(os.path.dirname(self.ingestion_config.raw_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_path,index=False) 
            logging.info("my raw data getting stored") 

            train_set,test_set=train_test_split(df,random_state=42,test_size=0.30)
            train_set.to_csv(self.ingestion_config.train_path,index=False,header=True) 
            test_set.to_csv(self.ingestion_config.test_path,index=False,header=True)

            logging.info("data ingestion complete")

            return (
                self.ingestion_config.train_path,
                self.ingestion_config.test_path
                
            )
            

        except Exception as e:
            logging.info("exception occured in data ingestion stage")
            raise CustomeException(e,sys)
        













    


