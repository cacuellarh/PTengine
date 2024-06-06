from dataclasses import dataclass
from django.db import models
from typing import Union

@dataclass
class RepositoryResponse:
    Status : bool
    CodeStatus : int
    Message : str
    Data : Union[dict, list, models.Model]

    def ToDict(self)-> dict:
        data = self.Data
        if isinstance(self.Data, models.Model):
            data = self.Data.to_dict()

        print(f"DATAAA ES{data}")    
        return {
            "Status" : self.Status,
            "CodeStatus" : self.CodeStatus,
            "Message" : self.Message,
            "Data" : data
        }
        
