import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv()

Base = declarative_base()


class Database:
    def __init__(self):
        # Construct the connection string for SQLAlchemy
        connection_string = f'postgresql://{os.getenv("PGUSER")}:{os.getenv("PGPASSWORD")}@{os.getenv("PGHOST")}:5432/{os.getenv("PGDATABASE")}'
        # Create the SQLAlchemy engine
        self.engine = create_engine(connection_string)
        # Create a session maker
        self.Session = sessionmaker(bind=self.engine)

    def create_session(self):
        return self.Session()

    def create(self, obj):
        session = self.create_session()
        try:
            session.add(obj)
            session.commit()
        except Exception as e:
            session.rollback()
            return e
        finally:
            session.close()

    def read(self, cls, id=None):
        session = self.create_session()
        if id is None:
            try:
                obj = session.query(cls).all()
                return obj
            except Exception as e:
                return e
            finally:
                session.close()
        try:
            obj = session.query(cls).get(id)
            return obj
        except Exception as e:
            return e
        finally:
            session.close()

    def update(self, obj):
        session = self.create_session()
        try:
            session.merge(obj)
            session.commit()
        except Exception as e:
            session.rollback()
            return e
        finally:
            session.close()

    def delete(self, obj):
        session = self.create_session()
        try:
            session.delete(obj)
            session.commit()
        except Exception as e:
            session.rollback()
            return e
        finally:
            session.close()

    def join(self, *tables, conditions):
        session = self.create_session()
        try:
            query = session.query(*tables).filter(conditions)
            result = query.all()
            return result
        except Exception as e:
            return e
        finally:
            session.close()
