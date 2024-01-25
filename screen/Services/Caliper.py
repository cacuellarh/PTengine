from ..models import ImageTrack
from decimal import Decimal

class Caliper:
    
    def calibrateY(img_track : ImageTrack, percentage):
        
        img_track.width *= Decimal(percentage) 
        img_track.height*= Decimal(percentage) 
        
        return img_track