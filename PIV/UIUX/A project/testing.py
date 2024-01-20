from PyQt5.QtWidgets import QLabel, QApplication
from PyQt5.QtCore import QSize

class Painter(QLabel):
    # ... (other methods)

    def resizeEvent(self, event):
        old_size = event.oldSize()
        new_size = event.size()

        print(f"Old Size: {old_size.width()}, {old_size.height()}")
        print(f"New Size: {new_size.width()}, {new_size.height()}")

        # Update the rectangle coordinates based on the new size of the widget
        if self.isDrawing:
            self.start_percent *= QSize(self.width() / old_size.width(), self.height() / old_size.height())
            self.end_percent *= QSize(self.width() / old_size.width(), self.height() / old_size.height())

if __name__ == '__main__':
    app = QApplication([])
    painter = Painter()
    painter.resize(400, 300)
    painter.show()
    app.exec_()
