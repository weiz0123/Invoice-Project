from PyQt5.QtWidgets import QApplication, QMainWindow, QTreeWidget, QTreeWidgetItem
from PyQt5.QtCore import QDir, Qt, QUrl
import os

path = os.getcwd()
class my_tree(QTreeWidget):
    def __int__(self, parent=None):
        super().__int__(parent)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls():
            event.setDropAction(Qt.CopyAction)
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            event.setDropAction(Qt.CopyAction)
            event.accept()
            for url in event.mimeData().urls():
                if url.isLocalFile():
                    print(str(url))

                    file_path = url.path()
                    file_path = file_path[1:]
                    file_path = r'' + file_path
                    folder_path = r''+path.replace("\\","/")      #replace path C:\... to C:/ so that we can use copy to copy file to folders
                    print(file_path, folder_path)
                    import shutil
                    try:
                        shutil.copy(file_path, folder_path)
                        self.populate_tree(folder_path)
                        print("File copied successfully")
                    except Exception as e:
                        print(f"Fail to copy\nAn error occurred: {e}")

        else:
            event.ignore()

    # def update_tree(self):


    def add_files_to_tree(self, folder_path, parent_item):
        dir = QDir(folder_path)

        # Get a list of all entries (files and sub-folders) in the directory
        entries = dir.entryInfoList()

        for entry in entries:
            # Skip "." and ".." (current and parent directory)
            if entry.fileName() in ('.', '..'):
                continue

            item = QTreeWidgetItem(parent_item)
            item.setText(0, entry.fileName())

            # If the entry is a directory, recursively add its files and sub-folders
            if entry.isDir():
                self.add_files_to_tree(entry.filePath(), item)

    def populate_tree(self, folder_path):
        self.clear()
        root_item = QTreeWidgetItem(self)
        root_item.setText(0, folder_path)

        self.add_files_to_tree(folder_path, root_item)
