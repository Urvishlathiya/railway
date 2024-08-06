from sqlalchemy import Column,Integer,String,Boolean,DateTime , ForeignKey
from database.database import Base
from datetime import datetime
import uuid

class Schedule(Base):
    __tablename__ = "schedule"
    id = Column(String(50), primary_key=True, default=str(uuid.uuid4()))
    train_id = Column(String(50),ForeignKey("trains.id"))
    Departure_from = Column(String(30),nullable=False)
    Arrival_to = Column(String(30),nullable=False)
    Departure_Time= Column(String(30),nullable=False)
    Departure_date = Column(String(20), nullable = False)
    JourneyDuration = Column(String(20), nullable = False)
    Booked_tickets = Column(String(50),nullable = False)
    Availability = Column(String(20), nullable = False)
    Status = Column(String(30), nullable = False)
    Stations = Column(String(50), nullable = False)
    is_deleted=Column(Boolean,default=False)
    is_active=Column(Boolean,default=True)
    created_at=Column(DateTime,default=datetime.now)
    modified_at=Column(DateTime,default=datetime.now,onupdate=datetime.now)


    
    
