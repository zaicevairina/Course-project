from .app import engine, app, session, window
from .models import Base, Branch
from .data_generator import get_data
from .handlers import query_1, query_2, query_3, add_to_db
import sys
from sqlalchemy import func


def more_data(session):
    begin_id = session.query(func.max(Branch.id)).scalar()
    if not begin_id:
        begin_id = 0
    for tuples in get_data(begin_id + 1, begin_id + 10):
        session.add_all(tuples)
    session.commit()


if __name__ == "__main__":
    Base.metadata.create_all(engine)
    more_data(session)
    window.init_ui(query_1, query_2, query_3, add_to_db)
    window.show()
    sys.exit(app.exec_())
