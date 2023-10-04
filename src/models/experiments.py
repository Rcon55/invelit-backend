from sqlalchemy import Column, Integer, String, ForeignKey, DateTime

from src.models.base import Base


class Samples(Base):
    __tablename__ = "Samples"
    sample_id = Column(Integer, primary_key=True)
    borehole_id = Column(Integer, ForeignKey("Boreholes.borehole_id"))
    name = Column(String(30))


class Experiments(Base):
    __tablename__ = "Experiments"
    sample_id = Column(Integer, ForeignKey("Samples.sample_id"))
    experiment_date = Column(DateTime(timezone=True))
