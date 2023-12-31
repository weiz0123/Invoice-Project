from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import  Qt
def show_status(self, company, num_inv):
    """
    show the message in status bar
    """
    message = f"Current Company: {company}, Number of Invoice: {num_inv}"
    message_label = QtWidgets.QLabel(message)
    message_label.setAlignment(Qt.AlignmentFlag.AlignRight)
    self.statusbar.addWidget(message_label, 1)
"""
if we want to split the message to left and right, just create another Qlabel aligned to left
"""

