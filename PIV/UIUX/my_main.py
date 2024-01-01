import v2
import os
from functions import *
from PyQt5 import QtCore, QtGui, QtWidgets

path = os.getcwd()
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = v2.Ui_MainWindow()
    ui.setupUi(MainWindow)
    show_status(ui, 1, 1)
    populate_tree(ui, path)
    MainWindow.show()
    sys.exit(app.exec())