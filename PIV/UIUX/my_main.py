import Window_Level_Management  # Updated import
import os
from functions import *
from PyQt5 import QtCore, QtGui, QtWidgets

path = os.getcwd()

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = Window_Level_Management.ExtendedUi_MainWindow(path)

    # Updated import for the UI class
    ui = Window_Level_Management.ExtendedUi_MainWindow(path)  # Change this line to use ExtendedUi_MainWindow
    MainWindow.show()
    sys.exit(app.exec())
