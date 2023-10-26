import sys
sys.path.append("C:\\Users\\zhouw\\OneDrive\\Documents\\personal sci project\\vs\\ProjectIII")
from PyQt6 import uic
from PyQt6.QtGui import QPixmap, QPalette, QColor, QDragEnterEvent, QDropEvent, QIcon, QShortcut
from PyQt6.QtWidgets import ( QStyle, QGridLayout, QToolButton,QTreeView,QTreeWidget,QTreeWidgetItem, QLineEdit, QCompleter, QApplication, QMainWindow, QVBoxLayout, QWidget, QGraphicsView,QWidget, QLabel, QFrame, QComboBox, QPushButton, QHBoxLayout, QTabWidget, QScrollArea, QProgressBar, QDialog)
from PyQt6.QtCore import Qt, QThread, QTimer, pyqtSignal,QModelIndex, QMimeData
from PyQt5.QtWidgets import QFileSystemModel
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas, NavigationToolbar2QT as NavigationToolbar


from GUI_Component.QComboBox.Company_ComboBox import Company_ComboBox
from GUI_Component.QComboBox.Category_ComboBox import Category_ComboBox
from GUI_Component.QPushButton.Process_Button_Group import Process_Button, Save_Button, Exist_Button
from GUI_Component.QEditBox.company_search_editBox import company_search_lineEdit
from GUI_Component.QWidget.File_Explorer_Widget import File_Explorer_Widget
from GUI_Managment.Image_Display_GUI import Canvas, NavigationToolbar
from User_Action.Data_Access import Data_Access
from User_Action.Process_Access import Process_Access
from PyQt6.QtGui import QKeySequence
from GUI_Managment.user_level_management import ULM
from GUI_Managment.operation_access import Operation_Access
ui_file_path = "C:\\Users\\zhouw\\OneDrive\\Documents\\vs\\ProjectIII\\GUI_Managment\\Invoice_Management_System_Test_A_.ui"
test_path = "C:\\Users\\zhouw\\OneDrive\\Documents\\vs\\ProjectIII\\Test_Resource\\company_test"

class MainWindow(QWidget):
    def __init__(self):
        self.user = ULM(test_path)
        self.operation = Operation_Access(self.user)
        super().__init__()
        #* UI
        self._initialize_ui()

    def _initialize_ui(self):
        uic.loadUi(ui_file_path, self)
        self.setWindowTitle("Invoice Management")


if __name__ == '__main__':
    app = QApplication(sys.argv)    
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
    