import os
from DoubleLinkedList import DLinkedList as DL
from DoubleLinkedList import DLinkedListNode as DN
import BinaryTree as BT
#TODO: issue: terrible search / sort
#asdf
class Folder:

    def __init__(self, root_path) -> None:
        
        ### components of a folder at a particular level
        self.__path = root_path
        if root_path != 'None':
            self.__folder = DL()
            self.__file = DL()
    
    def get_root(self):
        return self.__path
    
    def get_folders(self) -> DL:
        return self.__folder
    
    def get_files(self) -> DL:
        return self.__file

# In order for folder_structure to be complete, folder_hierachy() is required
class Folder_Structure():
    def __init__(self, root_path) :
        self.__root = Folder(root_path)
        self.__folder = self.__root.get_folders()
        self.__files = self.__root.get_files()

        # this loop is processed at 1 level down of the root_path
        for root, directories, files in os.walk(root_path):  
            #print(root_path)
            ### adding folder
            if len(directories) == 0:
                self.__folder.add(Folder(f"Folder None"))
            else:
                for items in directories:
                    self.__folder.add(Folder(f"{root}\\{items}"))

            ### adding files
            if len(files) == 0:
                self.__files.add(Folder(f"File None"))
            else:
                for items in files:
                    self.__files.add(Folder(f"{root}\\{items}"))

            break
    def get_root_path(self) -> str:
        return self.__root.get_root()
    
    def get_root(self) -> Folder:
        return self.__root
    
    def get_folders(self) -> DL:
        return self.__folder
    
    def get_files(self) -> DL:
        return self.__files

    def get_folder_str(self):
        temp_str = ''
        for i in range(self.__folder.getSize()):
            if self.__folder.getItem(i).get_root() == 'Folder None':###
    
                temp_str += "None\n"
            else:
                temp_str += self.__folder.getItem(i).get_root() + "\n"

        return temp_str
    
    def get_file_str(self):
        temp_str = ''
        for i in range(self.__files.getSize()):
        
            if self.__files.getItem(i).get_root() == 'File None':###
                temp_str += "None\n"
            else:
                temp_str += self.__files.getItem(i).get_root() + "\n"
        return temp_str
    
    def search_helpe(self, index, search_type:str) -> Folder:
        if search_type == "folder":
            return self.__folder.getItem(index)
        elif search_type == "file":
            return self.__files.getItem(index)
    

    def search_folder(self, item_path) -> Folder:
        for i in range(self.__folder.getSize()):
            next_folder_path = self.search_helper_item(i).get_root()
            if next_folder_path == item_path:
                return next_folder_path
            else:
                return "unable to find the desired folder -> possible error: folder doesnt exist/other error"

    def search_file(self, item_path):
        for i in range(self.__files.getSize()):
            next_folder_path = self.search_helper_item(i,"file").get_root()
            if next_folder_path == item_path:
                return next_folder_path
            else:
                return "unable to find the desired file-> possible error: folder doesnt exist/other error"

    #TODO:possible error for inserting item_path
    def add_required_file(self, item_path):
        self.__folder.add(Folder_Structure(f"{self.__root}\\{item_path}"))

    def add_required_folder(self, item_path):
        self.__files.add(Folder_Structure(f"{self.__root}\\{item_path}"))


# Control Folder Structure

def folder_hierarchy(root_folder: Folder_Structure):
    folder_list = root_folder.get_folders()
    file_list = root_folder.get_files()
    #print(folder_list.getItem(0).get_root())
    #print(file_list.getItem(0).get_root())

    if folder_list.getItem(0).get_root() == 'Folder None' and file_list.getItem(0).get_root() == 'Folder None':
        #print("both empty return none")
        return None
    elif folder_list.getItem(0).get_root() == 'Folder None':
        #print("one empty return none") 
        return None

    elif folder_list.getItem(0).get_root() != 'Folder None':
        ### loop through the folder of a root
        #print(folder_list.getSize())
        for i in range(folder_list.getSize()):

            #print(i)
            root_path = folder_list.getItem(i).get_root()  # path
            #print(f"root_path {root_path}")
            new_folder = Folder_Structure(root_path)
            folder_list.replace(i,new_folder)

            folder_hierarchy(new_folder)  #  ->  mistake


PATHII = "C:\\Users\\zhouw\\OneDrive\\Documents\\vs\\Invoice Processing\\python_p2_FME\\test Folder I"
PATH = "C:\\Users\\zhouw\\OneDrive\\Documents\\vs\\Invoice Processing\\test Folder"
ROOT = Folder_Structure(PATH)
folder_hierarchy(ROOT)

print(ROOT.get_folders().getItem(0).get_root_path())
