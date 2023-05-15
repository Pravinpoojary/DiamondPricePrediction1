import os
import sys
import pandas as pd
from src.logging import logging
from src.exception import CustomeException

from src.components.data_ingestion import DataIngestion

if __name__=="__main__":
    obj=DataIngestion()
    train_path,test_path=obj.intiate_data_ingestion()

    print(train_path,test_path)



