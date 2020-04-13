from peewee import *
from models import Department, Branch, Project, Supplier, Purchase, Equipment


def get_purchases():
	res = ['{} {}'.format(i, i.good) for i in Purchase.select()]
	return res

def add_branch(address, purchase):
	get_purchase = Purchase.select().where(Purchase.id == purchase.split(' ')[0]).first()
	branch = Branch.create(address=address)
	Purchase.create(good=get_purchase.good,amount=get_purchase.amount, supplier=get_purchase.supplier, project=get_purchase.project, department=get_purchase.department, branch=branch)
	return get_purchase.good

def get_goods():
	res = [i.good for i in Purchase.select()]
	return set(res)

def query1(X):
	res = [i.director for i in Department.select().join(Purchase).where(Purchase.good==X)]
	return '\n'.join(res)

def query2(X):
	res = [str(i.requisites) for i in Supplier.select().join(Purchase).join(Project).where(Project.title==X).group_by(Purchase.supplier).order_by(fn.SUM(Purchase.amount))]
	return '\n'.join(res)

def max_budget():
	return Project.select(fn.MAX(Project.budget)).scalar()

def query3(X,Y):
	X =int(X)
	res = ['-'.join(i) for i in (Branch.select(Branch.address, Purchase.good, Project.title,Equipment.name).join(Purchase).join(Project).join(Equipment).where(Project.budget>=X, Equipment.name.contains(Y))).tuples()]
	return '\n'.join(set(res))

