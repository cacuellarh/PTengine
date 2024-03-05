from colorama import Fore, Style

class Console:
    
    @staticmethod
    def info(message):
        
        print(Fore.YELLOW, message + Style.RESET_ALL)
    @staticmethod
    def warning(message):
        
        print(Fore.RED, message + Style.RESET_ALL)
    @staticmethod
    def success(message):
        
        
        print(Fore.GREEN, message + Style.RESET_ALL)
    
    @staticmethod    
    def important(message):
        
        print(Fore.BLUE, message + Style.RESET_ALL)             