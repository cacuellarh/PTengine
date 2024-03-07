from ..Repos.Factory_repository import FactoryRepository
from ...models import History_events,History_prices,History_events_fails, ImageTrack
import datetime
from ...Services.Console_info import Console

class LogRepos():
    
    def __init__(self) -> None:
        #corregir DI
        self.factory_repos = FactoryRepository()
    def update_status_event(self, event : History_events):        
        event.status_scan = True
        self._save_model_instance(model_class=event, accion="update")

    def save_event(self, img: ImageTrack):
        return self._save_model_instance(History_events, fk_imagetrack=img, date=datetime.datetime.now())
             
    def save_event_error(self, event: History_events, route_error):
        self._save_model_instance(History_events_fails, fk_history_events=event, img_route_err=route_error)
          
    def save_history_prices(self, event: History_events, current_price):
        self._save_model_instance(History_prices, fk_history_events=event, price_scan=current_price)
    
    def _save_model_instance(self, model_class, accion="save", **kwargs):
        if accion == "save":
            instance = model_class(**kwargs)
        else:
            instance = model_class
        instance.save()  
        return instance
    
    def get_history_prices(self, id):
        
        result = History_prices.objects.filter(
        fk_history_events__fk_imagetrack_id=id
    ).values('price_scan', 'fk_history_events__fk_imagetrack__price', 'fk_history_events__date')
        print(result)
        return result