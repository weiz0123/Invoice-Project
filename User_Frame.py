import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QTextEdit, QLineEdit, QMenuBar, QAction
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt5.QtWidgets import QFileDialog
import os
from PyQt5.QtWidgets import QMainWindow, QTreeView, QVBoxLayout, QWidget, QApplication, QFileSystemModel
from PyQt5.QtCore import QModelIndex
from PyQt5.QtWidgets import QMainWindow, QTreeView, QVBoxLayout, QWidget, QApplication
from PyQt5.QtCore import QFileSystemModel, QModelIndex

class MyGUI(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set window title and size
        self.setWindowTitle("GUI Example")
        self.setGeometry(100, 100, 800, 600)

        # Create the central widget and layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # Create the menu bar and menu
        menu_bar = QMenuBar(self)
        file_menu = menu_bar.addMenu("File")
        self.setMenuBar(menu_bar)

        # Create actions for the menu
        open_action = QAction(QIcon(), "Open", self)
        open_action.triggered.connect(self.open_file)
        file_menu.addAction(open_action)

        # Create the text input boxes
        self.text_input1 = QLineEdit()
        self.text_input2 = QLineEdit()

        # Create the Matplotlib plot
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)

        # Create the file explorer
        self.file_explorer = QTextEdit()
        self.file_explorer.setReadOnly(True)

        # Add the widgets to the layout
        self.layout.addWidget(self.text_input1)
        self.layout.addWidget(self.text_input2)
        self.layout.addWidget(self.canvas)
        self.layout.addWidget(self.file_explorer)

       # Set up the file system model
        self.file_system_model = QFileSystemModel()
        self.file_system_model.setRootPath("")  # Set the root path to the current directory

        # Create the file explorer widget
        self.file_explorer = QTreeView()
        self.file_explorer.setModel(self.file_system_model)
        self.file_explorer.setRootIndex(self.file_system_model.index(""))  # Set the root index to the current directory

        # Set up the main window layout
        main_widget = QWidget()
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.file_explorer)
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

    def open_file(self):
            # Get the desktop path
            desktop_path = os.path.expanduser("~/Desktop")

            # Open file dialog with initial directory set to the desktop path and parent as the main window
            file_path, _ = QFileDialog.getOpenFileName(self, "Open File", desktop_path, "All Files (*.*)")
            if file_path:
                self.file_explorer.append(file_path)
    def handle_file_selection(self, index: QModelIndex):
        file_path = self.file_system_model.filePath(index)
        print("Selected file:", file_path)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = MyGUI()
    gui.show()
    gui.open_file()
    sys.exit(app.exec_())
