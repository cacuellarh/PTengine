import secrets

class Email_token:
    
    def generate_token(self):
        
        return secrets.token_urlsafe(30)