from datetime import datetime, timedelta
from django.utils import timezone

class SetCurrentTimeCo:
    __TimeDifference : int = 5 #Por defecto diferencia entre USA y Colombia,
    @staticmethod
    def SetTimeCo(date : datetime) -> datetime:
        newDate = date - timedelta(hours=SetCurrentTimeCo.__TimeDifference)
        return newDate
    @staticmethod
    def SetTimeDifference(self,timeDifference:int)->None:
        SetCurrentTimeCo.__TimeDifference = timeDifference