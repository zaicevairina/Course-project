from .app import engine, window, app, session
from .models import Base, Department
from .data_generator import get_data
import sys
from sqlalchemy import func


def more_data(session):
    begin_id = session.query(func.max(Department.id)).scalar()
    if not begin_id:
        begin_id = 0
    for tuples in get_data(begin_id + 1, begin_id + 10):
        session.add_all(tuples)
    session.commit()


if __name__ == "__main__":
    Base.metadata.create_all(engine)
    more_data(session)
    window.init_ui()
    window.show()
    sys.exit(app.exec_())
