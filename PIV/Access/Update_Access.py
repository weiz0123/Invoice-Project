import os.path

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import Data_Management.Secure_Data_Management
from Data_Management.Company_Level_Management import Company_Level_Management
from Data_Management.Image_Level_Management import Image_Level_Management
from Data_Management.Secure_Data_Management import Category_Manager, Data_Management, Position_Data_Management
from Access.Data_Access import Data_Access
from Observer.Update_Observer import Update_Observer
import threading


class Update_Access:
    """
    Purpose:
    1. assist Data_Access to access updated data
    2. assist to refresh User_Level_Management and Operation Access
    2. currently only observing Company Directory and Pdf Directory


    Communication:
    1. User_Level_Management
    2. Data_Access -> .class_level_management_list
    3: Update_Observer
    """

    def __init__(self, data_access: Data_Access, User = None):
        self.company_level_management_list: list = data_access.company_level_management_list
        self.root_path: str = data_access.get_data_access_root_path()
        # pdf_update = Pdf_Update(self.company_level_management_list)
        company_update = Company_Update(data_access)


class Company_Update:
    def __init__(self, data_access: Data_Access):
        self.data_access = data_access
        self.root_path: str = data_access.get_data_access_root_path()
        self.company_level_management_list: list = data_access.company_level_management_list
        self.start()

    def start(self):
        company_observer: Update_Observer = Update_Observer(0, self.root_path, self.observer_add_receiver)
        thread = threading.Thread(target=company_observer.start)
        thread.start()

    def observer_add_receiver(self, target_path: list[str], _id: int, command: str):

        print(f"id {_id}, manager for {self.root_path}, updated path: {target_path}")
        print(len(self.company_level_management_list))
        if command == "create":
            company_manager: Company_Level_Management = Company_Level_Management(target_path[0])
            self.company_level_management_list.append(company_manager)
        else:
            company_name: str = os.path.basename(target_path[0])
            #print(company_name)
            company_manager_index = self.data_access.get_company_name_list().index(company_name)
            self.company_level_management_list.pop(company_manager_index)

        print(len(self.company_level_management_list))
        target_path.clear()


class Pdf_Update:

    def __init__(self, company_level_management: list):
        self.company_level_management: list[Company_Level_Management] = company_level_management
        self.company_update = {}
        self.pdf_update = {}
        self.clear_list = []
        self.start()

    '''===Internal Class Implementation: the following methods cannot be accessed by other classes==='''

    def start(self):
        """
        1. create a pdf observer for each company
        return:
        """
        i: int = 0
        for company_manager in self.company_level_management:
            company_path = company_manager.get_company_path()
            company_observer: Update_Observer = Update_Observer(i, company_path, self.observer_receiver)
            thread = threading.Thread(target=company_observer.start)
            self.company_update[i] = [company_path, company_observer, thread]
            thread.start()
            i += 1

    def observer_receiver(self, target_path: list[str], _id: int):
        # corresponding id will show up
        print(f"id {_id}, manager for {self.company_update[_id][0]}, updated path: {target_path}")


def main():
    DEFAULT_PATH = "C:\\Users\\zhouw\\OneDrive\\Documents\\personal sci project\\vs\\ProjectIV\\Test_Resource\\company_test"
    data_access = Data_Access(DEFAULT_PATH)
    update_access = Update_Access(data_access)


if __name__ == "__main__":
    main()
