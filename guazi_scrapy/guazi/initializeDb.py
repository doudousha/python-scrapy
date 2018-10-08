from pymysql import OperationalError
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+pymysql://guazi:Cp54w6wPhmyxF27s@45.78.9.17:3306/guazi')
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()


def initialize_db():
    from guazi.models.guaZiDetail import GuaZiDetail
    try:
        GuaZiDetail.metadata.create_all(engine)

    except OperationalError:
        print(OperationalError)


initialize_db()
