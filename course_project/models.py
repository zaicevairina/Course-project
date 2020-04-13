from sqlalchemy import Column,\
    Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

# от него наследуются отсальные orm классы
Base = declarative_base()


class Department(Base):
    __tablename__ = 'department'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    director = Column(String)
    # purchase_id = relationship("Purchase")
    purchase_id = Column(ForeignKey("purchase.id"))

    def __repr__(self):
        return "<User(name='%s', director='%s', purchase='%s')>" % (
                             self.name, self.director, self.purchase)


class Branch(Base):
    __tablename__ = 'branch'

    id = Column(Integer, primary_key=True)
    address = Column(String)
    purchase_id = Column(ForeignKey("purchase.id"))

    def __repr__(self):
        return "<User(address='%s', purchase='%s')>" % (
                             self.address, self.purchase_id)


class Purchase(Base):
    __tablename__ = 'purchase'

    id = Column(Integer, primary_key=True)
    item = Column(String)
    amount = Column(Integer)
    # department = Column(ForeignKey("Department.Purchase"))
    supplier_id = Column(ForeignKey("supplier.id"))
    project_id = Column(ForeignKey("project.id"))

    def __repr__(self):
        return "<User(item='%s', amount='%s', supplier='%s', project='%s')>"\
             % (self.item, self.amount, self.supplier_id, self.project_id)


class Equipment(Base):
    __tablename__ = 'equipment'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    project_id = Column(ForeignKey("project.id"))

    def __repr__(self):
        return "<User(name='%s', project_id='%s')>" % (
                             self.name, self.project_id)


class Supplier(Base):
    __tablename__ = 'supplier'

    id = Column(Integer, primary_key=True)
    organization = Column(String)
    detail = Column(String)
    purchase_id = Column(ForeignKey("purchase.id"))

    def __repr__(self):
        return "<User(organization='%s', detail='%s', purchase='%s')>" % (
                             self.organization, self.detail, self.purchase_id)


class Project(Base):
    __tablename__ = 'project'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    budget = Column(Integer)

    def __repr__(self):
        return "<User(name='%s', budget='%s')>" % (
                             self.name, self.budget)
