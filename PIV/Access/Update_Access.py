from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class Update_Access(FileSystemEventHandler):
    """
    Purpose:
    1. assist Data_Access to access updated data

    Communication:
    1. User_Level_Management
    2. Data_Access -> .class_level_management_list
    3: Update_Observer
    """

    def __init__(self):
        pass

    '''===Internal Class Implementation: the following methods cannot be accessed by other classes==='''


def main():
    pass


if __name__ == "__main__":
    main()
