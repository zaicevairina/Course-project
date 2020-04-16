from PyQt5.QtWidgets import (QLineEdit, QDialog, QDialogButtonBox, QComboBox,
                             QFormLayout, QLabel, QSpinBox, QRadioButton)
from .models import Department, Equipment, Purchase, Supplier, Branch, Project
from .app import Session, window

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
    session = Session()
    ui_elements = [("Адрес", QLineEdit()), ("Закупка", QComboBox())]
    purchases = session.query(Purchase.id, Purchase.item).all()
    purchases = {p[1]: p[0] for p in purchases}
    ui_elements[1][1].addItems(purchases.keys())
    dialog = Dialog(ui_elements, "Добавить запись")
    if dialog.exec() == QDialog.Accepted:
        new_purchase = Branch(address=ui_elements[0][1].text(),
                              purchase_id=purchases[
                                  ui_elements[1][1].currentText()])
        session.add(new_purchase)
        session.commit()
        session.refresh(new_purchase)
        window._view.setText(f"Created new branch with id {new_purchase.id}")


def query_1(self):
    def get_result(X: str) -> str:
        session = Session()
        result = session\
            .query(Department.director)\
            .select_from(Department)\
            .join(Purchase)\
            .filter(Purchase.item == X)
        result_format = "\n".join(
            [str(director[0]) for director in result.all()])
        print(f'\n--> sql query:\n{result}\n\
\n--> result:\n{result_format}\n')
        session.commit()
        return result_format
    ui_elements = [("", QLabel(DESCRIPTION_1)), ("Предметы :", QComboBox())]
    session = Session()
    items = session.query(Purchase.item).all()
    ui_elements[1][1].addItems([item[0] for item in items])
    session.commit()
    dialog = Dialog(ui_elements, "Найти руководителей")
    if dialog.exec() == QDialog.Accepted:
        print(ui_elements[1][1].currentText())
        window._view.setText(get_result(ui_elements[1][1].currentText()))
        print("First query worked")


def query_2(self):
    def get_result(X: str) -> str:
        session = Session()
        project_id = session.query(Project.id).filter(Project.name == X)
        result = session\
            .query(Supplier.detail)\
            .select_from(Supplier)\
            .join(Purchase, Purchase.supplier_id == Supplier.id)\
            .filter(Purchase.project_id == project_id)\
            .order_by(Purchase.amount.asc())
        result_format = "\n".join(
            [str(detail[0]) for detail in result.all()])
        print(f'\n--> sql query:\n{result}\n\
\n--> result:\n{result_format}\n')
        session.commit()
        return result_format
    ui_elements = [("", QLabel(DESCRIPTION_2)),
                   ("Проект", QLineEdit())]
    dialog = Dialog(ui_elements, "Получить реквизиты")
    if dialog.exec() == QDialog.Accepted:
        window._view.setText(get_result(ui_elements[1][1].text()))


def query_3(self):
    def get_result(X: int, Y: str) -> str:
        session = Session()
        result = session.query(Branch.address, Purchase.item, Project.name)\
            .select_from(Branch)\
            .join(Purchase)\
            .join(Project)\
            .join(Equipment)\
            .filter(Project.budget >= X)\
            .filter(Equipment.name.like(f"%{Y}%"))
        result_format = "\n".join(
            [" ".join(tuple_) for tuple_ in result.all()])
        print(f'\n--> sql query:\n{result}\n\
\n--> result:\n{result_format}\n')
        session.commit()
        return result_format
    button_1 = QRadioButton("sub_1")
    button_2 = QRadioButton("sub_2")
    button_3 = QRadioButton("sub_3")
    ui_elements = [("", QLabel(DESCRIPTION_3)),
                   ("Бюджет", QSpinBox()),
                   ("", button_1), ("", button_2), ("", button_3)]
    dialog = Dialog(ui_elements, "Поиск по названию оборудования")
    if dialog.exec() == QDialog.Accepted:
        value: int = ui_elements[1][1].value()
        if (button_1.isChecked()):
            window._view.setText(get_result(value, 'sub_1'))
        if (button_2.isChecked()):
            window._view.setText(get_result(value, 'sub_2'))
        if (button_3.isChecked()):
            window._view.setText(get_result(value, 'sub_3'))
