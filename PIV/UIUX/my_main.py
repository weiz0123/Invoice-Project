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
    initialize_file_explorer(ui, path)
    initialize_search_box(ui)
    update_company_combo_box(ui, path)
    update_category_combo_box(ui)
    triggered_tools(ui, path)
    update_status(ui, path)

    MainWindow.show()
    sys.exit(app.exec())

