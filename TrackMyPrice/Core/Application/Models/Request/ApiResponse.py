from dataclasses import dataclass
from typing import Union
from django.db import models

@dataclass
class ResponseDetails:
    status : bool
    status_code: int
    message: str
    data: Union[dict, list, models.Model] = None