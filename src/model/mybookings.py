from sqlalchemy import Column,Integer,String,Boolean,DateTime , ForeignKey
from database.database import Base
from datetime import datetime
import uuid


class Mybooking(Base):
    __tablename__ = "mybooking"
    id = Column(String(50), primary_key=True, default=str(uuid.uuid4()))
    user_id = Column(String(50),ForeignKey("users.id"))
    Booking_id = Column(String(50),ForeignKey("booking.id"))
    Train_name = Column(String(30),nullable=False)
    Departure_from = Column(String(30),nullable=False)
    Arrival_to = Column(String(30),nullable=False)
    Departure_Time= Column(String(30),nullable=False)
    Departure_date = Column(String(20), nullable = False)
    Booked_tickets = Column(String(50),nullable = False)
    Booking_Status = Column(String(50), nullable = False)
    Booking_date = Column(String(40),nullable=False)
    is_deleted=Column(Boolean,default=False)
    is_active=Column(Boolean,default=True)
    created_at=Column(DateTime,default=datetime.now)
    modified_at=Column(DateTime,default=datetime.now,onupdate=datetime.now)


    
    
