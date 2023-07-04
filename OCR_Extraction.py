import cv2 as cv
import sys
from PyPDF2 import PdfReader
import os
from PyPDF2 import PdfReader, PdfWriter
from PyPDF2.generic import AnnotationBuilder
import re
import cv2 
import numpy as np
import pytesseract
from pytesseract import Output
from matplotlib import pyplot as plt
import matplotlib.patches as patches
import time as time
import matplotlib.animation as animation

def extraction (format:dict, path:str):
    # 'C:\\Users\\zhouw\\OneDrive\\Documents\\vs\\python_p1\\image\\Inv_18715_from_Acure_Safety_West_Inc_14880_230504_213242-page-001.jpg'
    all_info = []
    all_file = []
    for root, dirs, file in os.walk(path):    
        all_file = file

    for pic in file:
        IMG_DIR = f"{path}\\{pic}"
        img = cv.imread(IMG_DIR)
        individual_info_list = []
        if img is None:
            sys.exit("Could not read the image.")

        cv.cvtColor(img, cv.COLOR_BGR2GRAY)

            
        
        for val in format.values():
            x = val[0]
            y = val[1]
            
            crop = img[x[1]:y[1], x[0]:y[0]]   # crop
            cv.rectangle(img,(x[0],x[1]),(y[0],y[1]),(0,255,0),2)   # find the box
            #cv.namedWindow('image', cv.WINDOW_NORMAL)  # Create a named window
            #cv.resizeWindow('image', img.shape[1], img.shape[0])  # Set window size to image dimensions

            #cv.imshow('image', img)
            b,g,r = cv2.split(crop)
            rgb_img = cv2.merge([r,g,b])

            sharpen_kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
            sharpen = cv2.filter2D(rgb_img, -1, sharpen_kernel)

    
            k = cv.waitKey(0) # 0  means wait for ever

            if k == ord("s"):
                cv.imwrite("starry_night.png", img)
    

            image = rgb_img
        #    cv.imshow('image',sharpen)
            d = pytesseract.image_to_data(crop, output_type=Output.DICT)

            #print('DATA KEYS: \n', d['text'])
            extracted_text = list(filter(lambda a: a != "", d['text']))
            tempStr = ''
            for i in d['text']:
                    tempStr += i
            individual_info_list.append(tempStr)
        
        all_info.append(individual_info_list)
    return all_info


