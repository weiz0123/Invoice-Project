from PyQt6.QtWidgets import (QMenuBar,QMenu, QMainWindow, QWidget)
from PyQt6.QtGui import  QAction,QFileSystemModel
from PyQt6.QtCore import pyqtSignal
class Menu_Bar(QMainWindow):
    process = pyqtSignal()
    def __init__(self, menu_bar:QMenuBar, user):
        super().__init__()
        self.menu:QMenu = menu_bar.findChild(QMenu, "menuFile")
        print(self.menu)
        self.user = user 
        self.current_company_export_action:QAction = self.find_target_child("Export_For_Current_Company")

        self._connection()
        
    def find_target_child(self,target_name):
        for action in self.menu.actions():
            if action.objectName() == target_name:
                return action
        
        raise Exception("unable to find the action from the menu")
    
    def _connection(self):
        self.current_company_export_action.triggered.connect(self.process_trigger)

    def process_trigger(self):
        self.process.emit()