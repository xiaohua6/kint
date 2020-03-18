# encoding:utf-8
from PIL import Image

import pytesseract

im=Image.open("3.png")

result=pytesseract.image_to_string(im)
print(result)

