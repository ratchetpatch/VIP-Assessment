from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi
from .database import Database


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("app/ui/main_window.ui", self)
        self.database = Database("data/app.db")
        self.database.initialize_database()
        self.initUI()

    def initUI(self):
        self.load_data()

    def load_data(self):
        query = "SELECT * FROM your_table"
        results = self.database.execute_read_query(query)
        for row in results:
            print(row)
