from screen.models import ImageTrack
from TrackMyPrice.Core.Application.Contracts.Repository.IScannedImageRepository import IScannedImageRepository

class ScannedImageRepository(IScannedImageRepository):

    def __init__(self) -> None:
        super().__init__(ImageTrack)