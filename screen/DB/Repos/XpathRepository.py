from screen.models import ElementsXpaths
from screen.DB.Repos.RepositoryBase import RepositoryBase

class XpathRepository(RepositoryBase):
    def __init__(self) -> None:
        super().__init__(ElementsXpaths)
        
    def getAllXpath(self):
        return super().get_all()