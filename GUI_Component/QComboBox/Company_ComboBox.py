import sys
sys.path.append("C:\\Users\\zhouw\\OneDrive\\Documents\\personal sci project\\vs\\ProjectIII")
from PyQt6.QtWidgets import QComboBox, QWidget
from PyQt6.QtCore import pyqtSignal


# ComboBox ID: Company_ComboBox
#! why does it need to be inherited???
class Company_ComboBox(QWidget):

    selected_company_index = pyqtSignal(int)
    def __init__(self, comboBox:QComboBox, user):
        super().__init__()
        self.user = user
        self.comboBox : QComboBox = comboBox  #  get comboBox
        #self.comboBox_item = self.user.display_company_name() -> this function needs to be called all the time due to the update requirement
        self.set_comboBox_item()  #  set list to comboBox
        self.set_selected_index(0) # default the setting 
        self.comboBox.currentIndexChanged.connect(self.item_change_listener)
        self.emit = True

    def item_change_listener(self):
        if self.emit:
            self.selected_company_index.emit(self.comboBox.currentIndex())
            

    def set_comboBox_item(self) -> None:
        ''' add list to the combobox for display'''
        self.comboBox.addItems(self.user.display_company_name())

    def set_selected_index(self, position:int)-> None:
        if position < len(self.user.display_company_name()):
            self.comboBox.setCurrentIndex(position)
        else:
            raise Exception( 'company name is out of index in the comboBox')  
    
    def refresh(self):
        self.emit = False
        self.comboBox.clear()
        self.set_comboBox_item()
        self.set_selected_index(0)
    
        print(f"succeed {self.comboBox.count()}")
        self.emit = True
    

         




    

