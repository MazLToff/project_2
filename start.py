import sys
from PyQt6.QtWidgets import QWidget, QPushButton, QApplication
import subprocess


class StartWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Главное меню')
        self.setGeometry(100, 100, 1200, 600)
        # self.setWindowIcon()

        self.start_button = QPushButton('Начать', self)
        self.start_button.clicked.connect(self.runner)

    def runner(self):
        path = 'game.py'
        self.close()
        subprocess.call(['python', path])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = StartWindow()
    window.show()
    sys.exit(app.exec())
