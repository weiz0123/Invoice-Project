import sys
sys.path.append("C:\\Users\\zhouw\\OneDrive\\Documents\\personal sci project\\vs\\ProjectIII")
from User_Action.Company_Level_Management import CLM
from User_Action.Directory_Watch_Dog import Folder_Watch_Dog
import os
import threading

class Data_Access:
    #TODO: Review Prev: Review Data Access Plan: there may be conflict / error and design flaw with operation and update access 
    def __init__(self, root_path):
        self.root_path = root_path
        #* activate all current company
        self.clm = []

    #$ Documentation: Document and Re-Document the following 2 function
    def generate_company(self):
        for directory, folder, file in os.walk(self.root_path):
            for company in folder:
                company_path = f"{self.root_path}\\{company}"
                new_company = CLM(company_path)
                self.clm.append(new_company)
                new_company.generate_image()
                
            break

    def get_clm(self):
        return self.clm

    def get_company_list(self):
        company_name_list = []
        for clm in self.clm:
            company_name_list.append(clm.get_name())

        return company_name_list
    
    #TODO: Redesign: this function may be removed from this class. since update info has been assigned to Process_Access
    def search_target_clm(self, target_company_name):
        for clm in self.clm:
            #print(clm.get_name())
            if clm.get_name() == target_company_name:
                return clm
            
        raise Exception("no company folder has found")
    #!
    #TODO:Documentation: new function added to get all image from a target company
    def get_ilm(self, company_name):
        
        #* company name will be passed from combobox
        try:
            clm = self.search_target_clm(company_name)
            ilm = clm.get_ilm()
            return ilm
        except Exception:
            print(" company name doesnt exist, cannot find the target ilm list")

    def get_company_first_image(self, company_name):
        for clm in self.clm:
            #print(clm.get_name())
            #print(company_name)
            if clm.get_name() == company_name:
                first_image_ilm = clm.get_ilm() [0]
                return first_image_ilm.get_cv_image()
        raise Exception("first company image is not found")
        
    def get_category_list(self):
        return ["invoice number", "invoice date"]

    def get_root_path(self):
        return self.root_path
    
    def update_company_list(self):
        pass
    
    #TODO: Documentation: the following functionality will be build in the next version
    def get_company_target(self, company):
        pass

    def update_category(self, category):
        pass

    
    #! the following 3 function may require re-design. 
    #! since these functions deal with gui display.
    #! possible solution is to make them only return the necessary data

    def display_sample_image(self):
        pass

    def display_all_image(self):
        pass

    def erase_position_info(self):
        pass

if __name__ == "__main__":
    test_path = "C:\\Users\\zhouw\\OneDrive\\Documents\\vs\\ProjectIII\\Test_Resource\\invoice_test_folder_beta"
    new_data_manage = Data_Access(test_path)
    new_data_manage.generate_company()
    new_data_manage.get_company_list()
'''
    test_clm:CLM = new_data_manage.search_target_clm("bigk")
    ilm = test_clm.get_ilm() # -> list
'''
    