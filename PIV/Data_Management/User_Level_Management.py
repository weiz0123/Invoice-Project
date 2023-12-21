from numpy import ndarray

from Access.Data_Access import Data_Access
from Access.Process_Access import Process_Access

# This path is for testing purpose
DEFAULT_PATH = "C:\\Users\\zhouw\\OneDrive\\Documents\\personal sci project\\vs\\ProjectIV\\Test_Resource\\company_test"


class User_Level_Management:
    """
    Purpose:
    1. a model that mimic user's action
    2. receiving request from GUI
    3. pass formatted data for display

    Communication:
    1. User_Interface_Control
    2. Operation_Access -> will contain a copy of User_Level_Management
    3. Process Access
    4. Data Access
    5. Update Access -> will contain a copy of User_Level_Management
    """

    def __init__(self, root_path: str):
        # user level management will have full access to write and read files in root_path
        # through data_access and process_access
        self.root_path: str = root_path
        self.data_access: Data_Access = Data_Access(root_path)
        self.process_access: Process_Access = Process_Access(root_path)

    # The following controls are from data_access
    def display_company_name(self) -> list[str]:
        """
        return: a full list of company name at current time
        """
        company_name: list = self.data_access.get_company_name_list()
        return company_name

    def display_extraction_category(self) -> list[str]:
        """
        return: return a full list of extraction category at current time
        """
        category_name: list = self.data_access.get_category_list()
        return category_name

    def display_first_image(self, company_name: str) -> ndarray:
        """
        1. if the no image stored, exception is raised but not handled at the time
            * further design and refine is required for this exception

        param: company_name
        return:  the first cv image from the image storage
        """
        img_name_list: list = self.data_access.get_company_image_name_list(company_name)
        if len(img_name_list) >= 1:
            first_img_name: str = img_name_list[0]
        else:
            raise Exception("fail to display cv image")
        return self.data_access.get_company_targeted_image(company_name, first_img_name)

    def display_image_name(self, company_name: str) -> list[ndarray]:
        """
        1. if the image list has length of zero, then it raise exception but not handled at the time
            * further design and refine is required for this exception

        param: company_name
        return: a full list of image name at the time
        """
        img_name_list: list = self.data_access.get_company_image_name_list(company_name)
        if len(img_name_list) >= 1:
            return img_name_list
        else:
            raise Exception("fail to display image name from User_Level_Management")

    # The following controls are from Process Access
    # {"invoice number": [[1337.7434768516018, 130.97587920695787], [1491.2558028559597, 202.7800316928674]],
    # "invoice date": [[245.825158014154, 821.7813462265678], [372.101426179029, 861.3974303567247]]}
    def get_extracted_text_from_roi(self, cv_img: ndarray, position_information: dict) -> str:
        """
        1. using the extraction
        param cv_img: OpenCv_img position_information: e.g. ->
        {"invoice number": [[1337.7434768516018, 130.97587920695787], [1491.2558028559597, 202.7800316928674]]}

        return: the target text from the image i.e. roi
        """
        pos1: list = position_information.values()[0][0]
        pos2: list = position_information.values()[0][1]
        target_cv_img_roi = self.process_access.crop_for_roi(cv_img, pos1, pos2)
        target_text = self.process_access.text_extraction(target_cv_img_roi)
        return target_text

    def convert_this_pdf_to_image(self, company_name: str, pdf_path: str) -> bool:
        """
        param company_name: str, pdf_path
        return truth value, if converted successfully, return ture, otherwise false
        """
        try:
            self.process_access.convert_existing_pdf(company_name, pdf_path)
            return True
        except ValueError(f"unable to convert {pdf_path} to jpg"):
            return False
