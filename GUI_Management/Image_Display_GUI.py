import sys
sys.path.append("C:\\Users\\zhouw\\OneDrive\\Documents\\personal sci project\\vs\\ProjectIII")

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas, NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
from matplotlib.widgets import RectangleSelector
import matplotlib.patches as patches
import numpy as np
from User_Action.Data_Access import Data_Access
from User_Action.Process_Access import Process_Access
from PyQt6.QtCore import pyqtSignal

#TODO: Redesign: 
class Canvas(FigureCanvas):


    position_data = pyqtSignal(list, list)
    def __init__(self, parent, user):
        self.fig, self.ax= plt.subplots(figsize=(5, 4), dpi=200)
        self.fig.subplots_adjust(left=0.043, right=0.927, bottom=0.094, top=0.950)
        self.user = user
        super().__init__(self.fig)
        self.current_company = None
        self.plot_image(0) # default company_index is set to 0, meaning automatically display the first company's first image in the company list
        
        self.pos1 = []
        self.pos2 = []
    

    def plot_image (self, company_index):
        
        self.ax.clear()  # Clear any previous plot
        self.current_company = self.user.display_company_name()[company_index] # display_company_name return a list of company name, 
        img = self.user.display_first_image_of_company(self.current_company) # find the first image of the selected company name
        
        # plot the image and enable rectangle painting
        try:
            self.ax.imshow(img)
            self.rs = RectangleSelector(self.fig.gca(), self.on_rectangle_select)
            # display the plot
            self.draw()
        except Exception:
            print("unable to plot any image")


    def on_rectangle_select(self, eclick, erelease):
        # Retrieve the coordinates of the selected rectangle
        x1, y1 = eclick.xdata, eclick.ydata
        x2, y2 = erelease.xdata, erelease.ydata
        rect = patches.Rectangle((x1, y1), x2 - x1, y2 - y1, edgecolor='r', facecolor='none')
        self.fig.gca().add_patch(rect)
        self.pos1 = [x1, y1]
        self.pos2 = [x2, y2]
        self.position_data.emit( self.pos1, self.pos2)
        self.draw()

    #TODO: Important Notice: following draw rect function needs to be re-viewed
    #! the following function may be deleted
    def erase_rectangle(self, pos1, pos2):
        # Loop through the stored rectangles and remove the one with matching positions
        for rect in self.ax.patches:
            x1, y1 = rect.get_xy()
            x2, y2 = x1 + rect.get_width(), y1 + rect.get_height()
            if (x1, y1) == tuple(pos1) and (x2, y2) == tuple(pos2):
                rect.remove()
                self.draw()
                
    def erase_all_rectangles(self, null_pos1, null_pos2):
    # Loop through all the stored rectangles and remove each one
        for rect in self.ax.patches:
            rect.remove()
        self.draw()

    def redraw_rectangle(self):
        try:
            self.erase_rectangle(self.pos1, self.pos2)
        except Exception:
            print('Nothing to remove')

class Toolbar(NavigationToolbar):
    def __init__(self, *args, **kwargs):
        super(Toolbar, self).__init__(*args, **kwargs)
