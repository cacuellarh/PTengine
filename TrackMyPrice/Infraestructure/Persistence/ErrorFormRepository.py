
from TrackMyPrice.Core.Application.Contracts.Repository.IErrorFormRepository import IErrorFormRepository
from screen.models import Error_form

class ErrorFormRepository(IErrorFormRepository):
    def __init__(self) -> None:
        super().__init__(Error_form)