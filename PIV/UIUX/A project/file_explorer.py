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
                    file_path = url.toLocalFile()

                    # Use os.path.join to handle paths in a platform-independent way
                    folder_path = os.path.join(path, "company")

                    # Append the file/folder name to the destination folder path
                    destination_path = os.path.join(folder_path, os.path.basename(file_path))
                    import shutil
                    try:
                        if os.path.isdir(file_path):
                            # If it's a folder
                            if os.path.exists(destination_path):
                                # Folder already exists, you might want to update or skip
                                print(f"destination_path: {destination_path}")
                                shutil.rmtree(destination_path)
                            # Folder doesn't exist, copy it
                            shutil.copytree(file_path, destination_path)
                            self.populate_tree(folder_path)
                            print(f"Folder '{os.path.basename(file_path)}' copied successfully")
                        else:
                            # If it's a file, use shutil.copy
                            shutil.copy(file_path, destination_path)
                            self.populate_tree(folder_path)
                            print(f"File '{os.path.basename(file_path)}' copied successfully")
                    except Exception as e:
                        print(f"Failed to copy\nAn error occurred: {e}")

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

    def populate_tree(self, path):
        self.clear()
        root_item = QTreeWidgetItem(self)
        folder_path = path
        root_item.setText(0, folder_path)

        self.add_files_to_tree(folder_path, root_item)
