from .app import engine, window, app
from .models import Base
import sys


if __name__ == "__main__":
    Base.metadata.create_all(engine)
    window.init_ui()
    window.show()
    sys.exit(app.exec_())
