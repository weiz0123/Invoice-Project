import sys
from PyQt6 import uic
from PyQt6.QtGui import QPixmap
import numpy as np
from PyQt6.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QWidget, QGraphicsView,QWidget, QLabel, QFrame, QComboBox, QPushButton, QHBoxLayout, QTabWidget)
from PyQt6.QtCore import Qt
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas, NavigationToolbar2QT as NavigationToolbar

from PyQt6.QtGui import QPalette, QColor
import matplotlib.pyplot as plt

from matplotlib.widgets import RectangleSelector
import matplotlib as plt1
import matplotlib.patches as patches


ui_file_path = "C:\\Users\\zhouw\\OneDrive\\Documents\\vs\\Invoice Processing\\python_p3_Modulization\\GUI\\invoice_gui\\Invoice_Management_System.ui"

class Toolbar(NavigationToolbar):
    def __init__(self, *args, **kwargs):
        super(Toolbar, self).__init__(*args, **kwargs)

class Canvas(FigureCanvas):
    def __init__(self, parent):
        self.fig, self.ax = plt.subplots(figsize=(5, 4), dpi=200)
        self.fig.subplots_adjust(left=0.033, right=0.967, bottom=0.094, top=0.950)
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
        self.__Next_Company : QPushButton = self.findChild(QPushButton, "Next_Company_Button")

        self.setUpMainWindow()
        self.show()
    """ Button Click Group """
    def Next_Comapny_Click (self):
        print("clicked...")
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

        self.sc.plot_image("C:\\Users\\zhouw\\OneDrive\\Documents\\vs\\Invoice Processing\\python_p3_Modulization\\GUI\\invoice_gui\\image\\ASL-INVC-324852-32041357-Apr-07-2022-1134.jpg")
        self.rs = RectangleSelector(self.sc.fig.gca(), self.on_rectangle_select)
        

        """ Layout DataBase Entry"""


        """ UI Component Action"""
        self.__Next_Company.clicked.connect(self.Next_Comapny_Click)
        self.__Company_List.addItems(['a','b','c'])
        

def set_dark_theme(app):
    # Create a dark color palette
    palette = app.palette()
    palette.setColor(QPalette.ColorRole.Window, QColor(53, 53, 53))
    palette.setColor(QPalette.ColorRole.WindowText, QColor(255, 255, 255))
    palette.setColor(QPalette.ColorRole.Base, QColor(25, 25, 25))
    palette.setColor(QPalette.ColorRole.AlternateBase, QColor(53, 53, 53))
    palette.setColor(QPalette.ColorRole.ToolTipBase, QColor(255, 255, 255))
    palette.setColor(QPalette.ColorRole.ToolTipText, QColor(255, 255, 255))
    palette.setColor(QPalette.ColorRole.Text, QColor(255, 255, 255))
    palette.setColor(QPalette.ColorRole.Button, QColor(53, 53, 53))
    palette.setColor(QPalette.ColorRole.ButtonText, QColor(255, 255, 255))
    palette.setColor(QPalette.ColorRole.BrightText, QColor(255, 0, 0))
    palette.setColor(QPalette.ColorRole.Link, QColor(42, 130, 218))
    palette.setColor(QPalette.ColorRole.Highlight, QColor(42, 130, 218))
    palette.setColor(QPalette.ColorRole.HighlightedText, QColor(0, 0, 0))

    app.setPalette(palette)


# Run the program
if __name__ == '__main__':
    app = QApplication(sys.argv)
    #set_dark_theme(app)
    window = MainWindow()
    #window.show()
    sys.exit(app.exec())