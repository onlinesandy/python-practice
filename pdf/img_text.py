"""
#CONVERT PDF TO IMAGE 
#IMAGE TO TEXT
#COMPARE PDF
SOME IMPORTANT COMMANDS
sudo apt-get update
sudo apt-get install tesseract-ocr
sudo apt-get install libtesseract-dev

pip3 install tesseract
pip3 install tesseract-ocr
"""
import os
import pdf2image
import time
import pytesseract
from PIL import Image


#DECLARE CONSTANTS
PDF_PATH1 = "pdf1.pdf"
PDF_PATH2 = "pdf2.pdf"
DPI = 200
OUTPUT_FOLDER = "img"
FIRST_PAGE = None
LAST_PAGE = None
FORMAT = 'jpg'
THREAD_COUNT = 1
USERPWD = None
USE_CROPBOX = False
STRICT = False

def pdftopil(pdf_file):
    pil_images = pdf2image.convert_from_path(pdf_file, dpi=DPI, output_folder=OUTPUT_FOLDER, first_page=FIRST_PAGE, last_page=LAST_PAGE, fmt=FORMAT, thread_count=THREAD_COUNT, userpw=USERPWD, use_cropbox=USE_CROPBOX, strict=STRICT)
    return pil_images
    
def save_images(pil_images,counter=0):
    #This method helps in converting the images in PIL Image file format to the required image format
    index = 1
    if(counter > 0):
        index = counter
    for image in pil_images:
        image.save("img/IMG_" + str(index) + ".jpg")
        index += 1


def compare_pdf(pdf1,pdf2):
    path1 = "img/IMG_1.jpg"
    path2 = "img/IMG_2.jpg"
    
    img1 = pdftopil(pdf1)
    save_images(img1)
    pdf_data_1 = pytesseract.image_to_string(Image.open(path1))


    img2 = pdftopil(pdf2)
    save_images(img2,2)
    pdf_data_2 = pytesseract.image_to_string(Image.open(path2))
    
    print(pdf_data_1)
    print(pdf_data_2)
    os.remove(path1)
    os.remove(path2)

    


if __name__ == "__main__":
    compare_pdf(PDF_PATH1,PDF_PATH2)

