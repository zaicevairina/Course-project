from sqlalchemy import Column,\
    Integer, String, ForeignKey
from .app import Base


class Department(Base):
    __tablename__ = 'department'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    director = Column(String)
    purchase = Column(ForeignKey("purchase.id"))

    def __repr__(self):
        return "<User(name='%s', director='%s', purchase='%s')>" % (
                             self.name, self.director, self.purchase)


class Branch(Base):
    __tablename__ = 'branch'

    id = Column(Integer, primary_key=True)
    address = Column(String)
    purchase = Column(ForeignKey("purchase.id"))

    def __repr__(self):
        return "<User(address='%s', purchase='%s')>" % (
                             self.address, self.purchase)


class Purchase(Base):
    __tablename__ = 'purchase'

    id = Column(Integer, primary_key=True)
    item = Column(String)
    amount = Column(Integer)
    supplier = Column(ForeignKey("supplier.id"))
    project = Column(ForeignKey("project.id"))

    def __repr__(self):
        return "<User(item='%s', amount='%s', supplier='%s', project='%s')>"\
             % (self.item, self.amount, self.supplier, self.project)


class Equipment(Base):
    __tablename__ = 'equipment'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    project = Column(ForeignKey("project.id"))

    def __repr__(self):
        return "<User(name='%s', fullname='%s', nickname='%s')>" % (
                             self.name, self.fullname, self.nickname)


class Supplier(Base):
    __tablename__ = 'supplier'

    id = Column(Integer, primary_key=True)
    organization = Column(String)
    detail = Column(String)
    purchase = Column(ForeignKey("purchase.id"))

    def __repr__(self):
        return "<User(organization='%s', detail='%s', purchase='%s')>" % (
                             self.organization, self.detail, self.purchase)


class Project(Base):
    __tablename__ = 'project'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    budget = Column(String)

    def __repr__(self):
        return "<User(name='%s', budget='%s')>" % (
                             self.name, self.budget)
