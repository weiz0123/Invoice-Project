from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
from Data_Management.Company_Level_Management import Company_Level_Management
from Data_Management.User_Level_Management import User_Level_Management


class Update_Observer:
    def __init__(self, id: int, target_path: str, emitter):
        self.id = id
        self.target_path: str = target_path
        self.emitter_to_access_unit = emitter
        update_manager = Directory_Observer(self.signal_receiver_create, self.signal_receiver_delete)
        observer = Observer()
        observer.schedule(update_manager, target_path, recursive=False)
        observer.start()
        while True:
            pass

    def signal_receiver_create(self, target_path_list: list[str]):
        """
        1. this function is called by Directory_Observer when a list of path is added
        2. emitter is a function call to a function in Update_Access
        param target_path_list:
        return:
        """
        self.emitter_to_access_unit(target_path_list, self.id)

    def signal_receiver_delete(self, target_path_list: list[str]):
        """
        1. this function is called by Directory_Observer when a list of path is deleted
        2. emitter is a function call to a function in Update_Access
        param target_path_list:
        return:
        """
        self.emitter_to_access_unit(target_path_list, self.id)


class Directory_Observer(FileSystemEventHandler):
    def __init__(self, on_create_emitter, on_delete_emitter):
        self.on_create_emitter = on_create_emitter
        self.on_delete_emitter = on_delete_emitter
        self.on_create_path: list[str] = []
        self.on_delete_path: list[str] = []

    def update_event(self, event, command: str):
        """
        1. event.src_path is the newly added or deleted path
        param: event, command
        return:
        """
        if command == "create":
            self.on_create_path.append(event.src_path)
            self.on_create_emitter(self.on_create_path)
        else:
            self.on_delete_path.append(event.src_path)
            self.on_delete_emitter(self.on_delete_path)

    def on_created(self, event):
        """
        1. called by observer when a path is created or added to event.src_path
        param event:
        return:
        """
        self.update_event(event, "create")

    def on_deleted(self, event):
        """
        1. called by observer when a path is removed or deleted from event.src_path
        param event:
        return:
        """
        self.update_event(event, "delete")


def test_function(target_list: list, id: int):
    print(id)
    print(target_list)
    target_list.clear()


def main():
    DEFAULT_PATH = "C:\\Users\\zhouw\\OneDrive\\Documents\\personal sci project\\vs\\ProjectIV\\Test_Resource\\company_test"
    update_observer = Update_Observer(DEFAULT_PATH, test_function)


if __name__ == "__main__":
    main()
