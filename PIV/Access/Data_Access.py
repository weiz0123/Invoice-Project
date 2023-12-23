import os
from numpy import ndarray
from Data_Management.Company_Level_Management import Company_Level_Management

DEFAULT_PATH = "C:\\Users\\zhouw\\OneDrive\\Documents\\personal sci project\\vs\\ProjectIV\\Test_Resource\\company_test"


class Data_Access:
    """
    Purpose:
    1. access data
    2. format data for representation
        - most formats are done on company level
        - image level and data level are done by Company_Level_Management
    3. store data

    Communication:
    1. User_Level_Management
    """
    _instance = None

    def __new__(cls, data_access_root_path: str):
        if cls._instance is None:
            cls._instance = super(Data_Access, cls).__new__(cls)

        # data_access_root_path is the path of the directory that has the highest hierarchy in Data Storage
        # this variable should not be accessed from this class
        cls.data_access_root_path = data_access_root_path

        # this list represents a model of companies. each element represents a "company manager" for the target company
        cls.class_level_management_list: list = []

        # search and add all the company_manager for all company directories
        cls._generate_company_level_management(cls)

        return cls._instance

    '''===Internal Class Implementation: the following methods cannot be accessed by other classes==='''

    def _generate_company_level_management(self):
        """
         1. generates a list of Class_Level_Management for all the companies in the directory data_access_root_path
         2. Each Class_Level_Management will manage only one targeted company folder.
         3. To create a Class_Level_Managemeynt for the company folder, the directory path of company
            will be passed into the Class_Level_Management
          param:  None
          return: None
        """

        for directory, folder, file in os.walk(f"{self.data_access_root_path}"):
            for company in folder:
                company_path = f"{self.data_access_root_path}\\{company}"
                new_company: Company_Level_Management = Company_Level_Management(company_path)
                self.class_level_management_list.append(new_company)
            break
        print("generate_company_level_management succeed\n")

    def _get_company_level_management(self, company_name: str) -> Company_Level_Management:
        """
         1. generates a list of Class_Level_Management for all the companies in the directory data_access_root_path

          param:  (company_name:str)
          return: Company_Level_Management
        """
        for company_manager in self.class_level_management_list:
            if company_manager.get_company_root_path() == f"{self.data_access_root_path}\\{company_name}":
                return company_manager
        raise Exception("Data_Access._get_company_level_management -> company company_manager not found")

    '''===External Class Implementation: the following methods cannot be accessed by this class ==='''

    def get_data_access_root_path(self) -> str:
        """
        param: None
        return: self.data_access_root_path
        """
        return self.data_access_root_path

    def get_company_name_list(self) -> list[str]:
        """
        1. this loop through class_level_management_list, get the name from each company manager,
        2. then store the name in a list
        param:  None
        return: a list of company names
        """
        company_name_list = []
        for company_manager in self.class_level_management_list:
            company_name_list.append(company_manager.get_company_name())

        return company_name_list

    def get_company_targeted_image(self, target_company_name: str, target_img_name: str) -> ndarray:
        """
        1. when user attempts to find a specific image from a company, 2 parameters are required. target_company_name is
           used to locate the designated company_manager. the company_manager will take target_img_name as its parameter
           and locate the image.
        2. if the target_img_name is None; then, the first image will be returned. Since finding the image is a task for
           company_manager, this case will be handled by Class_Level_Management
        param (target_company_name: str, target_img_name: str)
        return ndarray that represents image
        """
        company_manager: Company_Level_Management = self._get_company_level_management(target_company_name)
        return company_manager.get_cv_image(target_img_name)

    def get_company_image_name_list(self, target_company_name: str):
        """
        1. when user attempts to find a list of image name from a company, target_company_name is
           used to locate the designated company_manager.
        2. the company_manager will take target_img_name as its parameter
           and find all the image name for that company
        param (target_company_name: str, target_img_name: str)
        return ndarray that represents image
        """

        company_manager: Company_Level_Management = self._get_company_level_management(target_company_name)
        return company_manager.get_image_name_list()

    def get_category_list(self, company_name: str) -> list[str]:
        """
        * further design, documentation will be included for this method.
        """
        target_company_manager: Company_Level_Management = self._get_company_level_management(company_name)
        category_list: list[str] = target_company_manager.get_category_list()
        return category_list

    def get_extracted_data_for_all_image(self, company_name: str) -> dict[dict]:
        target_company_manager: Company_Level_Management = self._get_company_level_management(company_name)
        extracted_data: dict[dict] = target_company_manager.get_extracted_data()
        return extracted_data

    def get_extracted_data_for_targeted_image(self, company_name: str, image_name: str):
        extracted_data: dict[dict] = self.get_extracted_data_for_all_image(company_name)
        for image in extracted_data.keys():
            if image == image_name:
                return extracted_data[image]

        raise Exception("Data_Access: get_extracted_data_for_target_image() -> No image found")

    def get_position_for_all_category(self, company_name: str) -> dict:
        target_company_manager: Company_Level_Management = self._get_company_level_management(company_name)
        position_data: dict = target_company_manager.get_position_list()
        return position_data

    def get_position_for_target_category(self, company_name: str, category_key: str):
        position_data: dict = self.get_position_for_all_category(company_name)
        for category in position_data.keys():
            if category == category_key:
                return position_data[category]

        raise Exception("Data_Access: get_position_for_target_category() -> no position found")

    def update_data(self, company_name: str, command: str, image_name: str, category_key: str = None, text: str = None):
        target_company_manager: Company_Level_Management = self._get_company_level_management(company_name)
        target_company_manager.update_data_info(command, image_name, category_key, text)

    def update_position(self, company_name: str, command: str, category_key: str = None, pos1: list[float] = None,
                        pos2: list[float] = None):
        target_company_manager: Company_Level_Management = self._get_company_level_management(company_name)
        target_company_manager.update_position_info(command, category_key, pos1, pos2)

    def update_category(self, company_name: str, category_list: list[str]):
        target_company_manager: Company_Level_Management = self._get_company_level_management(company_name)
        target_company_manager.update_category(category_list)

    def update_to_file(self, company_name: str):
        target_company_manager: Company_Level_Management = self._get_company_level_management(company_name)
        target_company_manager.update_to_file()

    def get_company_path(self, company_name: str):
        target_company_manager: Company_Level_Management = self._get_company_level_management(company_name)
        return target_company_manager.get_company_path()
