import mss
import mss.tools
import pytesseract
import numpy as np
from pytesseract.pytesseract import Output
import cv2

sct = mss.mss()

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

ss = sct.grab(sct.monitors[1]) # 
im = np.array(ss) # convert to nparray
im = np.flip(im[:,:,:3],2) # convert bgra -> rgb

string = pytesseract.image_to_string(im)
data = pytesseract.image_to_data(im, output_type=Output.DICT)
print(string)
print(data)