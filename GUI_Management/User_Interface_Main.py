import sys

sys.path.append("C:\\Users\\zhouw\\OneDrive\\Documents\\personal sci project\\vs\\ProjectIII")
from PyQt6 import uic
from PyQt6.QtWidgets import (QMenuBar, QTreeWidget, QLineEdit, QApplication, QMainWindow, QVBoxLayout, QComboBox,
                             QPushButton)

from GUI_Component.QComboBox.Company_ComboBox import Company_ComboBox
from GUI_Component.QComboBox.Category_ComboBox import Category_ComboBox
from GUI_Component.QPushButton.Process_Button_Group import Process_Button
from GUI_Component.QEditBox.company_search_editBox import company_search_lineEdit
from GUI_Component.QWidget.File_Explorer_Widget import File_Explorer_Widget
from GUI_Managment.Image_Display_GUI import Canvas, NavigationToolbar
from GUI_Managment.user_level_management import ULM
from GUI_Managment.operation_access import Operation_Access
from GUI_Component.menu_bar.Menu_Bar import Menu_Bar

ui_file_path = "C:\\Users\\zhouw\\OneDrive\\Documents\\personal sci project\\vs\\ProjectIII\\GUI_Managment\\Invoice_Management_System_Test_A_.ui"
test_path = "C:\\Users\\zhouw\\OneDrive\\Documents\\personal sci project\\vs\\ProjectIII\\Test_Resource\\company_test"

class MainWindow(QMainWindow):
    def __init__(self):
        self.user = ULM(test_path)
        self.operation = Operation_Access(self.user)

        super().__init__()
        # * UI
        self._initialize_ui()
        self._initialize_comboBox()
        self._initialize_lineEdit()
        self._initialize_layout()
        self._initialize_canvas()
        self._initialize_widget()
        self._initialize_button()
        self._initialize_menu_bar()
        self._connection_establishment()
        self.operation_connection()
        self.menu_connection()

    # ======================================================================================================#
    # * UI
    def _initialize_ui(self):
        # set up a main window
        uic.loadUi(ui_file_path, self)
        self.setWindowTitle("Invoice Management")

    def _initialize_lineEdit(self):
        self.company_search_lineEdit = company_search_lineEdit(self.findChild(QLineEdit, 'search_company_name_lineBox'),
                                                               self.user)

    def _initialize_widget(self):
        self.__File_Explorer_Widget: File_Explorer_Widget = File_Explorer_Widget(
            self.findChild(QTreeWidget, "File_Explore_List_Widget"))

    def _initialize_layout(self):
        self.__Matplot_VLayout: QVBoxLayout = self.findChild(QVBoxLayout, "Matplot_VLayout")

    def _initialize_comboBox(self):
        self.company_comboBox = Company_ComboBox(self.findChild(QComboBox, 'Company_ComboBox'), self.user)
        self.category_comboBox = Category_ComboBox(self.findChild(QComboBox, 'Category_ComboBox'), self.user)

    def _initialize_canvas(self):
        self.sc = Canvas(self, self.user)
        self.toolbar = NavigationToolbar(self.sc, self)
        self.__Matplot_VLayout.addWidget(self.toolbar)
        self.__Matplot_VLayout.addWidget(self.sc)

    def _initialize_button(self):
        # !!!!!!
        self.process_button: Process_Button = Process_Button(self.findChild(QPushButton, "process_button"), self.user)

    # TODO: Documentation:
    def _initialize_menu_bar(self):
        menubar = self.findChild(QMenuBar, "menubar")
        self.menu_class = Menu_Bar(menubar, self.user)

    # ======================================================================================================#
    # TODO: Review: review the following connetion, \\ means completed connection, \... means ongoing connection
    '''
    c1: QEditbox send index to company comboBox to display searched company \\
    c2: QEditbox send the signal to access the category file to Data Access \\
    c3: QEditbox send the signal to the plot image in Image_Display_GUI     \\
    c4: 
    
    '''

    # TODO: Redesign: seperate GUI internal connection from connection thorugh operatino access class.
    # TODO: Redesign: sperate class Update_Access class (directly call user_interaction) as a way to orgnize the function called when updating for the watchdogs

    # * connection
    def _connection_establishment(self):
        # * after search the company, searched company is auto showing in comboBox
        self.company_search_lineEdit.send_company_name_to_company_list_comboBox.connect(
            self.company_comboBox.set_selected_index)

        # * after search the company, the first image of the searched company is auto showing in plot
        self.company_search_lineEdit.send_company_name_to_company_list_comboBox.connect(self.sc.plot_image)

        # * showing the image of the selected company in the comboxbox
        self.company_comboBox.selected_company_index.connect(self.sc.plot_image)

        # * when company change, set category to 0 position
        self.company_comboBox.selected_company_index.connect(self.category_comboBox.re_set_position)
        # $ update current selected company

        self.company_comboBox.selected_company_index.connect(self.operation.update_selected_company)

        # * send the selected position of the category

        self.category_comboBox.selected_category.connect(self.operation.update_selected_category)
        # * erase all the rectangle after a category has been set
        self.category_comboBox.erase_rectangle.connect(self.sc.erase_all_rectangles)

        # * update the newest category to file
        self.sc.position_data.connect(self.operation.recieve_update_position_data)

        # TODO!, THIS WILL BE REPLACED BY PROCCESS IN MENU BAR
        # * proccess button
        # $ self.process_button.process.connect(self.operation.recieve_extraction_data)

        # * auto erase if there is a needs to redraw
        self.sc.position_data.connect(self.sc.erase_all_rectangles)

    def menu_connection(self):
        self.menu_class.process.connect(self.operation.recieve_extraction_data)

    def operation_connection(self):
        print("operation connection established")
        # * update company combobox from proccess access
        self.user.update_company_comboBox_signal.connect(self.company_comboBox.refresh)

    def menu_test(self):
        print('test')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
