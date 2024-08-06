from fastapi import FastAPI, HTTPException, APIRouter , Depends , Header
from database.database import SessionLocal
from src.model.user import User
from src.model.otp import Otp
from src.model.bookings import Booking
from src.model.schedule import Schedule
from src.model.mybookings import Mybooking
from passlib.context import CryptContext
from src.schemas.user1 import StuBase
from src.utils.otp import generate_otp,send_otp_email
from src.schemas.user1 import Bookingbase
from src.schemas.user1 import Schedules
from src.schemas.user1 import Mybookings
from datetime import datetime


#from src.schemas.student import RollStu, BranchStu
mybooking1 = APIRouter(tags=["MY BOOKINGS"])


db = SessionLocal()



@mybooking1.post("/details_of_mybookings", response_model= Mybookings)
def booking_tickets(mybooking : Mybookings):
    newdetail = Mybooking(

    
    user_id = mybooking.user_id,
    Booking_id = mybooking.Booking_id,
    Train_name = mybooking.Train_name,
    Departure_from = mybooking.Departure_from,
    Arrival_to = mybooking.Arrival_to,
    Departure_Time= mybooking.Departure_Time,
    Departure_date = mybooking.Departure_date,
    Booked_tickets = mybooking.Booked_tickets,
    Booking_Status = mybooking.Booking_Status,
    Booking_date = mybooking.Booking_date

    )

    db.add(newdetail)
    db.commit()

    return newdetail


@mybooking1.get("/get_mybooking_details", response_model=Mybookings)

def read_details(mybooking_id : str):
    breakpoint()
    mybooking = db.query(Mybooking).filter(Mybooking.id == mybooking_id, Mybooking.is_active==True , Mybooking.is_deleted == False).first()
    if mybooking is None:
        raise HTTPException(status_code=404, detail="Details not found")
    return mybooking


@mybooking1.get("/my_all_booking_details/", response_model=list[Mybookings])
def read_bookings():
    mybooking = db.query(Mybooking).filter(Mybooking.is_active==True , Mybooking.is_deleted==False).all()
    length_list = len(mybooking)
    if length_list == 0:
        raise HTTPException(status_code=404, detail="Table is empty")
    return mybooking



@mybooking1.put("/Update_mybooking_details/", response_model=Mybookings)
def update_person(mybooking_id: str,mybooking : Mybookings):
    db_mybooking = db.query(Mybooking).filter(Mybooking.id == mybooking_id).first()
    if db_mybooking is None:
        raise HTTPException(status_code=404, detail="Details not found")

    db_mybooking.user_id  = mybooking.user_id,
    db_mybooking.Booking_id = mybooking.Booking_id,
    db_mybooking.Train_name = mybooking.Train_name,
    db_mybooking.Departure_from = mybooking.Departure_from,
    db_mybooking.Arrival_to = mybooking.Arrival_to,
    db_mybooking.Departure_Time= mybooking.Departure_Time,
    db_mybooking.Departure_date = mybooking.Departure_date,
    db_mybooking.Booked_tickets = mybooking.Booked_tickets,
    db_mybooking.Booking_Status = mybooking.Booking_Status,
    db_mybooking.Booking_date = mybooking.Booking_date

    db.add(db_mybooking)
    db.commit()
    
    return db_mybooking

