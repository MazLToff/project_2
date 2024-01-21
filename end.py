import sys
from PyQt6.QtWidgets import QWidget, QPushButton, QApplication
import subprocess


class StartWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Экран смерти')
        self.setGeometry(100, 100, 1200, 600)
        # self.setWindowIcon()

        self.reset_button = QPushButton('Начать сначала', self)
        self.reset_button.move(50, 50)
        self.home_button = QPushButton('В главное меню', self)
        self.home_button.move(0, 00)

        self.reset_button.clicked.connect(self.game)
        self.home_button.clicked.connect(self.home)

    def home(self):
        path = 'start.py'
        self.close()
        subprocess.call(['python', path])

    def game(self):
        path = 'game.py'
        self.close()
        subprocess.call(['python', path])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = StartWindow()
    window.show()
    sys.exit(app.exec())
