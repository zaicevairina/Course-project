from .models import Branch, Department, Project, Purchase, Equipment, Supplier

'''
До занесения в базу id == None, поэтому ручками
Может стоило использовать refresh
'''


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
        Equipment(id=i, name=f'equipment_{i}')
        for i in range(begin, end)
        ]


def generate_supplier(begin: int, end: int):
    return [
        Supplier(id=i, organization=f'organization_{i}', detail=f'detail_{i}')
        for i in range(begin, end)
        ]


def generate_project(begin: int, end: int):
    return [
        Project(id=i, name=f'project_{i}', budget=i*i)
        for i in range(begin, end)
        ]


def get_data(begin: int, end: int):
    department = generate_department(begin, end)
    branch = generate_branch(begin, end)
    purchase = generate_purchase(begin, end)
    equipment = generate_equipment(begin, end)
    supplier = generate_supplier(begin, end)
    project = generate_project(begin, end)
    # from random import shuffle
    # shuffle(department)
    # shuffle(branch)
    # shuffle(purchase)
    # shuffle(equipment)
    # shuffle(supplier)
    # shuffle(project)
    for i in range(end-begin):
        department[i].purchase_id = purchase[i].id
        branch[i].purchase_id = purchase[i].id
        purchase[i].project_id = project[i].id
        purchase[i].supplier_id = supplier[i].id
        equipment[i].project_id = project[i].id
        supplier[i].purchase_id = purchase[i].id
    # для второй
    purchase[0].project_id = begin + 1
    purchase[1].project_id = begin + 1
    purchase[2].project_id = begin + 1
    # для третьей
    equipment[0].name += 'sub_1'
    equipment[1].name += 'sub_1'
    equipment[2].name += 'sub_1'
    equipment[3].name += 'sub_2'
    equipment[4].name += 'sub_2'
    equipment[5].name += 'sub_2'
    equipment[6].name += 'sub_3'
    equipment[7].name += 'sub_3'
    equipment[8].name += 'sub_3'
    return [department, branch, purchase, equipment, supplier, project]


__all__ = ['get_data']
