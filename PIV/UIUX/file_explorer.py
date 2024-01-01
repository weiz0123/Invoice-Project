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
                        print("File copied successfully")
                    except Exception as e:
                        print(f"Fail to copy\nAn error occurred: {e}")

        else:
            event.ignore()

