import pytesseract
from PIL import Image

def raw_text_extraction(img_path):
    """
    Extracts text from an image file using OCR.

    :param img_path: The file path of the image from which text needs to be extracted.
    :return: A string containing the text extracted from the image.
    """
    image = Image.open(img_path)  # Opening the image file using Pillow
    return pytesseract.image_to_string(image)  # Using pytesseract to convert the image to a string (text extraction)
# print(raw_text_extraction(image))
