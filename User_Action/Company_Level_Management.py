import sys
sys.path.append("C:\\Users\\zhouw\\OneDrive\\Documents\\personal sci project\\vs\\ProjectIII")
import cv2, os, json, csv
from User_Action.Directory_Watch_Dog import Pdf_Watch_Dog
import threading

class CLM:
    def __init__(self, company_root_path):
        #* Comapny path establish
        self.company_root_path = company_root_path

        #* Missing folder is created for new added company and check if folder is accidently deteld
        try:
            self.TARGET_FOLDER_RECOVERY() #! this maybe redundent or may replace the similar function from SDM
        except Exception:
            print("reconvery is unnecessary")
        #*initialize DoNotDelete Folder
        self.position_data = Position(f"{self.company_root_path}\\DoNotDelete","position.json") 
        self.extraction_data = Data(f"{self.company_root_path}\\DoNotDelete", "data.json")  
        self.category_data = Category_Data(self.company_root_path) #! category needs to be init before Data Class
        self.category_data.create_category()
        self.extraction_data.set_category(self.category_data.get_category())
        
        #* ILM storage
        self.ilm = []

        #* Pdf_Observer Set up: the two function self.add, and self.deleted will be excuted by 
        pdf_file =Pdf_Watch_Dog(f"{self.company_root_path}", [self.add_image], [self.delete])
        pdf_observer = threading.Thread(target=pdf_file.file_change)
        pdf_observer.start()

        #! the following image function will be paused at this moment. Only pdf will be allowed
        #* Image Observer Set Up
        img_file =Pdf_Watch_Dog(f"{self.company_root_path}\\Images", [self.add], [self.delete])
        image_observer = threading.Thread(target=img_file.file_change)
        image_observer.start()

    #* go through the Images folder, for each image, create a ILM, then added to self.ilm[]
    def generate_image(self):

        img_dir = f"{self.company_root_path}\\Images"
        try:
            for root, dirs, files in os.walk(img_dir):
                for img in files:  
                    img_path = f"{img_dir}\\{img}"
                    self.ilm.append(ILM(img_path))

                break
        except Exception:
            print('path does not exist')

        if len(self.ilm) == 0:
            pass
    
    #* when a new pdf is passed into the folder    
    def add(self, data):
        print("action1")

    #* when a pdf is deleted from the folder
    def delete(self, data):
        print("action2")

    #* add new image to the ILM after new pdf is detected
    def add_image(self, img_path):
        new_ilm = ILM(img_path)
        self.ilm.append(new_ilm)

    #* delete an image when an new pdf is deleted
    def delete_image(self, img_path):
        for img in self.ilm:
            if img.get_img_path() == img_path:
                self.ilm.remove(img)

    #* return all the images
    def get_ilm(self):
        return self.ilm        

    #* return the position info of the current company, as a Position class inherited from SDM
    def get_position_data(self):
        return self.position_data

    #* return the position info of the current company, as a Data class inherited from SDM
    def get_extraction_data(self):
        return self.extraction_data  
    
    #* return the name of the current company
    def get_name(self):
        company_name = os.path.basename(self.company_root_path)
        return company_name
    
    #* get path of the current company
    def get_company_path(self):
        return self.company_root_path

    def TARGET_FOLDER_RECOVERY(self):
        #print("warning, missing files and folders are detected in ..., do you want to recover missing directory")
        print(f"checking for folder {self.get_name()}... ... ...")
        if not os.path.exists(f"{self.company_root_path}\\DoNotDelete"):
            os.mkdir(f"{self.company_root_path}\\DoNotDelete")
        else:
            print("DoNotDelete Check")
        if not os.path.exists(f"{self.company_root_path}\\DoNotDelete\\position.json"):
            with open(f"{self.company_root_path}\\DoNotDelete\\position.json", 'w') as new_file:
                pass
        else:
            print("position check")
        if not os.path.exists(f"{self.company_root_path}\\DoNotDelete\\data.json"):
            with open(f"{self.company_root_path}\\DoNotDelete\\data.json", 'w') as new_file:
                pass
        else:
            print("data check")

        if not os.path.exists(f"{self.company_root_path}\\Images"):
            os.mkdir(f"{self.company_root_path}\\Images")
        else:
            print("Images check")
        print(f"... ... ...checking finished fro {self.get_name()}")
    #TODO: Documentation: the following require new documentation
    def get_category(self):
        return self.category_data
    
    def get_category_list(self):
        pass

    def add_category(self, target_category):
        pass    

    def delete_category(self, target_category):
        pass

