import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget
from PyQt5.QtGui import QPixmap, QPainter, QColor
from PyQt5.QtCore import Qt


class ImageClickRecorder(QWidget):
    def __init__(self, image):
        super().__init__()

        self.image_path = image
        self.image_label = QLabel(self)
        self.image_pixmap = QPixmap(image)
        self.image_label.setPixmap(self.image_pixmap)
        self.image_label.mousePressEvent = self.get_click_pos
        self.image_label.mouseReleaseEvent = self.get_release_pos

        self.clicked_positions = []
        self.released_positions = []

        self.init_ui()

    def init_ui(self):
        self.setGeometry(100, 100, self.image_pixmap.width(), self.image_pixmap.height())
        self.setWindowTitle('Image Click and Release Recorder')
        self.show()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QColor(Qt.red))

        for pos in self.clicked_positions:
            painter.drawPoint(*pos)

    def get_click_pos(self, event):
        x = event.pos().x()
        y = event.pos().y()
        self.clicked_positions.append((x, y))
        print(f"Clicked at: ({x}, {y})")

    def get_release_pos(self, event):
        x = event.pos().x()
        y = event.pos().y()
        self.released_positions.append((x, y))
        print(f"Released at: ({x}, {y})")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    image_path = r"C:\Users\zhiji\Documents\company\CompanyI\Images\Invoice_000000000664731.jpg"
    window = ImageClickRecorder(image_path)
    sys.exit(app.exec_())