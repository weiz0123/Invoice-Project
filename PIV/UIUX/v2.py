# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '4.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(646, 506)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Tab_Widget = QtWidgets.QTabWidget(self.centralwidget)
        self.Tab_Widget.setTabPosition(QtWidgets.QTabWidget.North)
        self.Tab_Widget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.Tab_Widget.setMovable(False)
        self.Tab_Widget.setObjectName("Tab_Widget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.line = QtWidgets.QFrame(self.tab)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_4.addWidget(self.line, 0, 0, 1, 1)
        self.Extraction_GridLayout = QtWidgets.QGridLayout()
        self.Extraction_GridLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.Extraction_GridLayout.setObjectName("Extraction_GridLayout")
        self.search_company_name_lineBox = QtWidgets.QLineEdit(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search_company_name_lineBox.sizePolicy().hasHeightForWidth())
        self.search_company_name_lineBox.setSizePolicy(sizePolicy)
        self.search_company_name_lineBox.setAutoFillBackground(False)
        self.search_company_name_lineBox.setText("")
        self.search_company_name_lineBox.setObjectName("search_company_name_lineBox")
        self.Extraction_GridLayout.addWidget(self.search_company_name_lineBox, 0, 0, 1, 2)
        self.Company_ComboBox = QtWidgets.QComboBox(self.tab)
        self.Company_ComboBox.setObjectName("Company_ComboBox")
        self.Extraction_GridLayout.addWidget(self.Company_ComboBox, 1, 0, 1, 1)
        self.Category_ComboBox = QtWidgets.QComboBox(self.tab)
        self.Category_ComboBox.setObjectName("Category_ComboBox")
        self.Extraction_GridLayout.addWidget(self.Category_ComboBox, 1, 1, 1, 1)
        self.process_button = QtWidgets.QPushButton(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.process_button.sizePolicy().hasHeightForWidth())
        self.process_button.setSizePolicy(sizePolicy)
        self.process_button.setObjectName("process_button")
        self.Extraction_GridLayout.addWidget(self.process_button, 2, 0, 1, 2)
        self.Matplot_VLayout = QtWidgets.QVBoxLayout()
        self.Matplot_VLayout.setObjectName("Matplot_VLayout")
        self.Extraction_GridLayout.addLayout(self.Matplot_VLayout, 0, 2, 4, 5)
        self.gridLayout_4.addLayout(self.Extraction_GridLayout, 1, 0, 1, 1)
        self.Tab_Widget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(self.tab_2)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 2, 2, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 2, 1, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget, 1, 1, 1, 6)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 0, 1, 1, 3)
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 2, 3, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(self.tab_2)
        self.comboBox_2.setObjectName("comboBox_2")
        self.gridLayout.addWidget(self.comboBox_2, 0, 5, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 0, 4, 1, 1)
        self.comboBox_3 = QtWidgets.QComboBox(self.tab_2)
        self.comboBox_3.setObjectName("comboBox_3")
        self.gridLayout.addWidget(self.comboBox_3, 0, 6, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 2, 4, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.Tab_Widget.addTab(self.tab_2, "")
        self.horizontalLayout.addWidget(self.Tab_Widget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 646, 18))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menubar.sizePolicy().hasHeightForWidth())
        self.menubar.setSizePolicy(sizePolicy)
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statusbar.sizePolicy().hasHeightForWidth())
        self.statusbar.setSizePolicy(sizePolicy)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.dockWidget_3 = QtWidgets.QDockWidget(MainWindow)
        self.dockWidget_3.setObjectName("dockWidget_3")
        self.dockWidgetContents_3 = QtWidgets.QWidget()
        self.dockWidgetContents_3.setObjectName("dockWidgetContents_3")
        self.dockWidget_3.setWidget(self.dockWidgetContents_3)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget_3)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionImport_New_Company = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/open.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionImport_New_Company.setIcon(icon)
        self.actionImport_New_Company.setObjectName("actionImport_New_Company")
        self.actionImport_PDF_JPG = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/file-import.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionImport_PDF_JPG.setIcon(icon1)
        self.actionImport_PDF_JPG.setObjectName("actionImport_PDF_JPG")
        self.actionWork_Space = QtWidgets.QAction(MainWindow)
        self.actionWork_Space.setObjectName("actionWork_Space")
        self.view_image = QtWidgets.QAction(MainWindow)
        self.view_image.setObjectName("view_image")
        self.actionCheck_Images_With_Position_Data = QtWidgets.QAction(MainWindow)
        self.actionCheck_Images_With_Position_Data.setObjectName("actionCheck_Images_With_Position_Data")
        self.actionCurrent_Selected_Company = QtWidgets.QAction(MainWindow)
        self.actionCurrent_Selected_Company.setObjectName("actionCurrent_Selected_Company")
        self.actionAll_Company = QtWidgets.QAction(MainWindow)
        self.actionAll_Company.setObjectName("actionAll_Company")
        self.actionGuidence = QtWidgets.QAction(MainWindow)
        self.actionGuidence.setObjectName("actionGuidence")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.Current_Selected_Company_Export = QtWidgets.QAction(MainWindow)
        self.Current_Selected_Company_Export.setObjectName("Current_Selected_Company_Export")
        self.actionAll_Company_2 = QtWidgets.QAction(MainWindow)
        self.actionAll_Company_2.setObjectName("actionAll_Company_2")
        self.actionOpen_Working_Space_Directory = QtWidgets.QAction(MainWindow)
        self.actionOpen_Working_Space_Directory.setObjectName("actionOpen_Working_Space_Directory")
        self.Export_For_Current_Company = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/excel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Export_For_Current_Company.setIcon(icon2)
        self.Export_For_Current_Company.setObjectName("Export_For_Current_Company")
        self.actionExport_All_Company_to_Excel = QtWidgets.QAction(MainWindow)
        self.actionExport_All_Company_to_Excel.setObjectName("actionExport_All_Company_to_Excel")
        self.actionView_All_Image = QtWidgets.QAction(MainWindow)
        self.actionView_All_Image.setObjectName("actionView_All_Image")
        self.actionhome = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/icons/home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionhome.setIcon(icon3)
        self.actionhome.setObjectName("actionhome")
        self.actiongo_back = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/icons/right.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actiongo_back.setIcon(icon4)
        self.actiongo_back.setObjectName("actiongo_back")
        self.actiongo_next = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/icons/arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actiongo_next.setIcon(icon5)
        self.actiongo_next.setObjectName("actiongo_next")
        self.actionzoom = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/icons/zoom-in.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionzoom.setIcon(icon6)
        self.actionzoom.setObjectName("actionzoom")
        self.actionselection_box = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/icons/selection-box.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionselection_box.setIcon(icon7)
        self.actionselection_box.setObjectName("actionselection_box")
        self.menuFile.addAction(self.actionImport_New_Company)
        self.menuFile.addAction(self.actionOpen_Working_Space_Directory)
        self.menuFile.addAction(self.actionWork_Space)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionImport_PDF_JPG)
        self.menuFile.addAction(self.Export_For_Current_Company)
        self.menuFile.addAction(self.actionExport_All_Company_to_Excel)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionView_All_Image)
        self.menubar.addAction(self.menuFile.menuAction())
        self.toolBar.addAction(self.actionhome)
        self.toolBar.addAction(self.actionImport_PDF_JPG)
        self.toolBar.addAction(self.actionImport_New_Company)
        self.toolBar.addAction(self.actiongo_back)
        self.toolBar.addAction(self.actiongo_next)
        self.toolBar.addAction(self.Export_For_Current_Company)
        self.toolBar.addAction(self.actionzoom)
        self.toolBar.addAction(self.actionselection_box)

        self.retranslateUi(MainWindow)
        self.Tab_Widget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.process_button.setText(_translate("MainWindow", "process"))
        self.Tab_Widget.setTabText(self.Tab_Widget.indexOf(self.tab), _translate("MainWindow", "Extraction"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_5.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_2.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_4.setText(_translate("MainWindow", "Search"))
        self.pushButton_3.setText(_translate("MainWindow", "PushButton"))
        self.Tab_Widget.setTabText(self.Tab_Widget.indexOf(self.tab_2), _translate("MainWindow", "Data System"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionImport_New_Company.setText(_translate("MainWindow", "Open Company Folder"))
        self.actionImport_PDF_JPG.setText(_translate("MainWindow", "Import PDF/JPG"))
        self.actionWork_Space.setText(_translate("MainWindow", "Add Work Space Directory"))
        self.view_image.setText(_translate("MainWindow", "View All Image From Current Company"))
        self.actionCheck_Images_With_Position_Data.setText(_translate("MainWindow", "Check Images With Position Data"))
        self.actionCurrent_Selected_Company.setText(_translate("MainWindow", "Current Selected Company"))
        self.actionAll_Company.setText(_translate("MainWindow", "All Company"))
        self.actionGuidence.setText(_translate("MainWindow", "Guidence"))
        self.action_2.setText(_translate("MainWindow", "?"))
        self.Current_Selected_Company_Export.setText(_translate("MainWindow", "Current Selected Company"))
        self.actionAll_Company_2.setText(_translate("MainWindow", "All Company"))
        self.actionOpen_Working_Space_Directory.setText(_translate("MainWindow", "Open Working Space Directory"))
        self.Export_For_Current_Company.setText(_translate("MainWindow", "Export Current Company to Excel"))
        self.actionExport_All_Company_to_Excel.setText(_translate("MainWindow", "Export All Company to Excel"))
        self.actionView_All_Image.setText(_translate("MainWindow", "View All Image"))
        self.actionhome.setText(_translate("MainWindow", "home"))
        self.actiongo_back.setText(_translate("MainWindow", "go_back"))
        self.actiongo_back.setShortcut(_translate("MainWindow", "Ctrl+Z"))
        self.actiongo_next.setText(_translate("MainWindow", "go_next"))
        self.actiongo_next.setShortcut(_translate("MainWindow", "Ctrl+Y"))
        self.actionzoom.setText(_translate("MainWindow", "zoom"))
        self.actionselection_box.setText(_translate("MainWindow", "selection_box"))
import resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
