import cv2
import os
from cv2 import Mat
from numpy import ndarray


class Image_Level_Management:
    """
    Purpose:
    Communication:
    * this class doesn't require any documentation at this point as methods and purposes are self-explanatory
    -> high readability
    """
    def __init__(self, image_root_path):
        # this is the image representation for the object
        self.img_path = image_root_path

    def get_img_path(self):
        return self.img_path

    def get_img_name(self):
        img_name = os.path.basename(self.img_path)
        return img_name

    def set_image_name(self, new_image_name: str):
        # Extract the directory from the original path
        directory = os.path.dirname(self.img_path)

        # Construct the new path with the new basename
        self.img_path = os.path.join(directory, new_image_name)

    def get_cv_img(self) -> ndarray:
        cv_img = cv2.imread(self.img_path)
        return cv_img
