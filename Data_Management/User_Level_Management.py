from numpy import ndarray

from Access.Data_Access import Data_Access
from Access.Process_Access import Process_Access


class User_Level_Management:
    def __init__(self, root_path: str):
        self.data_access: Data_Access = Data_Access(root_path)
        self.process_access: Process_Access = Process_Access(root_path)

    def request_company_name_list(self) -> list[str]:
        return self.data_access.get_company_name_list()

    def request_img_name_list(self, company_name: str) -> list[str]:
        return self.data_access.get_company_image_name_list(company_name)

    def request_category_type(self, company_name: str) -> list[str]:
        pass

    def request_cv_img(self, company_name: str, img_name: str) -> ndarray:
        return self.data_access.get_company_targeted_image(company_name, img_name)

    def request_Category_Position(self, company_name: str) -> list[[int, int], [int, int]]:
        pass

    def request_ROI_image(self, company_name: str, img_name: str, category_type: str):
        pass
