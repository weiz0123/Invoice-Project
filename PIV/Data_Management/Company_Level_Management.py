import os, cv2
from numpy import ndarray
from Data_Management.Image_Level_Management import Image_Level_Management
from Data_Management.Secure_Data_Management import Position_Data_Management
from Data_Management.Secure_Data_Management import Data_Management
from Data_Management.Secure_Data_Management import Category_Manager


class Company_Level_Management:
    """
    Purpose:
    Communication:
    """

    def __init__(self, company_root_path):
        # store the company folder's path
        self.company_root_path = company_root_path
        # Image_Level_Management is an element of ilm. each image's path is stored and managed by
        # a unique Image_Level_Management.

        # This Image_Level_Management becomes the image manager for that image
        self.ilm = {}
        self.data = {}
        self.position = {}
        self.category = Category_Manager(f"{company_root_path}\\DoNotDelete\\Category", "category.json")
        self.dm = Data_Management(f"{company_root_path}\\DoNotDelete", "data.json", self.category.get_category_list())
        self.pm = Position_Data_Management(f"{company_root_path}\\DoNotDelete", "position.json",
                                           self.category.get_category_list())

        # Add all the image managers to .ilm list
        self.generate_image_manager()
        self.data = self.dm.get_data()
        self.position = self.pm.get_position_list()

    def generate_image_manager(self) -> None:
        """
        1. loop through the directory f"{self.company_root_path}\\Images". image name is taken as the key.
            image_manager is created as Image_Level_Management, stored as the values
        param:  None
        return: None
        """
        img_dir = f"{self.company_root_path}\\Images"
        for root, dirs, files in os.walk(img_dir):
            for img in files:
                img_path = f"{img_dir}\\{img}"
                self.ilm[img] = Image_Level_Management(img_path)

            break

    def get_company_path(self) -> str:
        """
        param:  None
        return: company root path
        """
        return self.company_root_path

    def get_company_name(self) -> str:
        """
        param:  None
        return: company name
        """
        company_name: str = os.path.basename(self.company_root_path)
        return company_name

    def get_cv_img(self, target_image_name: str) -> ndarray:
        """
        1. if target_image_name is None, then the first image will be returned as cv image using image manager
        2. if target_image_name is given, then the corresponding image manager will be found and convert the image
           cv image and return
        param:  target_image_name
        return: array representation of the target_image_name
        """
        target_image_manager: Image_Level_Management = None
        if target_image_name is None:
            target_image_manager: ndarray = self.ilm[0].get_cv_img()
        else:
            for image_name, image_manager in self.ilm.items():
                if image_name == target_image_name:
                    target_image_manager = image_manager.get_cv_img()
                    break

        return target_image_manager

    def get_image_name_list(self) -> list[str]:
        """
        1. loop through all the image name in the dictionary that store image manager

        param: None
        retrun: a list of string name
        """
        image_name_list = []
        for image_name in self.ilm.keys():
            image_name_list.append(image_name)

        return image_name_list

    def update_position_info(self, command: str, category_key: str = None, pos1: list[float] = None,
                             pos2: list[float] = None):
        """
        1. take newly determined position
        2. delete position when category is deleted

        param: command, category key, position 1 [x, y], position 2 [x, y]
        return:
        """
        if command == "update":
            self.pm.update_category_position(category_key, pos1, pos2)
        elif command == "remove":
            self.pm.remove_category(category_key)

    def update_data_info(self, command: str, image_name: str, category_key: str = None, text: str = None):
        """
        1. take newly extracted text
        2. delete extracted text when category is deleted

        param: command, image name, category key, text
        return:
        """
        if command == "update":
            self.dm.update_extracted_information(image_name, category_key, text)
        elif command == "remove":
            self.dm.remove_image(image_name)

    def update_category(self, category_list: list[str]):
        """
        1. sync category info to all .dm and .pm
        param: category list
        return:
        """
        self.category.update_category(category_list)
        self.dm.update_category(category_list)
        self.pm.update_category(category_list)

    def update_to_file(self):
        """
        1. update all data to local file for .category .pm and .dm

        param:
        return:
        """
        self.pm.update_to_file()
        self.dm.update_to_file()
        self.category.update_to_file()

    def get_extracted_data(self) -> dict[dict]:
        return self.dm.get_data()

    def get_category_list(self) -> list[str]:
        return self.category.get_category_list()

    def get_position_list(self) -> dict:
        return self.pm.get_position_list()


def main():
    test_path: str = "C:\\Users\\zhouw\\OneDrive\\Documents\\personal sci project\\vs\\ProjectIV\\Test_Resource\\company_test\\CompanyI"
    company_manager = Company_Level_Management(test_path)
    image_list: list = company_manager.get_image_name_list()
    print(f"company name {company_manager.get_company_name()}")
    print(f"company path {company_manager.company_root_path}")
    print(f"length of image list {len(image_list)}")
    print(f"image name list: {image_list}")
    image = company_manager.get_cv_img(image_list[0])
    cv2.imshow("image window", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    print("=====================Basic Test=====================")
    print("Company_Level_Management.py test")
    # main()
