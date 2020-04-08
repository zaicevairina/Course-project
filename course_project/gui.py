from PyQt5.QtWidgets import (QMainWindow, QWidget, QPushButton,
                             QTableView, QVBoxLayout, QHBoxLayout)
from PyQt5.QtCore import QCoreApplication
from .handlers import query_1, query_2, query_3, add_to_db


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self._view = QTableView()
        self._buttonAdd = QPushButton("Добавить")
        self._quit = QPushButton('Закончить')
        self._buttons = [(QPushButton("Первый запрос"), query_1),
                         (QPushButton("Второй запрос"), query_2),
                         (QPushButton("Третий запрос"), query_3)]

    def init_ui(self):
        widget = QWidget()
        main_layout = QVBoxLayout()
        tmp_layout = QHBoxLayout()
        self._buttonAdd.clicked.connect(add_to_db)
        self._quit.clicked.connect(QCoreApplication.instance().quit)
        for button, handler in self._buttons:
            button.clicked.connect(handler)
        self.setGeometry(400, 400, 300, 300)
        self.setWindowTitle('Наш курсовой проект')
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)
        main_layout.addWidget(self._view)
        main_layout.addLayout(tmp_layout)
        tmp_layout.addWidget(self._buttonAdd)
        for button, _ in self._buttons:
            tmp_layout.addWidget(button)
        tmp_layout.addWidget(self._quit)
