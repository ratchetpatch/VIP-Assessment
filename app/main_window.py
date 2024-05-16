from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("app/ui/main_window.ui", self)
        self.initUI()

    def initUI(self):
        # Initialize your UI elements here
        pass
