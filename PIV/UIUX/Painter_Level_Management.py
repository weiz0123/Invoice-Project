import sys
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QLabel, QTabWidget
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt, QRect


class Painter(QLabel):
    def __init__(self):
        super().__init__()
        self.pixmap = False
        self.start_point = None
        self.end_point = None

    def paintEvent(self, event):
        super().paintEvent(event)

        painter = QPainter(self)
        painter.setPen(QColor(0, 0, 255))  # Blue color for the rectangle outline
        if self.start_point is not None and self.end_point is not None:
            # Calculate the rectangle coordinates using start and end points
            rect = QRect(self.start_point, self.end_point)
            # Draw the rectangle
            painter.drawRect(rect)

    def mousePressEvent(self, event):
        x = event.pos().x()
        y = event.pos().y()
        print(f"Clicked at: ({x}, {y})")
        self.start_point = event.pos()

    def mouseMoveEvent(self, event):
        self.end_point = event.pos()
        self.update()

    def mouseReleaseEvent(self, event):
        x = event.pos().x()
        y = event.pos().y()
        print(f"release at: ({x}, {y})")
        self.end_point = event.pos()

    def setPixmap(self, pixmap):
        if pixmap.isNull():
            print("Error: Unable to load the image.")
        super().setPixmap(pixmap)
        self.pixmap = True