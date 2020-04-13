from PyQt5.QtWidgets import (QMainWindow, QWidget, QPushButton,
                             QTableView, QVBoxLayout, QHBoxLayout)
from PyQt5.QtCore import QCoreApplication
from .handlers import Dialog
from PyQt5.QtWidgets import (QLineEdit, QDialog, QDialogButtonBox, QComboBox,
                             QFormLayout, QLabel, QSpinBox, QRadioButton,QTextBrowser)

from .models import Department, Equipment, Purchase, Supplier, Branch, Project
from .app import Session

DESCRIPTION_1 = "Руководители отделов, закупивших предмет типа Х"
DESCRIPTION_2 = "Реквизиты поставщиков, поставляющих предметы для проекта X,\n\
отсортированные по кол-ву предметов в закупке"
DESCRIPTION_3 = "Адреса филиалов, виды предметов и названия проектов с бюджетом не менее Х,\n\
для которых поставляется оборудование, название которго содержит подстроку Y"


class MainWindow(QMainWindow):

    def __init__(self):
        # MainWindow главное окно приложения
        super().__init__()
        # окно для вывода
        # self._view = QTableView()
        self._view = QTextBrowser()
        # инициализация кнопок
        self._buttonAdd = QPushButton("Добавить")
        self._quit = QPushButton('Закончить')
        self._buttons = [(QPushButton("Первый запрос"), self.query_1),
                         (QPushButton("Второй запрос"), self.query_2),
                         (QPushButton("Третий запрос"), self.query_3)]

    def init_ui(self):
        # Класс QWidget является базовым для всех объектов пользовательского интерфейса.
        # Виджет - это элементарный объект пользовательского интерфейса:
        # он получает события мыши, клавиатуры и другие события от оконной системы и рисует свое изображение на экране.
        widget = QWidget()
        # Класс QVBoxLayout Выстраивает виджеты в вертикальную линию.
        main_layout = QVBoxLayout()
        # Класс QHBoxLayout выстраивает виджеты в горизонтальную линию.
        tmp_layout = QHBoxLayout()
        # соединение кнопки и функции
        self._buttonAdd.clicked.connect(self.add_to_db)
        # соединение кнокпи "Закончить" c сигналом выхода
        self._quit.clicked.connect(QCoreApplication.instance().quit)
        # соединение копок для запросов с функциями запросов
        for button, handler in self._buttons:
            button.clicked.connect(handler)
        # размер окна
        self.setGeometry(400, 400, 300, 300)
        # название окна
        self.setWindowTitle('Наш курсовой проект')
        # установка в главном оне вертикаольного лейата
        widget.setLayout(main_layout)
        # Устанавливает заданный виджет (widget), в качестве центрального виджета главного окна.
        self.setCentralWidget(widget)
        # Добавляет переданный виджет widget  в лейоут(вертикальный-главный)
        main_layout.addWidget(self._view)
        # добавление в виджет гориз лейаута
        main_layout.addLayout(tmp_layout)
        # добавление в гориз виджет кнопок
        tmp_layout.addWidget(self._buttonAdd)
        for button, _ in self._buttons:
            tmp_layout.addWidget(button)
        tmp_layout.addWidget(self._quit)

    def setModel(self, model):
        if model is None:
            return
        self._view.setModel(model)

    def add_to_db(self):
        ui_elements = [("Адрес", QLineEdit()), ("Закупка", QComboBox())]
        dialog = Dialog(ui_elements, "Добавить запись")
        if dialog.exec() == QDialog.Accepted:
            print("Запись в базу")

    def query_1(self):
        def get_result(X: str):
            session = Session()
            result = session.query(Department.director).select_from(Department) \
                .join(Purchase).filter(Purchase.item == X)
            session.commit()

        ui_elements = [("", QLabel(DESCRIPTION_1)), ("Предметы :", QComboBox())]
        ui_elements[1][1].addItems(list(map(lambda x: str(x), [1, 2, 4, 'asgr'])))
        dialog = Dialog(ui_elements, "Найти руководителей")

        if dialog.exec() == QDialog.Accepted:
            self._view.setText('123')
            import time
            # time.sleep(100)
            # self.setModel(get_result(ui_elements[1][1].currentText()))

    def query_2(self):
        def get_result(X: int):
            session = Session()
            result = session \
                .query(Supplier.detail) \
                .select_from(Supplier) \
                .join(Purchase, Purchase.supplier_id == Supplier.id) \
                .filter(Purchase.project_id == X) \
                .order_by(Purchase.amount.asc())
            print(f'\n--> sql query:\n{result}\n\
    \n--> result:\n{result.all()}\n')

        get_result(4)
        ui_elements = [("", QLabel(DESCRIPTION_2)),
                       ("Проект", QLineEdit())]
        dialog = Dialog(ui_elements, "Получить реквизиты")
        if dialog.exec() == QDialog.Accepted:
            self.setModel(get_result(ui_elements[1][1].text()))


    def query_3(self):
        def get_result(X: int, Y: str):
            session = Session()
            result = session.query(Branch.address, Purchase.item, Project.name) \
                .select_from(Branch) \
                .join(Purchase) \
                .join(Project) \
                .join(Equipment) \
                .filter(Project.budget >= X) \
                .filter(Equipment.name.like(f"%{Y}%"))
            print(f'\n--> sql query:\n{result}\n\
    \n--> result:\n{result.all()}\n')
            session.commit()

        # Example
        button_1 = QRadioButton("1")
        button_2 = QRadioButton("2")
        button_3 = QRadioButton("3")
        ui_elements = [("", QLabel(DESCRIPTION_3)),
                       ("Бюджет", QSpinBox()),
                       ("", button_1), ("", button_2), ("", button_3)]
        ui_elements[1][1].setMaximum(10 + 1)
        dialog = Dialog(ui_elements, "Поиск по названию оборудования")
        if dialog.exec() == QDialog.Accepted:
            val = ui_elements[1][1].value()
            if (button_1.isChecked()):
                self.setModel(get_result(val, '1'))
            if (button_2.isChecked()):
                self.setModel(get_result(val, '2'))
            if (button_3.isChecked()):
                self.setModel(get_result(val, '3'))

