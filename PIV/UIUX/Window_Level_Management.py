from v2 import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QDir, QUrl, QRect
from PyQt5.QtWidgets import QTreeWidget, QTreeWidgetItem, QCompleter, QDialog, QFileDialog, QLabel
from PyQt5.QtGui import QPixmap, QPainter, QColor
from file_explorer import my_tree
from Image_Level_Management import Image_Level_Management
from Painter_Level_Management import Painter

import image_clicked_recorder
import category_dialog
import subprocess
import sys

alist = ['1', '2']  # for testing


class ExtendedUi_MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):  # QtWidgets.QWidget
    def __init__(self, path):
        super().__init__()
        self.image_label = Painter()
        self.isDrawing = False
        self.window_size = [702, 475]
        self.start_point = QtCore.QPoint(0, 0)
        self.end_point = QtCore.QPoint(0, 0)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.initialization(path)

    def initialization(self, path):

        self.initialize_file_explorer(path)
        self.update_company_combo_box(path)
        self.update_search_box()
        self.update_category_combo_box()
        self.triggered_tools(path)
        self.update_status(path)
        self.init_label(path)
        # self.ui.tab = Painter()
        # self.painter = Painter()
        # self.ui.Matplot_VLayout.addWidget(self.painter)

    def resizeEvent(self, event):
        if self.count_resize > 2:
            # This method will be called whenever the main window is resized
            old_window_size = [self.window_size[0], self.window_size[1]]
            self.window_size[0] = event.size().height()
            self.window_size[1] = event.size().width()

            max_label_width = self.window_size[1] // 2
            max_label_height = max_label_width * 2200 // 1700
            if max_label_width > 950:
                max_label_width = 950
                max_label_height = max_label_width * 2200 // 1700
            self.image_label.setMaximumSize(max_label_width, max_label_height)

            self.image_label.resize(QtCore.QSize(max_label_width, max_label_height))
            #self.image_label_set_x_y

            self.count_resize += 1
            #print(
            #    f"Window resized to: {self.window_size}, max width: {max_label_width}, max height: {max_label_height}")
        else:
            self.count_resize += 1

    def init_label(self, path):
        folder_path = path + "\company\\"
        company = self.ui.Company_ComboBox.currentText()
        company_path = folder_path + company + "\Images"
        entries = self.get_entries(company_path)
        first_entry = entries[0]
        for entry in entries:
            if entry.fileName() not in ('.', '..'):
                first_entry = entry
                break
        image_path = company_path + "\\" + first_entry.fileName()
        image_object = Image_Level_Management(image_path)
        image = image_object.get_cv_img()
        self.count_resize = 1
        if image is not None:
            self.ui.Matplot_VLayout.setContentsMargins(self.window_size[0] // 10, 0, self.window_size[0] // 10, 0)
            max_label_width = self.window_size[1]
            max_label_height = max_label_width * 2200 // 1700
            self.image_label.setMaximumSize(max_label_width, max_label_height)
            pixmap = QtGui.QPixmap(image_path)
            self.image_label.setPixmap(pixmap)
            self.image_label.setScaledContents(True)
            self.ui.Matplot_VLayout.addWidget(self.image_label)

    def initialize_file_explorer(self, path):
        self.ui.File_Explore_List_Widget = my_tree(self.ui.tab)
        self.ui.File_Explore_List_Widget.setAcceptDrops(True)
        self.ui.File_Explore_List_Widget.setDragEnabled(True)
        self.ui.File_Explore_List_Widget.setObjectName("File_Explore_List_Widget")
        self.ui.File_Explore_List_Widget.headerItem().setText(0, "Invoice-Project")
        self.ui.File_Explorer_VLayout.addWidget(self.ui.File_Explore_List_Widget)
        company_path = path + "/company"
        self.ui.File_Explore_List_Widget.populate_tree(company_path)

    def get_entries(self, path):
        dir = QDir(path)

        # Get a list of all entries (files and sub-folders) in the directory
        entries = dir.entryInfoList()
        return entries

    def update_company_combo_box(self, path):
        folder_path = path + "\company"
        entries = self.get_entries(folder_path)
        for entry in entries:
            if entry.fileName() not in ('.', '..') and entry.isDir():
                self.ui.Company_ComboBox.addItem(entry.fileName())

    def clear_update_company_combo_box(self, path):
        for i in range(self.ui.Company_ComboBox.count()):
            self.ui.Company_ComboBox.removeItem(0)
        self.update_company_combo_box(path)

    def update_search_box(self):
        self.target_list = [self.ui.Company_ComboBox.itemText(i) for i in range(self.ui.Company_ComboBox.count())]
        # remember to replace target_list to USER.display_compnay_name()
        completer = QCompleter(self.target_list, self.ui.search_company_name_lineBox)
        completer.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)  # Set case sensitivity
        self.ui.search_company_name_lineBox.setCompleter(completer)

    def update_status(self, path):
        folder_path = path + "\company"

        entries = self.get_entries(folder_path)
        num_company = 0
        for entry in entries:
            if entry.fileName() not in ('.', '..') and entry.isDir():
                num_company += 1
        try:
            company = self.ui.Company_ComboBox.currentText()
            company_path = folder_path + "\\" + company + "\Images"
            company_entries = self.get_entries(company_path)
            num_inv = 0
            for entry in company_entries:
                if entry.fileName() not in ('.', '..') and entry.isFile():
                    num_inv += 1
            message = f"Total Company: {num_company},   Current Company: {company},     Number of Invoice: {num_inv}"
        except:
            message = f"Total Company: {num_company},   Current Company: None,    Number of Invoice: None"

        self.ui.message_label = QtWidgets.QLabel(message)
        self.ui.message_label.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.ui.statusbar.addWidget(self.ui.message_label, 1)

    def clear_update_status_bar(self, path):
        self.ui.statusbar.removeWidget(self.ui.message_label)
        self.update_status(path)

    def update_category_combo_box(self, action=None,
                                  item=None):  # item is a string if action is add, item is an index if actin is remove
        if action == "add":
            self.ui.Category_ComboBox.addItem(item)
        elif action == "remove":
            print(f"update remove: {item}")
            self.ui.Category_ComboBox.removeItem(item)
        else:
            self.ui.Category_ComboBox.addItems(alist)  # replace with user's category

    def triggered_tools(self, path):
        # Connect the triggered signal to a method (e.g., on_import_new_company)
        self.ui.actionAdd_category.triggered.connect(self.add_category)
        self.ui.actionOpenCompanyFolder.triggered.connect(lambda: self.open_company_folder(path))
        self.ui.actionrefresh.triggered.connect(lambda: self.refresh(path))
        self.ui.actionselection_box.triggered.connect(self.draw_rectangle)

    def add_category(self):
        Dialog = QtWidgets.QDialog()
        self.dialog = category_dialog.Ui_Dialog()
        self.dialog.setupUi(Dialog)
        self.dialog.comboBox.addItems(alist)
        self.dialog.add.clicked.connect(self.add_button)
        self.dialog.remove.clicked.connect(self.remove_button)
        Dialog.show()
        Dialog.exec_()  # to make this window exist, avoid closing immediatly

    def add_button(self):
        entered_text = self.dialog.lineEdit.text()
        if entered_text not in alist and entered_text:
            # append user's category list here
            alist.append(entered_text)
            self.dialog.comboBox.addItem(entered_text)
            self.update_category_combo_box(action="add", item=entered_text)
            print("Add category successfully")
        else:
            print(f"Fail to add. Please check if {entered_text} is already a category")
        self.dialog.lineEdit.clear()

    def remove_button(self):
        current_text = self.dialog.comboBox.currentText()
        if len(alist) == 0:
            print("Fail to remove, no category exist")
        else:
            index = 0
            for word in alist:
                if word == current_text:
                    alist.remove(word)
                    self.dialog.comboBox.removeItem(index)
                else:
                    index += 1
            self.update_category_combo_box(action="remove", item=index)
            print(f"remove: {current_text} from index {index}")

    def open_company_folder(self, path):
        folder_path = path + "\company"

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
        self.ui.File_Explore_List_Widget.populate_tree(path)
        self.clear_update_status_bar(path)
        self.clear_update_company_combo_box(path)
        self.update_search_box()
        # self.clear_image()
        # self.display_image(path)

    def draw_rectangle(self):
        self.isDrawing = True
        self.image_label.setDrawing(self.isDrawing)

    # def mousePressEvent(self, event):
    #     x = event.pos().x()
    #     y = event.pos().y()
    #     print(f"Clicked at: ({x}, {y})")
    #     self.start_point = event.pos()
    #
    #
    # def mouseMoveEvent(self, event):
    #     self.end_point = event.pos()
    #     self.update()
    #
    # def mouseReleaseEvent(self, event):
    #     x = event.pos().x()
    #     y = event.pos().y()
    #     print(f"release at: ({x}, {y})")
    #     self.end_point = event.pos()
    #
    # def paintEvent(self, event):
    #     painter = QPainter(self)
    #     painter.setPen(QColor(0, 0, 255))  # Blue color for the rectangle outline
    #
    #     if self.start_point is not None and self.end_point is not None:
    #         # Calculate the rectangle coordinates using start and end points
    #         rect = QRect(self.start_point, self.end_point)
    #         painter.drawRect(rect)
    #
    #
