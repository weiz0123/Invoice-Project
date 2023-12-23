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
        # init .position list
        self.load_file()

    def load_file(self):
        # if the position file exists (this should be handled at installation process), then load in the data to .position
        try:
            with open(f"{self.position_data_file_path}\\{self.position_data_file_name}", 'r') as file:
                self.position = json.load(file)
        except FileNotFoundError:
            print("Position_Data_Management : 'file is invalid'");

    def get_position_list(self) -> dict:
        return self.position

    def update_category_position(self, category_key: str, pos1: list[float], pos2: list[float]) -> bool:
        try:
            self.position[category_key] = [pos1, pos2]
            if category_key not in self.category_list:
                self.category_list.append(category_key)

            return True
        except ValueError:
            return False

    def remove_category(self, category_key: str) -> bool:
        try:
            del self.position[category_key]
            self.category_list.remove(category_key)

        except ValueError:
            print(f"{category_key} doesn't exist")

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

    def get_category_list(self):
        return self.category_list

    def update_category(self, category: list):  # !!!! VERY IMPORTANT
        """
        1. this function keeps update the newest category.
        2. when a category is deleted, corresponding data should also be deleted
        :param category:
        :return:
        """
        self.category_list = category


class Data_Management:
    def __init__(self, data_path: str, file_name: str, category_list: list[str]):
        self.data_path: str = data_path
        self.file_name: str = file_name
        self.data: dict[dict] = {}
        self.category_list: list = category_list

        self.load_file()

    def load_file(self) -> bool:
        try:
            with open(f"{self.data_path}\\{self.file_name}", 'r') as file:
                self.data = json.load(file)
            return True

        except FileNotFoundError:
            print('file is invalid')
            return False

        except EOFError:
            print("file is empty")
            return False

        except json.JSONDecodeError as e:
            print(f"JSON decoding error: {e}")
            return False

    # ! needs to worry about updating 'category' type
    def update_extracted_information(self, image_name, category_key: str, text: str) -> bool:
        # {{}{}{}}
        target_image = image_name
        if category_key not in self.category_list:
            raise ValueError("category doesn't exist")

        for image in self.data.keys():
            if image == image_name:
                target_image = image

        if target_image not in self.data.keys():
            self.data[target_image] = {}

        self.data[target_image][category_key] = text

        return True

    def remove_image(self, image_name: str) -> bool:
        target_image = 0
        for image in self.data:
            if image == image_name:
                target_image = image

        del self.data[target_image]

        return True

    def get_data(self):
        return self.data

    def update_to_file(self) -> bool:
        with open(f"{self.data_path}\\{self.file_name}", 'w') as file:
            json.dump(self.data, file)
            return True
        return False

    def update_category(self, category: list):  # !!!! VERY IMPORTANT
        """
        1. this function keeps update the newest category.
        2. when a category is deleted, corresponding data should also be deleted
        :param category:
        :return:
        """
        self.category_list = category

    def remove_category(self, category_key: str) -> bool:
        if category_key in self.category_list:
            self.category_list.remove(category_key)

        for image_name in self.data.keys():
            for category in self.data[image_name].keys():
                del self.data[image_name][category]

        return True


class Category_Manager:
    def __init__(self, data_path: str, file_name: str):
        self.data_path: str = data_path
        self.file_name: str = file_name
        self.category_list: list = []

        self.load_file()

    def load_file(self) -> bool:
        try:
            with open(f"{self.data_path}\\{self.file_name}", 'r') as file:
                self.category_list = json.load(file)
            return True

        except FileNotFoundError:
            print('file is invalid')
            return False

        except EOFError:
            print("file is empty")
            return False

        except json.JSONDecodeError as e:
            print(f"JSON decoding error: {e}")
            return False

    def update_category(self, category: list):  # !!!! VERY IMPORTANT
        """
        1. this function keeps update the newest category.
        2. when a category is deleted, corresponding data should also be deleted
        :param category:
        :return:
        """
        self.category_list = category

    def update_to_file(self):
        with open(f"{self.data_path}\\{self.file_name}", 'w') as file:
            json.dump(self.category_list, file)
            return True

        return False

    def get_category_list(self):
        return self.category_list


def position_test():
    # Test Material Set up
    category_list: list = ["invoice number", "invoice date"]
    position_data_path: str = f"C:\\Users\\zhouw\\OneDrive\\Documents\\personal sci project\\vs\\ProjectIV\\Test_Resource\\company_test_Secure_Data_Management\\CompanyI\\DoNotDelete"

    # Test Manager Init
    position_data_manager = Position_Data_Management(position_data_path, "position.json", category_list)

    # Get Position list
    position_data = position_data_manager.get_position_list()
    print(f"position information: {position_data}")

    # Update position list with existing category
    position_data_manager.update_category_position("invoice number", [2, 130.97587920695787],
                                                   [1491.2558028559597, 202.7800316928674])
    print(f"position information: {position_data_manager.get_position_list()}")

    # Update the current position list to local file
    position_data_manager.update_to_file()

    # Check current category
    print(f"category list {position_data_manager.get_category_list()}")

    # Update category and position with new category key
    position_data_manager.update_category_position("sale date", [2, 130.97587920695787],
                                                   [1491.2558028559597, 202.7800316928674])
    print(f"position information: {position_data_manager.get_position_list()}")
    print(f"category list {position_data_manager.get_category_list()}")


def data_test():
    # Test Material Set up
    category_list: list = ["invoice number", "invoice date"]
    data_path: str = f"C:\\Users\\zhouw\\OneDrive\\Documents\\personal sci project\\vs\\ProjectIV\\Test_Resource\\company_test_Secure_Data_Management\\CompanyI\\DoNotDelete"

    # Test manager init
    data_manager = Data_Management(data_path, "data.json")
    print(f"loading...: {data_manager.load_file()}")
    # Update category, Update data when category change, Update first time image
    data_manager.update_category(category_list)
    data_manager.update_extracted_information("test image", "invoice date", "invoice test 1")
    print(f"data: {data_manager.get_data()}")
    data_manager.update_extracted_information("test image", "invoice date", "invoice test 2")
    print(f"data: {data_manager.get_data()}")
    data_manager.update_extracted_information("test image", "invoice number", "invoice test 3")
    print(f"data: {data_manager.get_data()}")
    data_manager.update_extracted_information("test image1", "invoice number", "invoice test 2")
    print(f"data: {data_manager.get_data()}")

    # Remove image
    data_manager.remove_image("test image")
    print(f"data: {data_manager.get_data()}")
    print(f"uploading...: {data_manager.update_to_file()}")
    print(f"loading...: {data_manager.load_file()}")


def main():
    print("=====================Basic Test=====================")
    position_test()
    data_test()
    print("=====================Observer Test=====================")
    print("=====================Error Test=====================")


if __name__ == "__main__":
    print("Secure_Data_Management.py test")
    main()
