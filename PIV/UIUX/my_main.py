import v2
from functions import show_status
from PyQt5 import QtCore, QtGui, QtWidgets
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = v2.Ui_MainWindow()
    ui.setupUi(MainWindow)
    show_status(ui, 1, 1)
    MainWindow.show()
    sys.exit(app.exec())