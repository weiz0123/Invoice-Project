from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QDir, QUrl
from PyQt5.QtWidgets import QTreeWidget, QTreeWidgetItem, QCompleter, QDialog, QFileDialog
from file_explorer import my_tree
import category_dialog
import subprocess
import sys

alist = ['1', '2'] #for testing

def get_entries(path):
    dir = QDir(path)

    # Get a list of all entries (files and sub-folders) in the directory
    entries = dir.entryInfoList()
    return entries

def update_status(self, path):
    folder_path = path + "\company"

    entries = get_entries(folder_path)
    num_company = 0
    for entry in entries:
        if entry.fileName() in ('.', '..') and entry.isDir():
            num_company+=1
    try:
        company = self.Company_ComboBox.currentText()
        company_path = folder_path+"\\"+company
        company_entries = get_entries(company_path)
        num_inv = 0
        for entry in company_entries:
            if entry.fileName() in ('.', '..') and entry.isFile():
                num_inv += 1
        message = f"Total Company: {num_company},   Current Company: {company},     Number of Invoice: {num_inv}"
    except:
        message = f"Total Company: {num_company},   Current Company: None,    Number of Invoice: None"

    self.message_label = QtWidgets.QLabel(message)
    self.message_label.setAlignment(Qt.AlignmentFlag.AlignRight)
    self.statusbar.addWidget(self.message_label, 1)

def clear_update_status_bar(self, path):
    self.statusbar.removeWidget(self.message_label)
    update_status(self, path)

def initialize_file_explorer(self, path):
    self.File_Explore_List_Widget = my_tree(self.tab)
    self.File_Explore_List_Widget.setAcceptDrops(True)
    self.File_Explore_List_Widget.setDragEnabled(True)
    self.File_Explore_List_Widget.setObjectName("File_Explore_List_Widget")
    self.File_Explore_List_Widget.headerItem().setText(0, "Invoice-Project")
    self.File_Explorer_VLayout.addWidget(self.File_Explore_List_Widget)
    folder_path = path+"\company"
    self.File_Explore_List_Widget.populate_tree(folder_path)

def initialize_search_box(self):
    target_list = ['apple', 'abandon', 'abnormal', 'orange']
    #remember to replace target_list to USER.display_compnay_name()
    completer = QCompleter(target_list, self.search_company_name_lineBox)
    completer.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)  # Set case sensitivity
    self.search_company_name_lineBox.setCompleter(completer)

def triggered_tools(self, path):
    # Connect the triggered signal to a method (e.g., on_import_new_company)
    self.actionAdd_category.triggered.connect(add_category)
    self.actionOpenCompanyFolder.triggered.connect(lambda: open_company_folder(path))
    self.actionrefresh.triggered.connect(lambda: refresh(self, path))

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

def open_company_folder(path):
    folder_path = path+"\company"

    print(folder_path)
    try:
        """only supported for window now"""
        # Use the appropriate command based on the operating system
        if sys.platform.startswith('win'):
            subprocess.Popen(['explorer', folder_path], shell=True)
        elif sys.platform.startswith('darwin'):
            subprocess.Popen(['open', folder_path])
        elif sys.platform.startswith('linux'):
            subprocess.Popen(['xdg-open', folder_path])
        else:
            print("Unsupported platform")
    except Exception as e:
        print(f"Error opening folder: {e}")

def refresh(self, path):
    self.File_Explore_List_Widget.populate_tree(path)
    clear_update_status_bar(self, path)