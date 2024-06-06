from screen.models import Client
from TrackMyPrice.Core.Application.Contracts.Repository.IClientRepository import IClientRepository

class ClientRepository(IClientRepository):

    def __init__(self) -> None:
        super().__init__(Client)