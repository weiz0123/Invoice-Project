import sys
sys.path.append("C:\\Users\\zhouw\\OneDrive\\Documents\\personal sci project\\vs\\ProjectIII")
from User_Action.Data_Access import Data_Access
from User_Action.Process_Access import Process_Access
from pdf2image import convert_from_path
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QWidget

import os

#TODO Redesign: any customization will be excpet updating company or image will be postpond to the next version
#TODO Redsign: should listener be set in process or data access 
#! IMPORTNAT NOTCIE
#TODO: Redsign: all update data should be process through class Proccess Access
#TODO PAUSE !!!
default_path = "C:\\Users\\zhouw\\OneDrive\\Documents\\vs\\ProjectIII\\Test_Resource\\company_test"
class ULM(QWidget):
    update_company_comboBox_signal = pyqtSignal()
    def __init__(self, root_path):
        super().__init__()
        self.data = Data_Access(root_path)
        self.first_init()
        #* self.data.get_clm() only return after self.first_init().
        self.process = Process_Access(root_path, self.data.get_clm())
        self.init_connection_between_process_and_user()

    def first_init(self):
        self.data.generate_company()

    #TODO: Documentation:
    def init_connection_between_process_and_user(self):
        self.process.company_comboBox_refresh.connect(self.update_company_comboBox_emitter)
        print("user to process access connection established")
    
    def update_company_comboBox_emitter(self):
        self.update_company_comboBox_signal.emit()
        print("emmiteed to update")
    #$===================

    def display_company_name(self):
        company_name_list = self.data.get_company_list()
        return company_name_list

    def display_extraction_category(self):
        category_name_list = self.data.get_category_list()
        return category_name_list
    
    def display_first_image_of_company(self, company_name):
        try:
            cv_image = self.data.get_company_first_image(company_name)
            return cv_image
        except Exception:
            print('no image found')
    #TODO: Documentation: doc required
    def display_all_image(self, company_name):
        all_cv_img = []
        for ilm in self.data.get_ilm():
            cv_img = ilm.get_cv_image()
            all_cv_img.append(cv_img)
        return all_cv_img
    
    #TODO: Redesgin + Documentation : the following warning needs re-documentation for the current class and class Process_Access
    #! convert_existing_pdf is transfered to class Process_Access

    #TODO: the following needs further detailed documentation
    def extracted_target_image_information(self,img, pos1, pos2) -> str:
        croped_img = self.process.crop_image(img, pos1, pos2)
        extracted_text = self.process.extract_data_from_image(croped_img)
        return extracted_text
    
    #TODO: Documentation: the following function will be inherited from function above
    #TODO Manipulation: require minor change, the following only presented with example data such as the company_name and image_name etc.
    '''
    def ____________extract_target_company_image_sample(self, company_name):
        company_name = 'CompanyI'
        image_name = 'Invoice_000000000664731.jpg'
        category_list = new_user.get_category()
        position = {"invoice number": [[1331.588176033331, 137.08295673159], [1503.762524616663, 196.5613680603774]], "invoice date": [[229.4457067143735, 826.0155946267541], [413.6425134104252, 857.0190175359905]]}
        data = []
        data.append({"Company name":company_name, "Image name": image_name})
        for key, value in position.items():
            pos1 = value[0]
            pos2 = value[1]
            data[0][key] = new_user. extracted_target_image_information(image,pos1,pos2)
        return data
    '''
    
    def extract_target_company_image(self, company_name):
        clm = self.process.search_target_clm(company_name)
        ilm = clm.get_ilm()
        all_pdf_data = []
        for img in ilm:
            image_name = img.get_img_name()
            #* load position data from position json file
            clm.get_position_data().load_file()
            position = clm.get_position_data().get_position()
            #{"invoice number": [[1331.588176033331, 137.08295673159], [1503.762524616663, 196.5613680603774]], "invoice date": [[229.4457067143735, 826.0155946267541], [413.6425134104252, 857.0190175359905]]}
            data = []
            data.append({"Company name":company_name, "Image name": image_name})
            for key, value in position.items():
                pos1 = value[0]
                pos2 = value[1]
                data[0][key] = self.extracted_target_image_information(img.get_cv_image() ,pos1 ,pos2)
            all_pdf_data.append(data[0])
        print(all_pdf_data)

    def update_extract_position_information(self, company, category, pos1, pos2):
        self.process.update_extract_positon(company, category, pos1, pos2)
        
    #! 
    #TODO: Documentation: the following needs to be documented
    #TODO Redesign: postpond for the next version

    def update_company_comboBox(self):
        self.process
    def get_category(self):
        return self.data.get_category_list()
    
    def update_one_category(self, category):
        pass

    def update_all_category(self, category_list):
        pass

    def reset_category(self):
        pass


    

if __name__ == "__main__":
    pass
    #new_user = ULM(default_path)

    '''#$ (t1) data access test including: 
        1. get commpany_list
        2. convert company images that pre-existed in the folder before the init process
        3. get the first image of a targeted company

       #$ (t2) data operation test including:
       1. extract position from image a targeted company
       2. update extract position image of a targeted commpany
       3. read from extracted information and process through the rest image

       4. save extract text.
       5. save to local csv

       6. save / update category for each company. 

       #$ (t3) test for updating during the process.
    '''
    #$ T1
    '''
    #* test 1 get commpany_list
    all_company = new_user.display_company_name()
    
    #* test 2 convert company images that pre-existed in the folder before the init process
    for company in all_company:
        #* find path of each company
        company_path = f"{default_path}\\{company}"
        for directory, dirnames, filenames in os.walk(company_path):
            for pdf in filenames:
                pdf_path = f"{company_path}\\{pdf}"
                #! assume there is no un-required files
                try:
                    new_user.convert_existing_pdf(company, pdf_path)
                except Exception:
                    print(f'{pdf} doesnt exist')
            break

    #* test 3 get the first image of a targeted company
    try:
        #*  this return a cv image
        image = new_user.display_first_image_of_company("CompanyI")
        print(image)
    
    except Exception:
        print("no image found under the company")
    '''
    #$ T2
    '''
    #* test 1 extract position from image a targeted company
    #TODO: Redesign: add get_company target category to Data_Access, including the process of updating category for a targeted company
    company_name = 'CompanyI'
    image_name = 'Invoice_000000000664731.jpg'
    category_list = new_user.get_category()
    position = {"invoice number": [[1331.588176033331, 137.08295673159], [1503.762524616663, 196.5613680603774]], "invoice date": [[229.4457067143735, 826.0155946267541], [413.6425134104252, 857.0190175359905]]}
    data = []
    data.append({"Company name":company_name, "Image name": image_name})
    for key, value in position.items():
        pos1 = value[0]
        pos2 = value[1]
        data[0][key] = new_user. extracted_target_image_information(image,pos1,pos2)
    print(data)

    #* test 2 update extract position image of a targeted commpany
    new_user.update_extract_position_information('CompanyI', 'invoice number', [2,3], [4,5])

    #* test 3 read from extracted information and process through the rest image
    position = new_user    
    '''