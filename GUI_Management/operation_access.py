from PyQt6.QtCore import pyqtSignal
class Operation_Access:
    
    update_company_comboBox = pyqtSignal()
    def __init__(self, user):
        self.user = user
        #* Live Data
        self.selected_company = self.user.display_company_name()[0]
        self.selected_category = self.user.display_extraction_category()[0]
        

    #TODO: Notice: initialize live data structure format

    #TODO: Establish the following tunnel
    def update_selected_company(self, company_index):
        company_list = self.user.display_company_name() #* not put in init, making sure to have the most updated version of the list
        self.selected_company = company_list[company_index]

    def update_selected_category(self, category_index):
        category_list = self.user.display_extraction_category()
        self.selected_category = category_list[category_index]


    #* The following tunnel will be linked to all the emiter from GUI
    #TODO Review: review proccess access, reivew ULM and Data access for the process of extracting and updating data
    def recieve_update_position_data(self, pos1, pos2 ):
        #print(f"company name: {self.selected_company}, category: {self.selected_category}, pos1: {pos1}, pos2: {pos2}")
        self.user.update_extract_position_information(self.selected_company, self.selected_category, pos1, pos2)
    
    #TODO: Redesign: remove or clear position data will be automatically done once the category is removed

    #TODO Design: extract information

    def recieve_extraction_data(self):
        company = self.selected_company
        self.user.extract_target_company_image(company)
    


