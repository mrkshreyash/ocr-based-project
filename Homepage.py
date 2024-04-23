import pytesseract
import streamlit as st
from PIL import Image
from googletrans import Translator

st.set_page_config(
    page_title="OCR Marathi 2 English",
    layout='centered'
)


class Homepage:
    def __init__(self):
        self.ocr_data = ""
        self.translated_text = ""
        self.image_path = ""

    def read_ocr(self):
        file = st.file_uploader('Upload files')
        st.write("---")

        if file:
            # st.write(file)
            img = Image.open(file)
            self.ocr_data = pytesseract.image_to_string(img, lang='mar')
            return self.ocr_data

    def translate_to_english(self):
        translator = Translator()
        if self.ocr_data:
            self.translated_text = translator.translate(self.ocr_data, src='mr', dest='en')
            return self.translated_text.text


if __name__ == '__main__':

    st.title("Marathi to English Model (OCR + TRANSLATION)")
    st.write("---")
    app = Homepage()
    data = app.read_ocr()
    translation = app.translate_to_english()
    if data:
        with st.container():
            st.subheader("Original Text")
            st.write(data)
            st.write("---")

        with st.container():
            st.subheader("Translated Text")
            st.write(translation)
            st.write("---")
