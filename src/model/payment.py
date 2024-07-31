from sqlalchemy import Column,Integer,String,Boolean,DateTime , ForeignKey
from database.database import Base
from datetime import datetime
import uuid

class Payment(Base):
    __tablename__ = "payment"
    payment_id = Column(String(50), primary_key=True, default=str(uuid.uuid4()))
    Booking_id = Column(String(50),ForeignKey("booking.id"))
    payment_method = Column(String(30),nullable=False)
    transaction_status= Column(String(30),nullable=False)
    total_amount = Column(String(20),nullable=False)
    is_deleted=Column(Boolean,default=False)
    is_active=Column(Boolean,default=True)
    created_at=Column(DateTime,default=datetime.now)
    modified_at=Column(DateTime,default=datetime.now,onupdate=datetime.now)