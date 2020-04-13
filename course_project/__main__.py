from app import app
import sys
from gui import MainWindow

if __name__ == "__main__":
    window = MainWindow()
    # создание таблицы
    # Base.metadata.create_all(engine)
    # добавляем данные в бд
    # more_data(session)
    window.init_ui()
    window.show()
    sys.exit(app.exec_())
