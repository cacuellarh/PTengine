from TrackMyPrice.Core.Application.Contracts.Repository.IImageBasicRepository import IImageBasicRepository
from screen.models import ImageBasic

class ImageBasicRepositoryImp(IImageBasicRepository):

    def __init__(self) -> None:
        super().__init__(ImageBasic)