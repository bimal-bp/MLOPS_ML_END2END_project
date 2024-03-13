import os 
import sys 
import yaml 
import dill 
import pandas as pd 
from src.excep.exception import customexception
from src.constant import * 



def write_yaml_file(file_path:str,data:dict=None):
    try:
        os.makedirs(os.path.dirname(file_path),exist_ok=True):
        with open(file_path,'w') as yaml_file:
            if data is not None:
                yaml.dump(data,yaml_file)

    except Exception as e:
        raise customexception(e,sys)


def read_yaml_file(file_path:str) -> dict:
    try:
        with open(file_path,'rb') as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise customexception(e,sys)


def save_numpy_array_data(file_path:str,array:np.array):
    try:
        dir_path=os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)
        with open (file_path,'wb') as file_obj:
            np.save(file_obj,array)
    except Exception as e:
        raise customexception(e,sys)


def load_numpy_array_data(file_path:str) -> np.array:
    try:
        with open(file_path,'rb') as file_obj:
            return np.load(file_obj)
    except Exception as e:
        raise customexception(e,sys)


def save_object(file_path:str,obj):
    try:
        dir_path=os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)
        with open (file_path,'wb') as file_obj:
            dill.dump(obj,file_obj)

    except Exception as e:
        raise customexception (e,sys)


def load_object(file_path:str):
    try:
        with open(file_path,'rb') as file_obj:
            return dill.load(file_obj)

    except Exception as e:
        raise customexception(e,sys)


def load_data(file_path:str,schema_file_path:str) -> pd.DataFrame:
    try:
        dataset_schema=read_yaml_file(schema_filepath)
        schema=dataset_schema[DATASET_SCHEMA_COLUMNS_KEY]
        dataframe=pd.read_csv(file_path)

        error_message=" "

        for column in dataframe.columns:
            if column in list(schema.keys()):
                dataframe[column].astype(schema[column])
            else:
                error_message=f"{error_message} \n columsn:[{column}] not in schema"
        if len(error_messge)>0:
            raise customexception(error_message)

        return dataframe

    except Exception as e:
        raise customexception(e,sys)