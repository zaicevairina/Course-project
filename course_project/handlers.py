from PyQt5.QtWidgets import (QLineEdit, QDialog, QDialogButtonBox, QComboBox,
                             QFormLayout, QLabel, QSpinBox, QRadioButton)


DESCRIPTION_1 = "Руководители отделов, закупивших предмет типа Х"
DESCRIPTION_2 = "Реквизиты поставщиков, поставляющих предметы для проекта X,\n\
отсортированные по кол-ву предметов в закупке"
DESCRIPTION_3 = "Адреса филиалов, виды предметов и названия проектов с бюджетом не менее Х,\n\
для которых поставляется оборудование, название которго содержит подстроку Y"


class Dialog(QDialog):

    def __init__(self, ui_elements: list, title="title"):
        layout = QFormLayout()
        super().__init__()
        super().setWindowTitle(title)
        super().setLayout(layout)
        for elem_1, elem_2 in ui_elements:
            layout.addRow(QLabel(elem_1), elem_2)
        self.buttons = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        layout.addRow(self.buttons)
        self.buttons.accepted.connect(self.accept)
        self.buttons.rejected.connect(self.reject)


def add_to_db(self):
    ui_elements = [("Адрес", QLineEdit()), ("Закупка", QComboBox())]
    dialog = Dialog(ui_elements, "Добавить запись")
    if dialog.exec() == QDialog.Accepted:
        print("Запись в базу")


def query_1(self):
    ui_elements = [("", QLabel(DESCRIPTION_1)), ("Предметы :", QComboBox())]
    dialog = Dialog(ui_elements, "Найти руководителей")
    if dialog.exec() == QDialog.Accepted:
        print("First query worked")


def query_2(self):
    ui_elements = [("", QLabel(DESCRIPTION_2)),
                   ("Проект", QLineEdit())]
    dialog = Dialog(ui_elements, "Получить реквизиты")
    if dialog.exec() == QDialog.Accepted:
        print("Second query worked" + ui_elements[1][1].text())


def query_3(self):
    button_1 = QRadioButton("Подстрока 1")
    button_2 = QRadioButton("Подстрока 2")
    button_3 = QRadioButton("Подстрока 3")
    ui_elements = [("", QLabel(DESCRIPTION_3)),
                   ("Бюджет", QSpinBox()),
                   ("", button_1), ("", button_2), ("", button_3)]
    dialog = Dialog(ui_elements, "Поиск по названию оборудования")
    if dialog.exec() == QDialog.Accepted:
        if (button_1.isChecked()):
            print("Third query worked - 1")
        if (button_2.isChecked()):
            print("Third query worked - 2")
        if (button_3.isChecked()):
            print("Third query worked - 3")