class ILM(CLM):
    def __init__(self, image_root_path):
        self.img_path = image_root_path


    def get_img_path(self):
        return self.img_path

    def get_img_name(self):
        img_name = os.path.basename(self.img_path)
        return img_name
    
    def get_cv_image(self):
        cv_img = cv2.imread(self.img_path)
        return cv_img
    
class SDM:
    #TODO: Redesign: make all secure data structure as json. 
    def __init__(self, data_path, file_name):
        self.data_path= data_path
        self.file_name = file_name
        self.file_exist = False

    def create_file(self):
        if not os.path.exists(f"{self.data_path}\\{self.file_name}"):
            with open(f"{self.data_path}\\{self.file_name}",'w') as file:
                self.file_exist = True
                pass
        
    def delete_file(self):
        os.remove(f"{self.data_path}\\{self.file_name}")
        self.file_exist = False

    def re_create_file(self):
        self.delete_file()
        self.create_file()
        self.file_exist = True

    def get_data_path(self):
        return self.data_path
    
    def get_file_name(self):
        return self.file_name    
    
class Position(SDM):
    #! needs to worry about updating category type
    def __init__(self, data_path, file_name):
        self.data_path = data_path
        self.file_name = file_name
        self.position = {}
        self.category_list = [] 

        super().__init__(data_path, file_name)

    def load_file(self):
        try:
            with open(f"{self.data_path}\\{self.file_name}",'r') as file:
                self.position = json.load(file)
        except Exception:
            print('file may be empty.')
        
    
    def update_category(self, category_key:str, pos1:list[float], pos2:list[float]):
        self.position[category_key] = [pos1, pos2]
    
    def remove_category(self, category_key:str):
        if category_key in self.position:
            del self.position[category_key]

    def add_category(self, category_key:str):
        self.position[category_key] = [[0,0],[0,0]]
    

    def get_position(self):
        return self.position

    def update_to_file(self):
        try:
            with open(f"{self.data_path}\\{self.file_name}",'w') as file:    
                json.dump(self.position, file) 

        except Exception:
            print('file may not exist.')

    def over_write_file(self, dict):
        try:
            with open(f"{self.data_path}\\{self.file_name}",'w') as file:    
                json.dump(dict, file) 
        except Exception:
            print("file may not exist")
        
    def set_category(self, category:list):
        self.category_list = category
    
    def get_category(self):
        return self.category_list
#!    
class Data(SDM):
    def __init__(self, data_path, file_name):
        self.data_path = data_path
        self.file_name = file_name
        self.data = []
        self.category_list = [] 
        super().__init__(data_path, file_name)

    def load_file(self):
        try:
            with open(f"{self.data_path}\\{self.file_name}",'r') as file:
                self.data = json.load(file)

        except Exception:
            print('file is empty')
    
    #! needs to worry about updating 'category' type
    def update_extracted_information(self, image_name, category_key:str, text:str):
        # [{}{}{}]
        target_image = None
        for image in self.data:
            if image['Image_Name'] == image_name:
                    target_image = image
        
        target_image[category_key] = text
                
    def remove_image(self, image_name:str):
        target_index = 0
        count = 0
        for image in self.data:
            if image['Image_Name'] == image_name:
                target_index = count
            
            count += 1
        print(target_index)
        self.data.pop(target_index)

    def add_image(self, category_list:list, text:list[str]):
        image_format = {}
        index = 0
        for category in category_list:
            image_format[category] = text[index] #! text should have the same length as the cateogyr list. 
            index += 1
        self.data.append(image_format)

    def get_data(self):
        return self.data

    def update_to_file(self):
        with open(f"{self.data_path}\\{self.file_name}",'w') as file:    
            json.dump(self.data, file) 

    def over_write_file(self, data:list[dict]):
        with open(f"{self.data_path}\\{self.file_name}",'w') as file:    
            json.dump(data, file, indent=4)

    def set_category(self, category:list):
        self.category_list = category    
    
