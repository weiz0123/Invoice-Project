from Folder_Management import Folder
from Folder_Management import Folder_Management
from Folder_Management import Invoice_Source_Management




folder = None
manage = None
invoice_manage = None

def initilize_work_environment(PATH:str) -> bool:
    try:
        folder = Folder(PATH)
        manage = Folder_Management()
        invoice_manage = Invoice_Source_Management()
        manage.refresh(folder)  #  -> to initilize image file
        invoice_manage.refresh_image_folder(folder)
        manage.refresh(folder)  # -> to add image file into stored data structure
    except Exception:
        return False
    else:
        return True




def closing_work_environment():
    pass



def main():
    # test
    PATH = "C:\\Users\\zhouw\\OneDrive\\Documents\\vs\\Invoice Processing\\test Folder"
    if initilize_work_environment(PATH)[0]:
        print("...initilize_successfully")
    else:
        print("...fail to set up working environment")



if __name__== "__main__":
    main()
