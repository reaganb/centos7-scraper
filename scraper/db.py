from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.schema import CreateSchema
from sqlalchemy import Column, String, Integer, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import OperationalError
import os.path as op
import configparser


Base = declarative_base(metadata=MetaData(schema='scraper'))


class File(Base):

    __tablename__ = 'file'

    id = Column(Integer, primary_key=True)
    file_name = Column(String(255))
    download_link = Column(String(255), unique=True)
    file_size = Column(String(255))

    def __init__(self, file_name, download_link, file_size):
        self.file_name = file_name
        self.download_link = download_link
        self.file_size = file_size


def init_database(db_cred):
    """
    A function for initializing the database engine

    Argument:
        db_cred -- the hostname, username, password credentials

    return -- the db engine
    """

    config = config_parser(file='../data/config_db.ini')
    db_engine = config['args']['DB_ENGINE']
    db_port = config['args']['DB_PORT']
    db_name = config['args']['DB_NAME']
    db_schema = config['args']['DB_SCHEMA']
    db_user = db_cred['user']
    db_password = db_cred['password']
    db_host = db_cred['host']

    try:
        url = f'{db_engine}://{db_user}:{db_password}@{db_host}:{db_port}'

        if not database_exists(f'{url}/{db_name}'):
            create_database(f"{url}/{db_name}")
            engine = create_engine(f"{url}/{db_name}")
        else:
            engine = create_engine(f"{url}/{db_name}")

        conn = engine.connect()
        if not conn.dialect.has_schema(conn, schema='scraper'):
            engine.execute(CreateSchema(db_schema))
        conn.close()

        return engine

    except OperationalError:
        return None


def config_parser(file):
    """
    Function for reading configuration files using the configparser module

    Argument:
        file -- the relative config file path

    return -- the ConfigParser object or None
    """

    config_file = op.join(op.dirname(op.abspath(__file__)), file)
    if op.isfile(config_file):
        config = configparser.ConfigParser()
        config.read(config_file)
        return config
    else:
        return None
