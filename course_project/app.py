import sys
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from PyQt5.QtWidgets import QApplication
from .gui import MainWindow


Base = declarative_base()
engine = create_engine('sqlite:///db/whatever.db', echo=False)
app = QApplication(sys.argv)
window = MainWindow()
