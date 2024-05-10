from dataclasses import dataclass

@dataclass
class TesseractScanRequest:

    tesseractPath:str
    tesseractFlagsConfiguration:str
    preprocessorFileSaveTest:str = None