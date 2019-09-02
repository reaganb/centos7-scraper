from sqlalchemy import Column, String, Integer, Date, MetaData
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.schema import CreateSchema


Base = declarative_base(metadata=MetaData(schema='scraper'))

class File(Base):
    __tablename__ = 'file'

    id = Column(Integer, primary_key=True)
    file_name = Column(String)
    download_link = Column(String)
    file_size = Column(String)

    def __init__(self, file_name, download_link, file_size):
        self.file_name = file_name
        self.download_link = download_link
        self.file_size = file_size

# def init_database(db_engine, db_user, db_password, db_host, db_port, db_name, db_schema):
def init_database():
    DB_ENGINE = 'postgresql+psycopg2'
    DB_USER = 'postgres'
    DB_PASSWORD = 'nopassword'
    DB_HOST = 'localhost'
    DB_PORT = '5432'
    DB_NAME = 'scraper_db'
    DB_SCHEMA = 'scraper'

    url = f'{DB_ENGINE}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}'

    if not database_exists(f'{url}/{DB_NAME}'):
        create_database(f"{url}/{DB_NAME}")
        engine = create_engine(f"{url}/{DB_NAME}")
    else:
        engine = create_engine(f"{url}/{DB_NAME}")

    conn = engine.connect()
    if not conn.dialect.has_schema(conn, schema='scraper'):
        engine.execute(CreateSchema(DB_SCHEMA))
    conn.close()

    return engine

    # Session = sessionmaker(bind=engine)




# if __name__ == '__main__':
#     # 2 - generate database schema
#     Base.metadata.create_all(engine)
#
#     # 3 - create a new session
#     session = Session()
#     matt_damon = Actor("Matt Damon", date(1970, 10, 8))
#     matt_damon1 = Actor("Matt Damon1", date(1970, 10, 8))
#     matt_damon2 = Actor("Matt Damon2", date(1970, 10, 8))
#
#     session.add(matt_damon)
#     session.add(matt_damon1)
#     session.add(matt_damon2)
#
#     actors = session.query(Actor).all()
#
#     # 4 - print movies' details
#     print('\n### All Actors:')
#     for actor in actors:
#         print(f'{actor.id} {actor.name} and {actor.birthday}')
#     print('')
#
#     session.commit()
#     session.close()
