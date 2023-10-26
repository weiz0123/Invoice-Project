import sys
sys.path.append("C:\\Users\\zhouw\\OneDrive\\Documents\\personal sci project\\vs\\ProjectIII")
from PyQt6.QtWidgets import QPushButton ,QWidget
from PyQt6.QtCore import pyqtSignal
class Process_Button(QWidget):

    process = pyqtSignal()
    def __init__(self, button:QPushButton, user):
        super().__init__()
        self.user = user
        self.button = button
        self.button.clicked.connect(self.emit_clicked)
    
    def emit_clicked(self):
        print('clicked')
        self.process.emit()


