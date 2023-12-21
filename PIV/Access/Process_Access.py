import os

from numpy import ndarray
import pytesseract
from pdf2image import convert_from_path
from pytesseract import Output


class Process_Access:
    """
    Purpose:
    1. take data, manipulate, change, extract information

    Communication:
    1. User_Level_Management
    """

    def __init__(self, data_process_root_path: str):
        self.root_path = data_process_root_path

    @staticmethod
    def crop_for_roi(cv_img: ndarray, pos1: list[int, int], pos2: list[int, int]) -> ndarray:
        """
        1. pos1 -> top-left corner coordinate, and pos2 -> bot-right corner coordinate are taken to crop for roi region

        param: cv_img, pos1, pos2:
        return: roi i.e. cv_img
        """
        roi: ndarray = cv_img[int(pos1[1]):int(pos2[1]), int(pos1[0]):int(pos2[0])]
        return roi

    @staticmethod
    def text_extraction(roi: ndarray) -> str:
        """
        1. roi is a cropped section of a image. It should only contain one piece of information for
        extraction
        param roi:
        return text extracted from the roi img
        """
        d = pytesseract.image_to_data(roi, output_type=Output.DICT)
        extracted_text = list(filter(lambda a: a != "", d['text']))
        target_text = ''
        for i in d['text']:
            target_text += i

        return target_text

    def convert_existing_pdf(self, company_name: str, pdf_paths: list[str]):
        """
        * further detailed documentation for this function will be included
        """
        for pdf_path in pdf_paths:
            save_path = f"{self.root_path}\\{company_name}\\Images"
            try:
                images = convert_from_path(pdf_path)
                for i, image in enumerate(images):
                    temp_str = pdf_path[0:len(pdf_path) - 4]
                    last_index = temp_str.rfind("\\") + 1
                    image.save(f'{save_path}\\{pdf_path[last_index:len(pdf_path) - 4]}.jpg', "JPEG")

            except Exception as e:
                if os.path.exists(pdf_path) is False:
                    raise Exception(f"pdf path: <<{pdf_path}>> cannot be found or doesnt exsit")
                elif os.path.exists(save_path) is False:
                    raise Exception(f"save coverted image path: <<{save_path}>> cannot be found or doesnt exsit")
                else:
                    print(e.args)
                    raise Exception(f"errors when converting pdf to jpg from <<{pdf_path}>> to <<{save_path}>>")
