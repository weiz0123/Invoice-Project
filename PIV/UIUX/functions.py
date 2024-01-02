from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QDir, QUrl
from PyQt5.QtWidgets import QTreeWidget, QTreeWidgetItem, QCompleter, QDialog
from file_explorer import my_tree
import category_dialog
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
            add_files_to_tree(self, entry.filePath(), item)


def populate_tree(self, folder_path):
    root_item = QTreeWidgetItem(self.File_Explore_List_Widget)
    root_item.setText(0, folder_path)

    add_files_to_tree(self, folder_path, root_item)

def initialize_file_explorer(self):
    self.File_Explore_List_Widget = my_tree(self.tab)
    self.File_Explore_List_Widget.setAcceptDrops(True)
    self.File_Explore_List_Widget.setDragEnabled(True)
    self.File_Explore_List_Widget.setObjectName("File_Explore_List_Widget")
    self.File_Explore_List_Widget.headerItem().setText(0, "Invoice-Project")
    self.File_Explorer_VLayout.addWidget(self.File_Explore_List_Widget)

def initialize_search_box(self):
    target_list = ['apple', 'abandon', 'abnormal', 'orange']
    #remember to replace target_list to USER.display_compnay_name()
    completer = QCompleter(target_list, self.search_company_name_lineBox)
    completer.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)  # Set case sensitivity
    self.search_company_name_lineBox.setCompleter(completer)

    # self.result_label = QLabel("Suggested items will appear as you type", self)
    # layout.addWidget(self.result_label)

def triggered_tools(self):
    # Connect the triggered signal to a method (e.g., on_import_new_company)
    self.actionAdd_category.triggered.connect(add_category)

def add_category():
    # ui = category_dialog.Ui_Dialog()
    #

    Dialog = QtWidgets.QDialog()

    ui = category_dialog.Ui_Dialog()

    ui.setupUi(Dialog)

    Dialog.show()
    Dialog.exec_()