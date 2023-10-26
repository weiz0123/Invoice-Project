import sys
sys.path.append("C:\\Users\\zhouw\\OneDrive\\Documents\\personal sci project\\vs\\ProjectIII")
import keyboard 
from PyQt6.QtWidgets import QLineEdit, QWidget, QCompleter,QApplication, QDialog, QLabel, QVBoxLayout, QPushButton

from PyQt6.QtCore import pyqtSignal, Qt, QThread


import time
#* Functionality
#* 1) search based on provided company name
#* 2) once company is selected, sent the name to the combobox
class company_search_lineEdit(QWidget):
    send_company_name_to_company_list_comboBox = pyqtSignal(int)

    def __init__(self, lineEdit:QLineEdit, user):
        super().__init__()
        self.lineEdit : QLineEdit = lineEdit  
        self.user = user
        #* init target word list
        self.edit_line_box_IO()

        #* detect if there is any character typed in
        self.lineEdit.textChanged.connect(self.key_board_IO)
        
    #* search word method
    def edit_line_box_IO(self):
        self.target = [word.lower() for word in self.user.display_company_name()]
        completer = QCompleter(self.target, self.lineEdit)
        completer.setFilterMode(Qt.MatchFlag.MatchContains)
        self.lineEdit.setCompleter(completer)

    #* send the signal that enter key has been pressed
    def on_enter_pressed(self, event):
        self.target = [word.lower() for word in self.user.display_company_name()]
        self.current_text = self. lineEdit.text()
        if self.current_text.upper() not in self.target and self.current_text.lower() not in self.target:
            #! multi thread is needed    
            print('error comapny doesnt exist')

        else:
        
            
            input_text_index = self.target.index(self.current_text)
        #    print(f"position {input_text_index}")

            self.send_company_name_to_company_list_comboBox.emit(input_text_index)

    #* functionality can be ignored for the following function        
    def key_board_IO(self):
        print(self.lineEdit.hasFocus())
        if self.lineEdit.hasFocus():
            try:
                keyboard.on_press_key('enter', self.on_enter_pressed)
            
            except Exception as e:
                print(e.args)

        
