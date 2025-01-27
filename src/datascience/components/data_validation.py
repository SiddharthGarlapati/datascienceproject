import os
from src.datascience import logger
from src.datascience.entity.config_entity import (DataValidationConfig)
import pandas as pd

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_columns(self) -> bool:
        try:
            validation_status = None

            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = list(data.columns)

            all_schema = self.config.all_schema.keys()

            for col in all_cols:
                if not col in all_schema:
                    validation_status = False
                    with open(self.config.STATUS_FILE,'w') as f:
                        f.write(f"validation status: {validation_status}")
                else:
                    validation_status = True
                    with open(self.config.STATUS_FILE ,'w') as f:
                        f.write(f"validation status: {validation_status}")

            return validation_status  
        
        except Exception as e:
            raise e
        

    def validate_all_columns_types(self) -> bool:
        try: 
            validation_status = None
            data = pd.read_csv(self.config.unzip_data_dir)
            col_types = [ dtype.name for dtype in data.dtypes] 

            all_schema = self.config.all_schema.values()

            for x,y in zip(col_types,all_schema):
                if x != y:
                    validation_status = False
                else: 
                    validation_status = True  

            with open(self.config.STATUS_FILE,'w') as f:
                f.write(f"validation status: {validation_status}")

            return validation_status    

        except Exception as e:
            raise e   
        
