import sys
sys.path.append("C:\\Users\\zhouw\\OneDrive\\Documents\\personal sci project\\vs\\ProjectIII")
from PyQt6.QtWidgets import QComboBox, QWidget, QLineEdit
from PyQt6.QtCore import pyqtSignal


class Category_ComboBox(QWidget):
    erase_rectangle = pyqtSignal(list, list)
    selected_category = pyqtSignal(int)
    
    def __init__(self, comboBox:QComboBox, user):
        super().__init__()
        self.user = user
        self.comboBox : QComboBox = comboBox  #  get comboBox
        self.comboBox_item = ['Invoice number', 'Invoice Date']

        self._set_comboBox_item()
        self.set_selected_index(0) # default the setting 
        self.comboBox.currentIndexChanged.connect(self.item_changed)

    def item_changed(self):
        self.erase_rectangle.emit([], [])
        self.selected_category.emit(self.comboBox.currentIndex())

    def _set_comboBox_item(self) -> None:
        ''' add list to the combobox for display'''
        self.comboBox.addItems(self.comboBox_item)

    def set_selected_index(self, position:int)-> None:
        if position < len(self.comboBox_item):
            self.comboBox.setCurrentIndex(position)
        else:
            raise Exception( 'company name is out of index in the comboBox')   
    
    #8 null index is just used to match the format of the pysignal
    def re_set_position(self, null_index):
        self.set_selected_index(0)



     