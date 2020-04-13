from PyQt5.QtWidgets import (QLineEdit, QDialog, QDialogButtonBox, QComboBox,
                             QFormLayout, QLabel, QSpinBox, QRadioButton)
# from app import Session

DESCRIPTION_1 = "Руководители отделов, закупивших предмет типа Х"
DESCRIPTION_2 = "Реквизиты поставщиков, поставляющих предметы для проекта X,\n\
отсортированные по кол-ву предметов в закупке"
DESCRIPTION_3 = "Адреса филиалов, виды предметов и названия проектов с бюджетом не менее Х,\n\
для которых поставляется оборудование, название которго содержит подстроку Y"


class Dialog(QDialog):
    # Класс QDialog является базовым классом для диалоговых окон
    def __init__(self, ui_elements: list, title="title"):
        # Класс QFormLayout управляет формами виджетов ввода и связанных с ними меток.
        # QFormLayout является вспомогательным классом компоновки, который размещает свои дочерние элементы в двух столбцах
        layout = QFormLayout()
        super().__init__()
        # установка заголовка
        super().setWindowTitle(title)
        # установка компановщика
        super().setLayout(layout)
        #добавление эдементов название-объект
        for elem_1, elem_2 in ui_elements:
            layout.addRow(QLabel(elem_1), elem_2)
        # объявление кнопок ок и закрыть
        self.buttons = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        #     добавдние кнопок ок и закрыть
        layout.addRow(self.buttons)
        # событие ок
        self.buttons.accepted.connect(self.accept)
        # событие отмена
        self.buttons.rejected.connect(self.reject)
