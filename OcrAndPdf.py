from pdf2image import convert_from_path
import pytesseract

pdf_path = "Marathi Pdf.pdf"
pages = convert_from_path(pdf_path)

ocr_result = ""

for page in pages:
    ocr_result += pytesseract.image_to_string(page, lang='mar')

with open('output.txt', 'w+') as file:
    file.write(ocr_result)
