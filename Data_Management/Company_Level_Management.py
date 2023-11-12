import os
from numpy import ndarray
from Data_Management.Image_Level_Management import Image_Level_Management


class Company_Level_Management:

    def __init__(self, company_root_path):
        # store the company folder's path
        self.company_root_path = company_root_path
        # Image_Level_Management is element of ilm. each image's path is stored with a unique Image_Level_Management.
        # This Image_Level_Management becomes the image manager for that image
        # It is responsible to store and manipulate any information about the image.
        self.ilm = {}
        self.data = {}

    def generate_image(self) -> None:
        """
        1. loop through the directory f"{self.company_root_path}\\Images". image name is taken as the key.
            image_manager is created as Image_Level_Management, stored as the values
        param:  None
        return: None
        """
        img_dir = f"{self.company_root_path}\\Images"
        try:
            for root, dirs, files in os.walk(img_dir):
                for img in files:
                    img_path = f"{img_dir}\\{img}"
                    self.ilm[img] = Image_Level_Management(img_path)

                break
        except Exception:
            print('path does not exist')

        if len(self.ilm) == 0:
            pass

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

    def get_cv_image(self, target_image_name: str) -> ndarray:
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
            image_name_list.append()

        return image_name_list

