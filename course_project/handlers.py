from PyQt5.QtWidgets import (QLineEdit, QDialog, QDialogButtonBox, QComboBox,
                             QFormLayout, QLabel, QSpinBox, QRadioButton)
from .models import Department, Equipment, Purchase, Supplier, Branch, Project
from .app import Session

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

#
# def add_to_db(self):
#     ui_elements = [("Адрес", QLineEdit()), ("Закупка", QComboBox())]
#     dialog = Dialog(ui_elements, "Добавить запись")
#     if dialog.exec() == QDialog.Accepted:
#         print("Запись в базу")
#
#
# def query_1(self):
#     def get_result(X: str):
#         session = Session()
#         result = session.query(Department.director).select_from(Department)\
#             .join(Purchase).filter(Purchase.item == X)
#         session.commit()
#
#     ui_elements = [("", QLabel(DESCRIPTION_1)), ("Предметы :", QComboBox())]
#     ui_elements[1][1].addItems(list(map(lambda x:str(x),[1,2,4,'asgr'])))
#     dialog = Dialog(ui_elements, "Найти руководителей")
#
#     if dialog.exec() == QDialog.Accepted:
#         return get_result(ui_elements[1][1].currentText())
#
#
#
# def query_2(self):
#     def get_result(X: int):
#         session = Session()
#         result = session\
#             .query(Supplier.detail)\
#             .select_from(Supplier)\
#             .join(Purchase, Purchase.supplier_id == Supplier.id)\
#             .filter(Purchase.project_id == X)\
#             .order_by(Purchase.amount.asc())
#         print(f'\n--> sql query:\n{result}\n\
# \n--> result:\n{result.all()}\n')
#     get_result(4)
#     ui_elements = [("", QLabel(DESCRIPTION_2)),
#                    ("Проект", QLineEdit())]
#     dialog = Dialog(ui_elements, "Получить реквизиты")
#     if dialog.exec() == QDialog.Accepted:
#         return get_result(ui_elements[1][1].text())
#
#
#
# def query_3(self):
#     def get_result(X: int, Y: str):
#         session = Session()
#         result = session.query(Branch.address, Purchase.item, Project.name)\
#             .select_from(Branch)\
#             .join(Purchase)\
#             .join(Project)\
#             .join(Equipment)\
#             .filter(Project.budget >= X)\
#             .filter(Equipment.name.like(f"%{Y}%"))
#         print(f'\n--> sql query:\n{result}\n\
# \n--> result:\n{result.all()}\n')
#         session.commit()
#     # Example
#     button_1 = QRadioButton("1")
#     button_2 = QRadioButton("2")
#     button_3 = QRadioButton("3")
#     ui_elements = [("", QLabel(DESCRIPTION_3)),
#                    ("Бюджет", QSpinBox()),
#                    ("", button_1), ("", button_2), ("", button_3)]
#     ui_elements[1][1].setMaximum(10 + 1)
#     dialog = Dialog(ui_elements, "Поиск по названию оборудования")
#     if dialog.exec() == QDialog.Accepted:
#         val = ui_elements[1][1].value()
#         if (button_1.isChecked()):
#             return get_result(val, '1')
#             print("Third query worked - 1")
#         if (button_2.isChecked()):
#             return get_result(val, '2')
#         if (button_3.isChecked()):
#             return get_result(val, '3')
#
