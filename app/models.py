from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()

class Table(Base):
    __tablename__ = "tables"
    
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    seats = Column(Integer)
    location = Column(String(150))

    reservations = relationship("Reservation", back_populates="table")

class Reservation(Base):
    __tablename__ = "reservations"
    
    id = Column(Integer, primary_key=True)
    customer_name = Column(String(100))
    table_id = Column(Integer, ForeignKey("tables.id"))
    reservation_time = Column(DateTime)
    duration_minutes = Column(Integer)
    
    table = relationship("Table", back_populates="reservations")