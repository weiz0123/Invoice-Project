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

    def remove_from_folder(self, root_path:str):
        pass

    def remove_from_file(self, root_path:str):
        pass
    
        

    def __str__(self):
        tempStr = ''
        for i in range(self.__folder.getSize()):
            tempStr += self.__folder.getItem(i) + "\n"
        return tempStr

class Folder_Management:

    def __init__(self) -> None:
        self.__None = None

    def initailize (self, folder:Folder):
        root_path = folder.get_root()
        self.add_to_folder(root_path, folder)
        # self.add_to_file(root_path, folder) -> this is called in add_to_folder()
    
    def add_to_folder (self, root_path:str, folder:Folder):
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


    def get_file_str(self, folder:Folder):

        return folder.__str__()

    def get_folder_str(self, folder:Folder):

        return folder.__str__()

def main():
    PATH_Final = "C:\\Users\\zhouw\\OneDrive\\Documents\\vs\\Invoice Processing\\python_p2_FME\\test Folder I"
    PATH = "C:\\Users\\zhouw\\OneDrive\\Documents\\vs\\Invoice Processing\\test Folder"

    folder = Folder(PATH_Final)
    Manage = Folder_Management()
    Manage.initailize(folder)
    # Test
    for i in range(6):
        print(folder.get_folder().getItem(5).get_file().getItem(i).get_root())


if __name__== "__main__":
    main()


