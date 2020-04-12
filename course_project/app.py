import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from PyQt5.QtWidgets import QApplication


engine = create_engine('sqlite:///db/whatever.db', echo=False)
Session = sessionmaker(bind=engine)
session = Session()
app = QApplication(sys.argv)
