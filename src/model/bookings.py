from sqlalchemy import Column,Integer,String,Boolean,DateTime , ForeignKey
from database.database import Base
from datetime import datetime
import uuid

class Booking(Base):
    __tablename__ = "booking"
    id = Column(String(50), primary_key=True, default=str(uuid.uuid4()))
    user_id = Column(String(50),ForeignKey("users.id")),
    Departure_from = Column(String(30),nullable=False)
    Arrival_to = Column(String(30),nullable=False)
    Departure_Time= Column(String(30),nullable=False)
    Departure_date = Column(String(20), nullable = False)
    Train_class = Column(String(30),nullable=False)
    Categories = Column(String(40),nullable=False)
    Num_of_passengers = Column(String(20),nullable=False)
    Food_Available = Column(String(10),nullable=False)
    Price_of_one_ticket = Column(String(20),nullable=False)
    Total_amount = Column(String(20),nullable=False)
    is_deleted=Column(Boolean,default=False)
    is_active=Column(Boolean,default=True)
    created_at=Column(DateTime,default=datetime.now)
    modified_at=Column(DateTime,default=datetime.now,onupdate=datetime.now)


    
    
