import cv2
from TrackMyPrice.Core.Application.Contracts.SeleniumContracts import IPreproccesImage
from PIL import Image

class PreprocessImage(IPreproccesImage):

    def PreprocessImage(self, imagePath:str, pathSave:str):
        image = cv2.imread(imagePath)
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        _, threshold_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        cv2.imwrite(pathSave, threshold_image)

        return threshold_image