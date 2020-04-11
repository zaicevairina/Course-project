from .models import Branch, Department, Project, Purchase, Equipment, Supplier
from random import shuffle


def generate_department(begin: int, end: int):
    return [
        Department(id=i, name=f'department_{i}', director=f'director_{i}')
        for i in range(begin, end)
        ]


def generate_branch(begin: int, end: int):
    return [
        Branch(id=i, address=f'address_{i}')
        for i in range(begin, end)
        ]


def generate_purchase(begin: int, end: int):
    return [
        Purchase(id=i, item=f'item_{i}', amount=i)
        for i in range(begin, end)
        ]


def generate_equipment(begin: int, end: int):
    return [
        Equipment(id=i, name=f'name_{i}')
        for i in range(begin, end)
        ]


def generate_supplier(begin: int, end: int):
    return [
        Supplier(id=i, organization=f'organization_{i}', detail=f'detail_{i}')
        for i in range(begin, end)
        ]


def generate_project(begin: int, end: int):
    return [
        Project(id=i, name=f'name_{i}', budget=i)
        for i in range(begin, end)
        ]


def get_data(begin: int, end: int):
    department = generate_department(begin, end)
    branch = generate_branch(begin, end)
    purchase = generate_purchase(begin, end)
    equipment = generate_equipment(begin, end)
    supplier = generate_supplier(begin, end)
    project = generate_project(begin, end)
    shuffle(department)
    shuffle(branch)
    shuffle(purchase)
    shuffle(equipment)
    shuffle(supplier)
    shuffle(project)
    for i in range(end-begin):
        department[i].purchase = purchase[i].id
        branch[i].purchase = purchase[i].id
        purchase[i].project = project[i].id
        purchase[i].supplier = supplier[i].id
        equipment[i].project = project[i].id
        supplier[i].purchase = purchase[i].id
        project[i].budget = project[i].id
    return [department, branch, purchase, equipment, supplier, project]


__all__ = ['get_data']
