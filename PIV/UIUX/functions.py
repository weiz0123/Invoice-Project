from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QDir, QUrl
from PyQt5.QtWidgets import QTreeWidget, QTreeWidgetItem, QCompleter, QDialog
from file_explorer import my_tree
import category_dialog

alist = ['1', '2'] #for testing
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

def triggered_tools(self):
    # Connect the triggered signal to a method (e.g., on_import_new_company)
    self.actionAdd_category.triggered.connect(add_category)

def add_category():
    Dialog = QtWidgets.QDialog()
    ui = category_dialog.Ui_Dialog()
    ui.setupUi(Dialog)
    ui.comboBox.addItems(alist)
    ui.add.clicked.connect(lambda: add_button(ui))
    ui.remove.clicked.connect(lambda: remove_button(ui))
    Dialog.show()
    Dialog.exec_()  #to make this window exist, avoid closing immediatly

def add_button(self):
    entered_text = self.lineEdit.text()
    if entered_text not in alist and entered_text:
        # append user's category list here
        alist.append(entered_text)
        self.comboBox.addItem(entered_text)
        print("Add category successfully")
    else:
        print(f"Fail to add. Please check if {entered_text} is already a category")
    self.lineEdit.clear()

def remove_button(self):
    current_text = self.comboBox.currentText()
    if len(alist) == 0:
        print("Fail to remove, no category exist")
    else:
        index = 0
        for word in alist:
            if word == current_text:
                alist.remove(word)
                self.comboBox.removeItem(index)
            index+=1
        print(f"remove: {current_text}")