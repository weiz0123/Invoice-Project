from PyQt6.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QWidget, QGraphicsView,QWidget, QLabel, QFrame, QComboBox, QPushButton, QHBoxLayout, QTabWidget, QScrollArea, QProgressBar, QDialog)
from Folder_Management import Folder, Invoice_Source_Management, Folder_Management
import os
# TODO: This class needs to be only serving for comboBox
class ComboBox_Data_Transfer():
    '''
    Data transfer fromm A -> B

    add to the Data transfer node, naming with send_, deliver_

    receive from the Data transfer node, naming get_,  recieve_
    
    other data process, set_ find_ install_...
    '''
    '''
    deliever to Qobject requries name
    get from Qobject only requires object
    
    '''
    def __init__(self, folder:Folder, management:Folder_Management,   invoice_source_management:Invoice_Source_Management):
        self.__comboBox_Index = {} # key: comboBox_name : index of the selected company name in the comboBox
        self.__comboBox_item = {} # Key: comboBox_name
        #self.__current_company_path = None #TODO: needs to become a dictionary
        self.__current_company_path = {}
        self.__folder : Folder = folder
        self.__management: Folder_Management = management
        self.__invoice_management: Invoice_Source_Management = invoice_source_management


    def deliever_index(self, comboBox:QComboBox ) -> None:
        '''
        add current selected index -> A deliver info
        '''
        index = comboBox.currentIndex()
        comboBox_name = comboBox.objectName()
        self.__comboBox_Index[comboBox_name] = index
        print('index delievered from comboBox...')

    
    def get_index(self, comboBox:QComboBox) -> int:
        '''
        get current selected index -> B recieve info
        '''
        index = self.__comboBox_Index[comboBox.objectName()]
        print(f'index recieved from comboBox...{index}')
        return index
        

    def deliever_comboBox_list(self, comboBox_name:str, comboBox_List:list) -> None:
        '''
        This method will take in a target comboBox and set the comboBox list to the target combobBox
        '''
        self.__comboBox_item[comboBox_name] = comboBox_List
        print('list delievered to comboBox...')

    def get_comboBox_list (self, comboBox:QComboBox) -> list:
        comboBox_item = self.__comboBox_item[comboBox.objectName()]
        comboBox.addItems(comboBox_item)

        # the following section solves the issue of the first item is not automatically processed before any click of the combobox
        first_commpany_path = self.__folder.get_folder().getItem(0).get_root() 
        self.__current_company_path[comboBox.objectName()] = first_commpany_path

        print(f"list recieved for comboBox...{comboBox_item}")
        print(f'First Selected Company Path is {self.__current_company_path[comboBox.objectName()]}')
        print(len(self.__current_company_path))
        return comboBox_item


    def find_commpany_path(self, comboBox:QComboBox) -> str:
        '''
        This method returns each company's folder'path by taking the index taken from the item selected in the combBox
        '''
        current_company_index = self.get_index(comboBox)   
        current_commpany_path : str = self.__folder.get_folder().getItem(current_company_index).get_root()
        self.__current_company_path[comboBox.objectName()] =  current_commpany_path 
        print(f'Current Selected Company Path is {current_commpany_path}')
        return (self.__current_company_path[comboBox.objectName()])
        # TODO NEED DICTIONARY


    def find_first_images_path(self,comboBox_name:str) -> list[str]:
        #"C:\\Users\\zhouw\\OneDrive\\Documents\\vs\\Invoice Processing\\python_p3_Modulization\\test Folder\\baffin\\images\\364133.jpg"
    
        for key, values in self.__current_company_path.items():
            print(key)
        images_path = f"{self.__current_company_path[comboBox_name]}\\images"
        #TODO: cannot go backward: Current solution: loop through os.walk_path
        img_list = []
        for root, directories, files in os.walk(images_path):
            for img in files:
                img_list.append(f"{images_path}\\{img}")
        
        return img_list
    




class textBox_Data_Transfer:
    pass


class Data_Position_Transfer:

    def __init__(self) -> None:
        '''
        data name stores all the data names that will be extracted from a single image
        '''
        self.__data_name= []
        self.__data_position = {} # data name : position [[x1,y1], [x2,y2]]


    def set_data_position(self, data_name:str, position1:list, position2:list) -> None:
        '''
        acquire position of the extracted data with the rectangle information
        '''
        self.__data_position[data_name] = [position1, position2]

    def set_data_name(self, data_name:list) -> None:
        '''
        acquire list information from the comboBox
        '''
        self._data_name = data_name

    def search_data_position(self, data_name:str):
        '''
        search the rectangle position for a extracted data name
        '''
        return self.__data_position[data_name]

class File_Explorer_Data_Transfer():
        def __init__(self, folder:Folder, management:Folder_Management,   invoice_source_management:Invoice_Source_Management):
            self.__ROOT = folder.get_root()

        def get_root_path(self):
            return self.__ROOT
