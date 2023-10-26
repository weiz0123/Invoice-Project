import sys
sys.path.append("C:\\Users\\zhouw\\OneDrive\\Documents\\personal sci project\\vs\\ProjectIII")
import time
import threading
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class NewFileAndFolderHandler(FileSystemEventHandler):
    def __init__(self, on_create_target, on_delete_target):
        self.added = [] # new added company or pdf 
        self.deleted = [] # deleted company or pdf
        self.on_create_target = on_create_target #* function group 1
        self.on_delete_target = on_delete_target #* function group 2
        

    def on_created(self, event):
        if event.is_directory:
            print(f"New folder created: {event.src_path}")
            self.added.clear()
            self.added.append(event.src_path)
            self.call_add()

        else:
            print(f"New file created: {event.src_path}")
            self.added.clear()
            self.added.append(event.src_path)
            self.call_add()
    
    def on_deleted(self, event):
        #TODO Redesign: try to use os to check whether event.src_path is a directory or not
        if event.is_directory:
            print(f"Folder Deleted: {event.src_path}")
            self.deleted.clear()
            self.deleted.append(event.src_path)
            self.call_delete()
        else:
            print(f"File Deleted: {event.src_path}")
            self.deleted.clear()
            self.deleted.append(event.src_path)
            self.call_delete()
    
    #* when new file is added to a target 

    def call_add(self):
        count = 0
        for function in self.on_create_target:
            if count == 0:
                function(self.added) #* self.added is a list of new added directory
            else:
                function()
            count += 1
        
    def call_delete(self):
        count = 0
        for function in self.on_delete_target:
            if count == 0:
                function(self.deleted) #* self.deleted is a list of new added directory
            else:
                function()
            count += 1

    def new_added(self):
        return self.added

    def new_deleted(self):
        return self.deleted

class Folder_Watch_Dog(NewFileAndFolderHandler):
    def __init__(self, folder_to_watch, on_create_target, on_delete_target):
        #* Folder path to watch
        self.watch = folder_to_watch
        #* Function list to be called when file is created
        self.on_create_target = on_create_target
        #* Function list to be called when file is deleted
        self.on_delete_target = on_delete_target
        super().__init__(on_create_target, on_delete_target)
    
    #* This is like a main function for on_create() and on_deleted method
    def folder_change(self):
        event_handler = NewFileAndFolderHandler(self.on_create_target, self.on_delete_target)
        observer = Observer()
        observer.schedule(event_handler, self.watch, recursive=False)
        observer.start()

        try:
            i = 0
            while True:
                time.sleep(1)
                #print(f'{i}')
                i += 1
        except KeyboardInterrupt:
            observer.stop()
        observer.join() 
    
class Pdf_Watch_Dog(NewFileAndFolderHandler):
    def __init__(self, folder_to_watch, on_create_target, on_delete_target):
        self.watch = folder_to_watch
        self.on_create_target = on_create_target
        self.on_delete_target = on_delete_target
        super().__init__(on_create_target, on_delete_target)
    

    def file_change(self):
        event_handler = NewFileAndFolderHandler(self.on_create_target, self.on_delete_target)
        observer = Observer()
        observer.schedule(event_handler, self.watch, recursive=False)
        observer.start()

        try:
            i = 0
            while True:
                time.sleep(1)
                #print(f'{i}')
                i += 1
        except KeyboardInterrupt:
            observer.stop()
        observer.join() 

#! need to check whether the added is a file or a folder
#! call_add and call_delete are 2 protocals. they include a series of fixed action when a folder is updated in FWD, and Pdf updated in PWD
#! there needs to be an mechanism to check the legitmancy of folder for FWD and file for PWD. (i.e. does the format match the requirement)
#TODO: Redsign: need a call_add and call_delete protocal design
if __name__ == "__main__":
    # the following two are target function that mimics the add action and delete action 
    def add(data):
        print("action1")


    def delete(data):
        print("action2")


    folder_to_watch = 'C:\\Users\\zhouw\\OneDrive\\Documents\\vs\\ProjectIII\\Test_Resource\\company_test'
    pdf_to_watch = 'C:\\Users\\zhouw\\OneDrive\\Documents\\vs\\ProjectIII\\Test_Resource\\company_test\\CompanyI'

    test_f=Folder_Watch_Dog(folder_to_watch, [add], [delete])
    test_i = Pdf_Watch_Dog(pdf_to_watch, [add], [delete])

    thread1 = threading.Thread(target=test_f.folder_change)
    thread2 = threading.Thread(target=test_i.file_change)

    thread1.start()
    thread2.start()






