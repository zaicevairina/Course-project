from peewee import *
from datetime import date, time

db = SqliteDatabase('app.db')

class BaseModel(Model):
    class Meta:
        database = db

class Department(BaseModel):
    title = CharField(default='Smt')
    director = CharField(default='John')

class Branch(BaseModel):
	address = CharField()

class Supplier(BaseModel):
	organization = CharField()
	requisites = IntegerField()

class Project(BaseModel):
	title = CharField()
	budget = IntegerField()

class Purchase(BaseModel):
	good = CharField()
	amount = IntegerField()
	department = ForeignKeyField(Department, backref='purchases')
	branch = ForeignKeyField(Branch, backref='purchases')
	project = ForeignKeyField(Project, backref='purchases')
	supplier = ForeignKeyField(Supplier, backref='purchases')

class Equipment(BaseModel):
	name = CharField()
	project = ForeignKeyField(Project, backref='equipments')


# class ViewerToSession(BaseModel):
#     viewer = ForeignKeyField(Viewer, backref='viewer_sessions')
#     session = ForeignKeyField(Session, backref='session_viewers')

#     class Meta:
#         primary_key = CompositeKey('viewer', 'session')


if __name__ == '__main__':
	Department.create_table()
	Branch.create_table()
	Supplier.create_table()
	Project.create_table()
	Purchase.create_table()
	Equipment.create_table()

		

