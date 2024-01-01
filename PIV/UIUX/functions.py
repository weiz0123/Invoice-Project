from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QDir
from PyQt5.QtWidgets import QTreeWidget, QTreeWidgetItem

def show_status(self, company, num_inv):
    """
    show the message in status bar
    """
    message = f"Current Company: {company}, Number of Invoice: {num_inv}"
    message_label = QtWidgets.QLabel(message)
    message_label.setAlignment(Qt.AlignmentFlag.AlignRight)
    self.statusbar.addWidget(message_label, 1)


"""
if we want to split the message to left and right, just create another Qlabel aligned to left
"""

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
            add_files_to_tree(self,entry.filePath(), item)

def populate_tree(self, folder_path):
    root_item = QTreeWidgetItem(self.File_Explore_List_Widget)
    root_item.setText(0, folder_path)

    add_files_to_tree(self,folder_path, root_item)


