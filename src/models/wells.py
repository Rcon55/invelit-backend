from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func

from src.models.base import Base


class Wells(Base):
    __tablename__ = "Wells"
    well_id = Column(Integer, primary_key=True)
    well_name = Column(String(30), nullable=False)
    field = Column(String(30))
    time_created = Column(DateTime(timezone=True), server_default=func.now())


class Boreholes(Base):
    __tablename__ = "Boreholes"
    borehole_id = Column(Integer, primary_key=True)
    borehole_name = Column(String(30), nullable=False)
    well_id = Column(Integer, ForeignKey("Wells.well_id"))
