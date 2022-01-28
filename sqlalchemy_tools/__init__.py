import os
from dotenv import load_dotenv
import pathlib
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def get_sqlalchemy_url(prefix):
    """ build database url from env file """
    DB_TYPE = os.environ.get(prefix+'_DB_TYPE')
    DB_USERNAME = os.environ.get(prefix+'_DB_USERNAME')
    DB_PASS = os.environ.get(prefix+'_DB_PASSWORD')
    DB_NAME = os.environ.get(prefix+'_DB_NAME')
    DB_PORT = os.environ.get(prefix+'_DB_PORT')
    DB_HOST = os.environ.get(prefix+'_DB_HOST')
    sqlalchemy_url = DB_TYPE+"://"+DB_USERNAME+":"+DB_PASS+"@"+DB_HOST+":"+DB_PORT+"/"+DB_NAME
    return sqlalchemy_url

def get_sqlalchemy_session(env_file=".env", prefix="TEST"):
    '''
    connect to database and create sqlalchemy session.
    env_file: path to env file where database URL and credentials are stored
    prefix: string appended to database variable names. ex: PREFIX_DB_PASSWORD
    '''    
    dotenv = load_dotenv(env_file)
    sqlalchemy_url = get_sqlalchemy_url(prefix)
    engine = create_engine(sqlalchemy_url)
    engine.connect()
    Session = sessionmaker(engine)
    return Session()

def get_base(env_file=".env", prefix="TEST"):
    """ get model base, so that the model mappings of the orm can be used in other"""
    dotenv = load_dotenv(env_file)
    sqlalchemy_url = get_sqlalchemy_url(prefix)
    Base = automap_base()
    engine = sqlalchemy.create_engine(sqlalchemy_url)
    Base.prepare(engine, reflect=True)
    return Base
    

if __name__ == "__main__":
    session = get_sqlalchemy_session()
    base = get_base()
    print(session)
    print(base)
    