#TODO: Redesign: this object may require a redesign to inherit SDM
#TODO Redesign: create_cateogory may need to split its funcionality to match the create_file in SDM
class Category_Data:
    def __init__(self, company_path):
        #* a default category list is given
        #! this default version is only for test purpose, 
        #! the actual default version is more complex
        self.company_path = company_path

        #! this list should be taken directly from folder
        self.category_list = []

    def get_category(self):
        return self.category_list
    
    def save_category(self, category_list):
        try:
            with open(f"{self.company_path}\\DoNotDelete\\Category\\category.json", 'w') as json_file:
                json.dump(category_list, json_file)
        except Exception:

            print("nothing exist")

    def create_category(self):
        try:
            #$ TODO: if statement may be more strict
            new_path = f"{self.company_path}\\DoNotDelete\\Category"
            if not os.path.exists(new_path):
                os.mkdir(new_path)
                #! this default version is only for test purpose, 
                #! the actual default version is more complex
                #! this list should be taken directly from folder
                with open(f"{new_path}\\category.json", 'w') as json_file:
                    default_category_list = ["invoice number", "invoice date"]
                    json.dump(default_category_list, json_file)
            else:
                with open(f"{new_path}\\category.json", 'r') as json_file:
                    self.category_list = json.load(json_file)
        except Exception:
            print('file existed already')

    def add_category(self, category):
        self.category_list.append(category)

    def delete_category(self, category):
        try:
            remove_index = self.category_list.index(category)
            self.category_list.pop(remove_index)
        except Exception:
            print(f"{category} is not found")
    
    def re_set_category(self):
        #TODO: Important Notice: This content of category_list needs to be re-def 
        self.category_list = [] 


if __name__ == "__main__":
    
    #$ CLM test
    test_company_root_path = f"C:\\Users\\zhouw\\OneDrive\\Documents\\vs\\ProjectIII\\Test_Resource\\company_test\\CompanyI"
    clm = CLM(test_company_root_path) 
    '''
    clm.generate_image() #! CLM needs to be called manually 
    test_list = clm.get_ilm()
    print(test_list)
    for item in test_list:
        print(item.get_img_path())
        print(item.get_img_name())
    
    #$ SDM test
    baffin = f"C:\\Users\\zhouw\\OneDrive\\Documents\\vs\\ProjectIII\\Test_Resource\\invoice_test_folder_beta\\baffin"
    sdm = SDM(baffin)
    sdm.get_position_list()
    data_list = [{'Country_Name': 'baffin', 'Image_Name': '364133.jpg', 'invoice_number': 'error code 333', 'invoice_date': 'error code 333'},
    {'Country_Name': 'baffin', 'Image_Name': '374128.jpg', 'invoice_number': 'error code 333', 'invoice_date': 'error code 333'}
    ]
    sdm.update_extracted_data_list(data_list)

    
    new_dict =  {"invoice number": [[1359.0799759964452, 122.37234806801712], [1449.9511393466041, 157.32279551038596]], "invoice date": [[1359.0799759964452, 178.29306397580717], [1456.9412288350782, 203.923392100211]]}
    test_path = 'C:\\Users\\zhouw\\OneDrive\\Documents\\vs\\ProjectIII\\Test_Resource\\Random File'
    position = Position(test_path, "position.json")
    print(position.get_data_path())
    position.create_file()
    position.load_file()
    print(position.get_position())
    print(type(position.get_position()))
    position.update_category('test update', [1,1], [2,2])
    print(position.get_position())
    position.add_category('add update')
    position.remove_category('test update')
    print(position.get_position())
    position.update_to_file()
    position.over_write_file(new_dict)
    
    #$ SDM Test
    test_path = 'C:\\Users\\zhouw\\OneDrive\\Documents\\vs\\ProjectIII\\Test_Resource\\Random File\\DoNotDelete'
    test_category = ['Country_Name', 'Image_Name', 'invoice_number', 'invoice_date']
    test_data= [
                    {"Country_Name": "baffin", "Image_Name": "364133.jpg", "invoice_number": "error code 333", "invoice_date": "error code 333"},
                    {"Country_Name": "baffin", "Image_Name": "374128.jpg", "invoice_number": "error code 333", "invoice_date": "error code 333"}
                    ]
    position = Position(test_path, "position.json")
    data = Data(test_path, 'data.json')
    data.create_file()
    data.over_write_file(test_data)
    data.load_file()
#    print(data.get_data())
#    print(type(data.get_data()))
    data.add_image(test_category,['baffin', '321341.jpg','a','b'])
    data.remove_image('321341.jpg')
    data.update_extracted_information('374128.jpg','invoice_number', 'error code 444')
    print(data.get_data())
    data.set_category(test_category)
    print(data.get_category())
    print(position.get_file_name())
    print(data.get_file_name())
    data.add_image( test_category, ['baffin', '321341.jpg','a','b'])
    data.update_to_file()
    

    #$ Cateogory Test        
    test_category = Category_Data(test_company_root_path)
    test_category.create_category()
    print(test_category.get_category())
    test_category.delete_category('invoice date')
    print(test_category.get_category())
    test_category.save_category(test_category.get_category())
    test_category.add_category('invoice date')
    test_category.save_category(test_category.get_category())
    '''

