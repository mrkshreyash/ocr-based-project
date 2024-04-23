import cv2
import pytesseract
from langdetect import detect
from googletrans import Translator

def preprocess_image(image_path):
    # Read the image
    image = cv2.imread(image_path)
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Perform noise reduction and binarization
    preprocessed_image = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    return preprocessed_image

def perform_ocr(image_path):
    # Preprocess the image
    preprocessed_image = preprocess_image(image_path)
    # Perform OCR using PyTesseract
    ocr_data = pytesseract.image_to_string(preprocessed_image, lang='mar')
    return ocr_data

def translate_text(text, source_lang):
    translator = Translator()
    translated_text = translator.translate(text, src=source_lang, dest='en')
    return translated_text.text

def main(image_path):
    # Perform OCR
    ocr_data = perform_ocr(image_path)
    # Detect language
    detected_lang = detect(ocr_data)
    # Translate to English
    translated_data = translate_text(ocr_data, detected_lang)
    print("OCR Data (", detected_lang, "):", ocr_data)
    print("Translated Data:", translated_data)

if __name__ == "__main__":
    image_path = "Marathi Text.png"
    main(image_path)
