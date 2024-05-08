import sys 
sys.path.append(r'C:\\Users\\camil\\OneDrive\\Desktop\\Proyectos\\TMP\\PTengine')
import pytesseract
from PIL import Image
import cv2

from screen.Engine.OCR import OCR

def PreprocessImage(image_path):
    # Cargar la imagen usando OpenCV
    image = cv2.imread(image_path)
    # Convertir la imagen a escala de grises
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Aplicar umbral adaptativo para resaltar los números
    _, threshold_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return threshold_image

def ExtractText(image_path):
    # Preprocesar la imagen
    processed_image = preprocess_image(image_path)
    # Convertir la imagen procesada a un objeto Image de PIL
    pil_image = Image.fromarray(processed_image)
    # Utilizar Tesseract para extraer el texto de la imagen
    extracted_text = pytesseract.image_to_string(pil_image, config='-psm 6 --oem 3 -c tessedit_char_whitelist=0123456789 outputbase digits')
    return extracted_text.strip()

BASE_PATH_PROJECT = "C:\\Users\\camil\\OneDrive\\Desktop\\Proyectos\\TMP\\PTengine\\"
PATHS = {
    "base_url" : 'http://127.0.0.1:8000/',
    "tmp" : f'{BASE_PATH_PROJECT}screen\\static\\temp\\',
    "img_folder" : f'{BASE_PATH_PROJECT}screen\\static\\img\\',
    "error" : f'{BASE_PATH_PROJECT}screen\\static\\err_img\\',
    "tesseract": 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract',
    "ImageRoutes" : "http://127.0.0.1:8000/static/img/"
}

#ocr = OCR(PATHS["tmp"],PATHS["tesseract"])
num = extract_text("C:\\test\\4.png")
print(num)

