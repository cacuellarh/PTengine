import secrets

class EmailToken:
    @staticmethod
    def GenerateToken():
        
        return secrets.token_urlsafe(30)