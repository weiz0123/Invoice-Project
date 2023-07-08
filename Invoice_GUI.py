
""" System """
import sys
import numpy as np
import os
import threading

""" PyQt5/6 """
from PyQt6 import uic
from PyQt6.QtGui import QPixmap, QPalette, QColor
from PyQt6.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QWidget, QGraphicsView,QWidget, QLabel, QFrame, QComboBox, QPushButton, QHBoxLayout, QTabWidget, QScrollArea, QProgressBar, QDialog)
from PyQt6.QtCore import Qt, QThread, QTimer, pyqtSignal

""" MatPlot Library"""
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas, NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
from matplotlib.widgets import RectangleSelector
import matplotlib.patches as patches

""" Instance """
from Folder_Management import Folder, Invoice_Source_Management, Folder_Management

ui_file_path = "C:\\Users\\zhouw\\OneDrive\\Documents\\vs\\Invoice Processing\\python_p3_Modulization\\proccessed\\Invoice_Management_System.ui"
PATH = "C:\\Users\\zhouw\\OneDrive\\Documents\\vs\\Invoice Processing\\python_p3_Modulization\\test Folder"
#
""" Folder Management Section"""  
FOLDER = Folder(PATH)
MANAGE = Folder_Management()
INVOICE_MANAGE = Invoice_Source_Management()
def Initialize_Folder_System(root_folder_path:str):

    MANAGE.refresh(FOLDER)
    INVOICE_MANAGE.refresh_image_folder(FOLDER)
    MANAGE.refresh(FOLDER) # refresh when new item is added to the file
    print("Initialize Info Complete...")

def company_list_name():
    aList = []
    for i in range(FOLDER.get_folder().getSize()//2):
        each_company_path:str = FOLDER.get_folder().getItem(i).get_root()
        name = each_company_path[each_company_path.rfind('\\')+1:]
        aList.append(name)
    return aList

def get_commpany_path()

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
        self.initializeUI()

    def initializeUI(self):
        """ Set up the application for all ui components """
        uic.loadUi(ui_file_path, self)
        self.setWindowTitle("Invoice Management")

        """ Instance of Layout Componenet"""
        self.__Tab_HLayout : QHBoxLayout = self.findChild(QHBoxLayout, "Tab_HLayout")
        self.__Matplot_VLayout: QVBoxLayout = self.findChild(QVBoxLayout, "Matplot_VLayout")
        
        """ Instance of Componenet UI """
        # widget
        self.__Tab_Widget : QTabWidget = self.findChild(QTabWidget, "Tab_Widget")
        #container
        self.__Company_List : QComboBox = self.findChild(QComboBox, "Company_ComboBox")
        #button
        self.__capture_button : QPushButton = self.findChild(QPushButton, "capture_button")
        self.__save_button : QPushButton = self.findChild(QPushButton, "save_button")
        self.__process_button : QPushButton = self.findChild(QPushButton, "process_button")
        self.__error_button : QPushButton = self.findChild(QPushButton, "error_button")

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

    """ Draw Rectangle """
    def on_rectangle_select(self, eclick, erelease):
        # Retrieve the coordinates of the selected rectangle
        x1, y1 = eclick.xdata, eclick.ydata
        x2, y2 = erelease.xdata, erelease.ydata

        # Draw a rectangle using the selected coordinates
        rect = patches.Rectangle((x1, y1), x2 - x1, y2 - y1, edgecolor='r', facecolor='none')
        self.sc.fig.gca().add_patch(rect)
        self.sc.draw()

    def setUpMainWindow(self):

        """ Layout Matplot"""
        self.sc = Canvas(self)  # sc -> canvas fig is included in canvas
        toolbar = NavigationToolbar(self.sc, self)
        # match with the widget size
        matplot_layout_width = self.__Matplot_VLayout.sizeHint().width()
        matplot_layout_height = self.__Matplot_VLayout.sizeHint().height()
        # add matplot toolbar and canvas object to the matplot_VLayout
        self.__Matplot_VLayout.addWidget(toolbar)
        self.__Matplot_VLayout.addWidget(self.sc)
        """ plot image / Shape """
        #self.sc.plot_image("C:\\Users\\zhouw\\OneDrive\\Documents\\vs\\Invoice Processing\\python_p3_Modulization\\test Folder\\baffin\\images\\364133.jpg")
        self.rs = RectangleSelector(self.sc.fig.gca(), self.on_rectangle_select)
        
        """ Layout DataBase Entry"""



        """ UI Component Action"""
        # Button Output
        self.__capture_button.clicked.connect(self.capture_click)
        self.__save_button.clicked.connect(self.save_click)
        self.__process_button.clicked.connect(self.process_click)
        self.__error_button.clicked.connect(self.error_click)
        # Combox Output

        # User Output
        self.__Company_List.addItems(company_list_name())
        


# Run the program
if __name__ == '__main__':
    app = QApplication(sys.argv)    
    dialog = ProgressDialog()
    dialog.exec()
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
