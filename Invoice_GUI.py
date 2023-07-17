
""" System """
import sys
import numpy as np
import os
import threading

""" PyQt5/6 """
from PyQt6 import uic

from PyQt6.QtGui import QPixmap, QPalette, QColor, QDragEnterEvent, QDropEvent, QIcon
from PyQt6.QtWidgets import (QStyle, QGridLayout, QToolButton,QTreeView,QTreeWidget,QTreeWidgetItem, QLineEdit, QCompleter, QApplication, QMainWindow, QVBoxLayout, QWidget, QGraphicsView,QWidget, QLabel, QFrame, QComboBox, QPushButton, QHBoxLayout, QTabWidget, QScrollArea, QProgressBar, QDialog)
from PyQt6.QtCore import Qt, QThread, QTimer, pyqtSignal,QModelIndex, QMimeData
from PyQt5.QtWidgets import QFileSystemModel

""" MatPlot Library"""
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas, NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
from matplotlib.widgets import RectangleSelector
import matplotlib.patches as patches

""" Instance """
from Folder_Management import Folder, Invoice_Source_Management, Folder_Management
from Data_Transfer import ComboBox_Data_Transfer as CO
from Data_Transfer import File_Explorer_Data_Transfer as FO
from Data_Transfer import PushButton_Data_Transfer as PO

""" GUI DESIGN OBPTIMIZE"""
from comboBox.Company_List import Company_List 
ui_file_path = "C:\\Users\\zhouw\\OneDrive\\Documents\\vs\\Invoice Processing\\python_p4_Version\\Invoice_Management_System.ui"
PATH = "C:\\Users\\zhouw\\OneDrive\\Documents\\vs\\Invoice Processing\\python_p4_Version\\test Folder"

