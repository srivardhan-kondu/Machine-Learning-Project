# Importing necessary libraries
import os  # For handling file paths and directories
import sys  # For interacting with system-specific parameters and functions
from src.exception import CustomException  # Custom exception handling class
from src.logger import logging  # Logger for logging messages
import pandas as pd  # For data manipulation and analysis
from sklearn.model_selection import train_test_split  # For splitting data into training and test sets
from dataclasses import dataclass  # To define classes that primarily store data

# DataIngestionConfig will hold the paths for the training, testing, and raw data files
@dataclass
class DataIngestionConfig:
    # Define default paths for train, test, and raw data
    train_data_path: str = os.path.join('artifacts', 'train.csv')  # Path for training data
    test_data_path: str = os.path.join('artifacts', 'test.csv')  # Path for testing data
    raw_data_path: str = os.path.join('artifacts', 'raw_data.csv')  # Path for raw data

# DataIngestion class handles reading the data, saving raw data, and splitting it into train/test sets
class DataIngestion:
    # Constructor to initialize the DataIngestionConfig, storing paths for data
    def __init__(self):
        # Initialize config object which contains paths for train, test, and raw data
        self.ingestion_config = DataIngestionConfig()

    # Method to initiate the data ingestion process
    def initiate_data_ingestion(self):
        # Logging the start of the data ingestion process
        logging.info("Entered the data ingestion method or component")
        try:
            # Reading the dataset from a CSV file (you can modify this to read from a database or other sources)
            df = pd.read_csv(r'S:\Machine Learning\END -END PROJECT\notebooks\data\stud.csv')  # Example: Reading from a local CSV file
            logging.info("Read the dataset as a dataframe")

            # Create directories for storing the output files if they don't exist
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            # Save the raw data into a CSV file for future reference or reproducibility
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

            # Logging the initiation of the train-test split
            logging.info("Train-test split is initiated")

            # Split the dataset into training and testing sets (80% train, 20% test)
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            # Save the train and test datasets into CSV files
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            # Log completion of the ingestion process
            logging.info("Ingestion of data is completed")

            # Return the paths of the train and test data files
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        # Handle exceptions and raise custom exceptions with detailed error information
        except Exception as e:
            raise CustomException(e, sys)

if __name__=="__main__":
    obj=DataIngestion()
    obj.initiate_data_ingestion()