from screen.models import ImageTrack
from TrackMyPrice.Core.Application.Contracts.Repository.IimageTrackRepository import IimageTrackRepository

class ImageTrackRepository(IimageTrackRepository):

    def __init__(self) -> None:
        super().__init__(ImageTrack)