#
""" Folder Management Section"""  
FOLDER = Folder(PATH)
MANAGE = Folder_Management()
INVOICE_MANAGE = Invoice_Source_Management()
comboBox_IO = CO(FOLDER, MANAGE, INVOICE_MANAGE) # Data Transfer between comboBox and Processor
file_explorer_IO = FO(FOLDER,MANAGE,INVOICE_MANAGE) # Data Transfer between GUI and File Explorer
pushButton_IO = PO(FOLDER, MANAGE, INVOICE_MANAGE) # Data Transfer between GUI and pushButtono
def company_list_name() -> list:
    '''
    This method returns a list of each company's name. The list can be represented in a comboBox
    
    '''
    aList = []
    for i in range(FOLDER.get_folder().getSize()//2):
        each_company_path:str = FOLDER.get_folder().getItem(i).get_root()
        name = each_company_path[each_company_path.rfind('\\')+1:]
        aList.append(name)
    print(aList)
    comboBox_IO.controll_deliever_list("Company_ComboBox",aList)
    print("deliever completed //////////////")


def Initialize_Folder_System(root_folder_path:str):
    '''
    this method is like the main class
    '''
    MANAGE.refresh(FOLDER)
    INVOICE_MANAGE.refresh_image_folder(FOLDER)
    MANAGE.refresh(FOLDER) # refresh when new item is added to the file
    print("Initialize Info Complete...")
    


# The section above only deal with first time Data Step up
#===========================================================================================================================================================================================================================================================================================================================================================================================#
#===========================================================================================================================================================================================================================================================================================================================================================================================#
#===========================================================================================================================================================================================================================================================================================================================================================================================#

class Toolbar(NavigationToolbar):
    def __init__(self, *args, **kwargs):
        super(Toolbar, self).__init__(*args, **kwargs)

class Canvas(FigureCanvas):
    def __init__(self, parent):
        self.fig, self.ax = plt.subplots(figsize=(5, 4), dpi=200)
        self.fig.subplots_adjust(left=0.043, right=0.927, bottom=0.094, top=0.950)
        super().__init__(self.fig)
    
    def test_graph(self):
        """ 
        Matplotlib Script
        """
        t = np.arange(0.0, 2.0, 0.01)
        s = 1 + np.sin(2 * np.pi * t)
        
        self.ax.plot(t, s)

        self.ax.set(xlabel='time (s)', ylabel='voltage (mV)',
               title='About as simple as it gets, folks')
        self.ax.grid()

    def plot_image (self, img_path):
        img = plt.imread(img_path)
        img = self.ax.imshow(img)
        print(f"image ploted for {img_path}")

class WorkerThread(QThread):
    progressChanged = pyqtSignal(int)  # Define the progress signal
    finished = pyqtSignal()  # Define the finished signal

    terminateFlag = False  # Shared flag variable

    def run(self):
        thread2 = threading.Thread(target=self.load2)
        thread1 = threading.Thread(target=self.load1)
        thread2.start()
        thread1.start()
        thread2.join()
        self.terminateFlag = True  # Set the terminate flag when thread2 finishes
        thread1.join()
        self.finished.emit()  # Emit the finished signal when loading is complete

    def load1(self):
        for i in range(101):
            if self.terminateFlag:
                break  # Terminate the loop if the flag is set
            self.progressChanged.emit(i)
            self.msleep(100)
        self.finished.emit()

    def load2(self):
        Initialize_Folder_System(PATH)
    
class ProgressDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Loading All Files...")
        print("Loading Files...")
        layout = QVBoxLayout()
        self.progress_bar = QProgressBar()
        layout.addWidget(self.progress_bar)
        self.setLayout(layout)
        self.worker_thread = WorkerThread()
        self.worker_thread.progressChanged.connect(self.update_progress)
        self.worker_thread.finished.connect(self.hide)  # Hide the dialog when loading is finished
        self.worker_thread.start()

    def update_progress(self, value):
        self.progress_bar.setValue(value)

class MainWindow(QWidget):
    def __init__(self):
        """ Constructor for Empty Window Class """
        super().__init__()  #  inherit all the method from QWidget
        print("Main Window is setting up...")
        
        self.initializeUI()

    def initializeUI(self):
        """ Set up the application for all ui components """
        uic.loadUi(ui_file_path, self)
        self.setWindowTitle("Invoice Management")
        

        """ Instance of Componenet UI """
        # Layout
        self.__Tab_HLayout : QHBoxLayout = self.findChild(QHBoxLayout, "Tab_HLayout")
        self.__Matplot_VLayout: QVBoxLayout = self.findChild(QVBoxLayout, "Matplot_VLayout")
        self.__Extraction_GLayout: QGridLayout = self.findChild(QGridLayout, "Extraction_GridLayout")

        # widget
        self.__Tab_Widget : QTabWidget = self.findChild(QTabWidget, "Tab_Widget")
        self.__File_Explorer_Widget : QTreeWidget = self.findChild(QTreeWidget, "File_Explore_List_Widget")

        #container
        self.__Company_List : QComboBox = self.findChild(QComboBox, "Company_ComboBox")
        comboBox_IO.set_comboBox_list([self.__Company_List])
        #company_list_setup = Company_List(self.__Company_List, comboBox_IO, FOLDER, MANAGE, INVOICE_MANAGE)
        #company_list_setup.set_plot_tool(self.sc)
        company_list_name()
        
        #button
        self.__capture_button : QPushButton = self.findChild(QPushButton, "capture_button")
        self.__save_button : QPushButton = self.findChild(QPushButton, "save_button")
        self.__process_button : QPushButton = self.findChild(QPushButton, "process_button")
        self.__error_button : QPushButton = self.findChild(QPushButton, "error_button")
        self.__add_folder_button: QPushButton = self.findChild(QPushButton, "add_folder_button")
        self.__delete_folder_button : QPushButton = self.findChild(QPushButton, "delet_folder_button")
        self.__setting_button: QToolButton = self.findChild(QToolButton, "setting_button")
        
        pushButton_IO.set_pushButton_list([self.__capture_button, self.__save_button, self.__process_button, self.__error_button,
                                           self.__add_folder_button, self.__delete_folder_button, self.__setting_button ])
        # EditLine Box
        self.__words = []
        self.__search_company_name_lineBox: QLineEdit = self.findChild(QLineEdit, "search_company_name_lineBox")


        print("initailize UI componenet...")
        self.setUpMainWindow()
        self.show()

    """ Button Click Group """
    def capture_click (self):
        print("capture clicked...")

    def save_click (self):
        print("save clicked...")

    def process_click (self):
        print("process clicked...")

    def error_click (self):
        print("error clicked...")

    def setting_click(self):
        print("setting button clicked...")

    def add_folder_click(self):
        self.file_IO()
        self.comboBox_IO()
        print("add folder clicked...")

    def delete_folder_click(self):
        ''' refresh combobox and file explorer'''

        print("delete folder clicked...")

    """ ComboBox Click Group """
    def company_name_comboBox_IO(self):
        comboBox_IO.combo_deliever_index(self.__Company_List)
        comboBox_IO.find_commpany_path(self.__Company_List.objectName())

        # Recieve image: 
        img_path = comboBox_IO.find_first_images_path("Company_ComboBox")[0]
        self.sc.plot_image(img_path)
        self.sc.draw()

    """ Draw Rectangle """
    def on_rectangle_select(self, eclick, erelease):
        # Retrieve the coordinates of the selected rectangle
        x1, y1 = eclick.xdata, eclick.ydata
        x2, y2 = erelease.xdata, erelease.ydata

        # Draw a rectangle using the selected coordinates
        rect = patches.Rectangle((x1, y1), x2 - x1, y2 - y1, edgecolor='r', facecolor='none')
        self.sc.fig.gca().add_patch(rect)
        print("one rectangle is drawn on the image...")
        print(f"rectangle position {x1,y1}")
        print(f"rectangle position {y1,y2}")
        
        self.sc.draw()
    
    """ File Explore Events"""
    def populate_tree_view(self, path):
        root_item = QTreeWidgetItem(self.__File_Explorer_Widget, [path])  # Create the root item with the given path
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
        if os.path.isdir(file_path):
            self.__File_Explorer_Widget.clear()  # Clear the tree view
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

    """ Information Input/Output and Refresh"""
    def file_IO(self):
        # File IO
        self.__File_Explorer_Widget.setHeaderLabels(["Name"])  # Set header labels for columns
        self.__File_Explorer_Widget.setRootIsDecorated(True)  # Show the root entries as decorated items
        self.__File_Explorer_Widget.setAlternatingRowColors(True)  # Enable alternating row colors

        # Enable drag and drop events
        self.__File_Explorer_Widget.setDragEnabled(True)
        self.__File_Explorer_Widget.setAcceptDrops(True)
        self.__File_Explorer_Widget.setDropIndicatorShown(True)

        # Connect double-click event to handle folder navigation
        self.__File_Explorer_Widget.itemDoubleClicked.connect(self.handle_double_click)

    def edit_line_box_IO(self):
        completer : QCompleter = QCompleter([word.lower() for word in self.__words], self.__search_company_name_lineBox)
        completer.setFilterMode(Qt.MatchFlag.MatchContains)  # Match suggestions containing the input text
        self.__search_company_name_lineBox.setCompleter(completer)

    def button_IO(self):
        self.__capture_button.clicked.connect(self.capture_click)
        self.__save_button.clicked.connect(self.save_click)
        self.__process_button.clicked.connect(self.process_click)
        self.__error_button.clicked.connect(self.error_click)
        self.__setting_button.clicked.connect(self.setting_click)
        self.__add_folder_button.clicked.connect(self.add_folder_click)
        self.__delete_folder_button.clicked.connect(self.delete_folder_click)

    def comboBox_IO(self):
        self.__words = comboBox_IO.combo_recieve_list(self.__Company_List)  # this will represent the list on ComboBox
        self.__Company_List.addItems(self.__words)
        self.__Company_List.currentIndexChanged.connect(self.company_name_comboBox_IO)  
    
    def img_IO(self):
        pass
        '''
        img_path = comboBox_IO.find_first_images_path(self.__Company_List.objectName())[0]
        self.sc.plot_image(img_path)
        self.rs = RectangleSelector(self.sc.fig.gca(), self.on_rectangle_select)
        '''
    """ Main Window Set Up """
    def setUpMainWindow(self):
        print("Loading UI data...")

        """ Layout Matplot"""
        self.sc = Canvas(self)  # sc -> canvas fig is included in canvas
        self.toolbar = NavigationToolbar(self.sc, self)

        # match with the widget size
        matplot_layout_width = self.__Matplot_VLayout.sizeHint().width()
        matplot_layout_height = self.__Matplot_VLayout.sizeHint().height()

        # add matplot toolbar and canvas object to the matplot_VLayout
        self.__Matplot_VLayout.addWidget(self.toolbar)
        self.__Matplot_VLayout.addWidget(self.sc)

        """ Layout DataBase Entry"""

        """ UI Component Action"""
        # Button IO
        self.button_IO()

        # Combox IO
        self.comboBox_IO()

        # EditLine IO
        self.edit_line_box_IO()

        # File IO
        self.file_IO()

        """ plot image / Shape """
        self.img_IO()
              
        print("Window Set up Complete ")

# Run the program
if __name__ == '__main__':
    print("application start....")
    app = QApplication(sys.argv)    
    dialog = ProgressDialog()
    dialog.exec()
    window = MainWindow()
    window.populate_tree_view("C:\\Users\\zhouw\\OneDrive\\Documents\\vs\\Invoice Processing\\python_p3_Modulization\\test Folder")  # Set the initial root path for the tree view

    window.show()
    sys.exit(app.exec())
    print("application killed")
