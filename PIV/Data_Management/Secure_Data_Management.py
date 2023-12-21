import json


class Secure_Data_Management:
    """
    Purpose:
    Communication:
    """

    def __init__(self):
        pass


class Position_Data_Management:
    def __init__(self, data_path: str, file_name: str, category_list: list[str]):
        # position_data_file_path is the directory where files that record the position of each category are stored
        self.position_data_file_path: str = data_path

        # records the file name
        self.position_data_file_name: str = file_name

        # a list of category name that can be extracted from the cv img
        self.category_list: list[str] = category_list

        # store the position of each category
        self.position = {}

    def load_file(self):
        # if the position file exists (this should be handled at installation process), then load in the data to .position
        try:
            with open(f"{self.position_data_file_path}\\{self.position_data_file_name}", 'r') as file:
                self.position = json.load(file)
        except FileNotFoundError:
            print("Position_Data_Management : 'file is invalid'");

    def update_category_position(self, category_key: str, pos1: list[float], pos2: list[float]) -> bool:
        try:
            self.position[category_key] = [pos1, pos2]
            return True
        except ValueError:
            return False

    def update_category_list(self, new_category_list: list[str]) -> bool:
        try:
            self.category_list = new_category_list
            return True
        except ValueError:
            return False

    def update_to_file(self):
        """
        1. this function will take data stored in .position
        param:
        return:
        """
        # TODO: .position and .category_list  needs to be synced to which ever one has more category element
        try:
            with open(f"{self.position_data_file_path}\\{self.position_data_file_name}", 'w') as file:
                json.dump(self.position, file)

        except FileNotFoundError:
            print('file may not exist.')

    # TODO: update_to_file(self) function is also required for category


# redo required
class Data:
    def __init__(self, data_path, file_name):
        self.data_path = data_path
        self.file_name = file_name
        self.data = []
        self.category_list = []

    def load_file(self):
        try:
            with open(f"{self.data_path}\\{self.file_name}", 'r') as file:
                self.data = json.load(file)

        except FileNotFoundError:
            print('file is invalid')

    # ! needs to worry about updating 'category' type
    def update_extracted_information(self, image_name, category_key: str, text: str):
        # [{}{}{}]
        target_image = None
        for image in self.data:
            if image['Image_Name'] == image_name:
                target_image = image

        target_image[category_key] = text

    def remove_image(self, image_name: str):
        target_index = 0
        count = 0
        for image in self.data:
            if image['Image_Name'] == image_name:
                target_index = count

            count += 1
        print(target_index)
        self.data.pop(target_index)

    def add_image(self, category_list: list, text: list[str]):
        image_format = {}
        index = 0
        for category in category_list:
            image_format[category] = text[index]  # ! text should have the same length as the cateogyr list.
            index += 1
        self.data.append(image_format)

    def get_data(self):
        return self.data

    def update_to_file(self):
        with open(f"{self.data_path}\\{self.file_name}", 'w') as file:
            json.dump(self.data, file)

    def over_write_file(self, data: list[dict]):
        with open(f"{self.data_path}\\{self.file_name}", 'w') as file:
            json.dump(data, file, indent=4)

    def set_category(self, category: list):
        self.category_list = category


"""
class SDM:
    #TODO: Redesign: make all secure data structure as json. 
    def __init__(self, data_path, file_name):
        self.data_path= data_path
        self.file_name = file_name
        self.file_exist = False

    def create_file(self):
        if not os.path.exists(f"{self.data_path}\\{self.file_name}"):
            with open(f"{self.data_path}\\{self.file_name}",'w') as file:
                self.file_exist = True
                pass
        
    def delete_file(self):
        os.remove(f"{self.data_path}\\{self.file_name}")
        self.file_exist = False

    def re_create_file(self):
        self.delete_file()
        self.create_file()
        self.file_exist = True

    def get_data_path(self):
        return self.data_path
    
    def get_file_name(self):
        return self.file_name 

"""
