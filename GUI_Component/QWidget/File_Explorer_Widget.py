import sys
sys.path.append("C:\\Users\\zhouw\\OneDrive\\Documents\\personal sci project\\vs\\ProjectIII")
from PyQt6.QtWidgets import QTreeWidget, QTreeWidgetItem
from PyQt6.QtGui import QIcon, QDragEnterEvent, QDropEvent
from User_Action.Data_Access import Data_Access
import os

class File_Explorer_Widget(QTreeWidget):
    def __init__(self, tree_widget : QTreeWidget):
        super().__init__()
        self.tree_widget = tree_widget
    
        self.populate_tree_view("C:\\Users\\zhouw\\OneDrive\\Documents\\personal sci project\\vs\\ProjectIII\\Test_Resource\\company_test")
        self.tree_widget.setHeaderLabels(["Name"])  # Set column headers

    def populate_tree_view(self, path):
        root_item = QTreeWidgetItem(self.tree_widget, [path])  # Create the root item with the given path
        self.populate_tree_recursive(root_item, path)  # Recursively populate the tree view

    def populate_tree_recursive(self, parent_item, path):
        for file_name in os.listdir(path):
            file_path = os.path.join(path, file_name)
            item = QTreeWidgetItem(parent_item, [file_name, "", ""])  # Create an item with the file name
            if os.path.isdir(file_path):
                icon = QIcon.fromTheme("folder")
                self.populate_tree_recursive(item, file_path)  # Recursively populate subdirectories

    def handle_double_click(self, item, column):
        file_path = self.get_item_path(item)
        print('asdf')
        if os.path.isdir(file_path):
            self.tree_widget.clear()  # Clear the tree view
            self.populate_tree_view(file_path)  # Populate the tree view with the selected directory

    def get_item_path(self, item):
        path = item.text(0)
        parent = item.parent()
        while parent is not None:
            path = os.path.join(parent.text(0), path)
            parent = parent.parent()
        return path

    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event: QDropEvent):
        if event.mimeData().hasUrls():
            urls = event.mimeData().urls()
            for url in urls:
                path = url.toLocalFile()
                # Handle the dropped file path
                print("Dropped file:", path)
            event.acceptProposedAction()
    