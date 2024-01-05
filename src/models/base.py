from dotenv import load_dotenv
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine
import os

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float

load_dotenv(r'.env')

engine = create_engine(os.environ['DATABASE_URL'])
session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))


Base = declarative_base()

class Datasets(Base):
    __tablename__ = "Datasets"
    id = Column(Integer, primary_key=True)
    dataset = Column(Integer, nullable=False)
    name = Column(String(30))
    well = Column(Integer, ForeignKey("Wells.well"))


class Wells(Base):
    __tablename__ = "Wells"
    well = Column(Integer, primary_key=True)
    name = Column(String(30))
    # field = Column(Integer, ForeignKey("Fields.field_id"))


class Samples(Base):
    __tablename__ = "Samples"
    sample = Column(Integer, primary_key=True)
    name = Column(String(30))
    well = Column(Integer, ForeignKey("Wells.well"))
    md = Column(Integer)


class Experiments(Base):
    __tablename__ = "Experiments"
    experiment = Column(Integer, primary_key=True)
    sample = Column(Integer, ForeignKey("Samples.sample"))
    name = Column(String(30))
    type = Column(Integer, ForeignKey("Dict.id"))
    date = Column(DateTime(timezone=True))


class Properties(Base):
    __tablename__ = "Properties"
    id = Column(Integer, primary_key=True)
    experiment = Column(Integer, ForeignKey("Experiments.experiment"))
    property = Column(Integer, ForeignKey("Dict.id"))
    value = Column(Float)


class Dict(Base):
    __tablename__ = "Dict"
    id = Column(Integer, primary_key=True)
    group = Column(Integer)
    name = Column(String(30))
    description = Column(String(400))