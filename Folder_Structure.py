from DoubleLinkedList import DLinkedList 
import os

class Folder:
    def __init__(self, root_path:str) -> None:
        self.__root = root_path 

        self.__folder = DLinkedList() # container type: folder
        self.__file = DLinkedList() # container type: folder

    def get_root(self) -> str:
        return self.__root
    
    def get_file(self) -> DLinkedList:
        return self.__folder
    
    def get_folder(self) -> DLinkedList:
        return self.__file

class Folder_Management:

    def __init__(self) -> None:
        self.__None = None
        self.__level = 0

    def refresh (self, folder:Folder):
        root_path = folder.get_root()
        self.add_to_folder(root_path, folder)
        # self.add_to_file(root_path, folder) -> this is called in add_to_folder()
    
    def get_file_str(self, folder:Folder, pos:int) -> str:
        return folder.get_file().getItem(pos).get_root()

    def get_folder_str(self, folder:Folder, pos:int) -> str:
        return folder.get_folder().getItem(pos).get_root()

    def add_to_folder (self, root_path:str, folder:Folder):
        self.__level += 1
        self.add_to_file(root_path, folder)
        if self.sub_folder_exist(root_path):
            for root, directories, files in os.walk(root_path):
                for items in directories:
                    sub_path = f"{root_path}\\{items}"
                    new_folder = Folder(sub_path)
                    folder.get_folder().add(new_folder)
                    self.add_to_folder(sub_path, new_folder)
                    
                break

        else:
            new_folder = Folder("no any other folder")
            folder.get_folder().add(new_folder)
                    
    def add_to_file(self, root_path:str, folder:Folder):
        #print(self.sub_file_exist(root_path))
        if self.sub_file_exist(root_path):
            for root, directories, files in os.walk(root_path):
                for items in files:
                    sub_path = f"{root_path}\\{items}"
                    new_folder = Folder(sub_path)
                    folder.get_file().add(new_folder)
                break        
        else:
            new_folder = Folder("no any other files")
            folder.get_file().add(new_folder)
            
    def sub_folder_exist(self, root_path:str) -> bool:
            '''
            check if there is any extra folder under the current directory
            '''
            for root, directories, files in os.walk(root_path): 

                # adding folders
                if len(directories) == 0:

                    return False
                
                else:
                    return True
                
                break

    def sub_file_exist(self, root_path:str) -> bool:
        '''
        check if there is extra any file under the current directory
        '''
        for root, directories, files in os.walk(root_path): 

            # adding folders
            if len(files) == 0:

                return False
            
            else:
                return True
            
            break

    def get_file_list_str(self, folder:Folder):
        tempStr = '<{ ' 
        for i in range(folder.get_file().getSize()):
            tempStr += self.get_file_str(folder, i) + ', '

        tempStr += ' }>'
        return tempStr
        
    def get_folder_list_str(self, folder:Folder):
        tempStr = '<{ ' 
        for i in range(folder.get_folder().getSize()):
            tempStr += self.get_folder_str(folder, i) + ', '

        tempStr += ' }>'
        return tempStr


    #TODO:
    def find_file(self, searching_path:str) -> DLinkedList:
        pass
        

    def find_folder(self, initial_folder:Folder, target_path:str) -> DLinkedList:

        if initial_folder.get_folder().search(target_path):
            return True

        for i in range(initial_folder.get_folder().getSize()):
            self.find_folder(initial_folder.get_folder().getItem(i), target_path)
        

    def insert_to_folder(self, sub_root_path:str):
        sub_root_folder = Folder(sub_root_path)
        self.refresh(sub_root_folder)
    
    def insert_to_file(self):
        pass
    
    def get_level(self) -> int:
        return self.__level


def main():
    PATH_Final = "C:\\Users\\zhouw\\OneDrive\\Documents\\vs\\Invoice Processing\\python_p2_FME\\test Folder I"
    PATH = "C:\\Users\\zhouw\\OneDrive\\Documents\\vs\\Invoice Processing\\test Folder"
    folder = Folder(PATH_Final)
    Manage = Folder_Management()
    Manage.refresh(folder)

    #Test
    #print(Manage.get_folder_list_str(folder))
    #print(Manage.get_level()) # -> incorrect

    # Insert
    # print(Manage.find_folder(folder,'C:\\Users\\zhouw\\OneDrive\\Documents\\vs\\Invoice Processing\\test Folder I\\baffin' ))



if __name__== "__main__":
    main()


