from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float
from sqlalchemy.sql import func

from src.models.base import Base


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
    field = Column(Integer, ForeignKey("Fields.field_id"))


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
