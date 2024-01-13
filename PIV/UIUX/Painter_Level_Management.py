import sys
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QLabel, QTabWidget
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt, QRect, QSize, QPoint


class Painter(QLabel):
    def __init__(self):
        super().__init__()
        self.isDrawing = False
        self.start_point = None
        self.end_point = None
        self.current_size = [self.size().height(), self.size().width()]

    def draw(self):
        painter = QPainter(self)
        painter.setPen(QColor(0, 0, 255))  # Blue color for the rectangle outline
        # Calculate the rectangle coordinates using start and end points
        rect = QRect(self.start_point, self.end_point)
        # Draw the rectangle
        painter.drawRect(rect)

    def paintEvent(self, event):
        super().paintEvent(event)
        if self.start_point is not None and self.end_point is not None:
            self.draw()

    def mousePressEvent(self, event):
        if self.isDrawing:
            #print("wid:"+self.width(), " hei: "+self.height())
            x = event.pos().x()
            y = event.pos().y()
            print(f"Clicked at: ({x}, {y})")
            self.start_point = event.pos()

    def mouseMoveEvent(self, event):
        if self.isDrawing:
            self.end_point = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):
        if self.isDrawing:
            x = event.pos().x()
            y = event.pos().y()
            print(f"release at: ({x}, {y})")
            self.end_point = event.pos()
            self.setDrawing(False)

    def setPixmap(self, pixmap):
        if pixmap.isNull():
            print("Error: Unable to load the image.")
        super().setPixmap(pixmap)

    def setDrawing(self, is_drawing):
        self.isDrawing = is_drawing

    def resizeEvent(self, event):

        super().resizeEvent(event)
        old_size = [self.current_size[0], self.current_size[1]]
        self.current_size[0] = event.size().height()
        self.current_size[1] = event.size().width()
        print("height: ",old_size[0], "width: ",old_size[1])

        if self.start_point is not None:
            print(f"start point x: {self.start_point.x()}, start poit y: {self.start_point.y()}\nend point x: {self.end_point.x()}, end poit y: {self.end_point.y()}")
            ratio = [self.current_size[0] / old_size[0], self.current_size[1] / old_size[1]]
            self.start_point = QPoint(int(self.start_point.x()*ratio[1]), int(self.start_point.y()*ratio[0]))
            self.end_point = QPoint(int(self.end_point.x()*ratio[1]), int(self.end_point.y()*ratio[0]))
            self.draw()