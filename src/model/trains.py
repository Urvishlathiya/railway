from sqlalchemy import Column,Integer,String,Boolean,DateTime , ForeignKey
from database.database import Base
from datetime import datetime
import uuid

class Train(Base):
    __tablename__ = "trains"
    id = Column(String(50), primary_key=True, default=str(uuid.uuid4()))
    Train_name  = Column(String(100),nullable = False)
    Train_class = Column(String(30),nullable=False)
    Departure_from = Column(String(30),nullable=False)
    Arrival_to = Column(String(30),nullable=False)
    Departure_Time= Column(String(30),nullable=False)
    Departure_date = Column(String(20), nullable = False)
    Price_of_one_ticket = Column(String(20),nullable=False)
    is_deleted=Column(Boolean,default=False)
    is_active=Column(Boolean,default=True)
    created_at=Column(DateTime,default=datetime.now)
    modified_at=Column(DateTime,default=datetime.now,onupdate=datetime.now)
