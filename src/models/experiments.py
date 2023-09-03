from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.sql import func

from src.models.base import Base


class Samples(Base):
    __tablename__ = "Samples"
    sample_id = Column(Integer, primary_key=True)
    borehole_id = Column(Integer, ForeignKey("Boreholes.borehole_id"))
    name = Column(String(30))
