from screen.models import Frequency

class Frequency_repos():
    
    @staticmethod
    def get_all():
        
        return Frequency.objects.all()