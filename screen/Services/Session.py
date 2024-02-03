import random

class App_session:
    
    def create_sesion_key(self, request):
        
        head = random.randint(0,10000)
        random_ = random.randint(0,10000)
        
        key = f"{head}_{random_}"
        self._generate_id_session(key=key, request=request)
        
        
    
    def _generate_id_session(self, key, request):
        
        request.session['user_key_session'] = key