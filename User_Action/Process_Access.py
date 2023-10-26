import sys
sys.path.append("C:\\Users\\zhouw\\OneDrive\\Documents\\personal sci project\\vs\\ProjectIII")
import cv2, os, json, csv
from User_Action.Directory_Watch_Dog import Folder_Watch_Dog
import threading
from User_Action.Company_Level_Management import CLM
import os
from pdf2image import convert_from_path
import cv2 as cv
from PyPDF2 import PdfReader
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
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QWidget
#TODO Documentation: The following class require a complete documentation
class Process_Access(QWidget):
    company_comboBox_refresh = pyqtSignal()
    def __init__(self, root_path, clm_list):
        super().__init__()
        self.root_path = root_path


        #* this is taken from Data Access through User_Level_Management
        self.clm = clm_list 

        #!
        #TODO: EMERGENCY
        #* Company Observer Set Up
        folder =Folder_Watch_Dog(self.root_path, [self.add, self.update_company_comboBox] , [self.delete])
        company_observer = threading.Thread(target=folder.folder_change)
        company_observer.start()


    #* company add action will be performed in here 
    #! this function is auto called

    def add(self, data):

        # this will append the new added company to the active clm list
        #$ the reason why this list update is due to the mutability of a list
        for company_path in data:
            new_company = CLM(company_path)
            self.clm.append(new_company)
            new_company.generate_image()
        print(f"from process access after adding new company {self.clm}")

    #* company delete action will be performed in here
    #! this function is auto called
    def delete(self, data):

        # this will delete the new added company to the active clm list
        for company_path in data:
            count = 0
            for company in self.clm:
                if company_path == company.get_company_path():
                    self.clm.pop(count)
                count += 1
        #print(self.clm)

    #TODO: <<<<TAKE FROM HERE>>>> 2 task. add new company, add new pdf, delete a company, delete old pdf. 1 task, view all the image. 1 task view all the image with rectangle drawn...
    #! the following will be the 4 updating process
    # TODO: Documentation This signal is emitted to ulm. the ulm is connected to User_Interface then to operation access
    def update_company_comboBox(self):
        self.company_comboBox_refresh.emit()
        print("emitted")

    def crop_image(self, img, pos1:list, pos2:list):
        #cv image assuming for var img
        croped_img = img[int(pos1[1]):int(pos2[1]), int(pos1[0]):int(pos2[0])]
        return croped_img
    
    def extract_data_from_image(self, cropped_img) -> str:
        
        d = pytesseract.image_to_data(cropped_img, output_type=Output.DICT)
        extracted_text = list(filter(lambda a: a != "", d['text']))
        tempStr = ''
        for i in d['text']:
                tempStr += i
        
        return tempStr
    
    def convert_existing_pdf(self, company_name, pdf_path):
        save_path = f"{self.root_path}\\{company_name}\\Images"

        try:    
            images = convert_from_path(pdf_path)
            for i, image in enumerate(images):
                temp_str = pdf_path[0:len(pdf_path)-4]
                last_index = temp_str.rfind("\\")+1
                image.save(f'{save_path}\\{pdf_path[last_index:len(pdf_path)-4]}.jpg', "JPEG")
        
        except Exception as e:
             if os.path.exists(pdf_path) is False:
                  raise Exception (f"pdf path: <<{pdf_path}>> cannot be found or doesnt exsit")
             elif os.path.exists(save_path) is False:
                  raise Exception(f"save coverted image path: <<{save_path}>> cannot be found or doesnt exsit")
             else:
                  print(e.args)
                  raise Exception(f"errors when converting pdf to jpg from <<{pdf_path}>> to <<{save_path}>>")

    #TODO: Important Notice: This function is re-designed          
    def search_target_clm(self, target_company_name):
        for clm in self.clm:
            print(clm.get_name())
            if clm.get_name() == target_company_name:
                return clm
            
        raise Exception("no company folder has found")
    
    #! this will be linked to operation class update position function
    #TODO: Documentation: the following 3 function requires documentation
    def update_extract_positon(self,company, category, pos1, pos2 ):
        clm :CLM = self.search_target_clm(company)  # find company
        data = clm.get_position_data() #
        data.update_category(category, pos1, pos2)
        data.update_to_file()

    def get_position(self, company_name):
        clm :CLM = self.search_target_clm(company_name)
        data = clm.get_position_data()
        data.load_file()
        data.get_position()
        #TODO: Important Notice: this is an unfinished function to get data from file
