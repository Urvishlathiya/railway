from fastapi import FastAPI, HTTPException, APIRouter , Depends , Header
from database.database import SessionLocal
from src.model.user import User
from src.model.otp import Otp
from src.model.bookings import Booking
from passlib.context import CryptContext
from src.schemas.user1 import StuBase
from src.utils.otp import generate_otp,send_otp_email
from src.schemas.user1 import Bookingbase
from datetime import datetime


#from src.schemas.student import RollStu, BranchStu
Booking1 = APIRouter()


db = SessionLocal()

pwd_context = CryptContext(schemes = ["bcrypt"] , deprecated = "auto")

@Booking1.post("/Book_tickets/", response_model= Bookingbase)
def booking_tickets(booking : Bookingbase):
    newBooking = Booking(

    user_id = booking.user_id, 
    Departure_from =booking.Departure_from,
    Arrival_to =booking.Arrival_to,
    Departure_Time=booking.Departure_Time,
    Departure_date = booking.Departure_date,
    Train_class = booking.Train_class,
    Categories = booking.Categories,
    Num_of_passengers = booking.Num_of_passengers,
    Food_Available = booking.Food_Available,
    Price_of_one_ticket = booking.Price_of_one_ticket,
    Total_amount = booking.Total_amount,

    )

    db.add(newBooking)
    db.commit()

    return booking


@Booking1.get("/get_booking_details", response_model=Bookingbase)

def read_bookings(booking_id : str):
    breakpoint()
    booking = db.query(Booking).filter(Booking.id == booking_id, Booking.is_active==True , Booking.is_deleted == False).first()
    if booking is None:
        raise HTTPException(status_code=404, detail="Details not found")
    return booking


@Booking1.get("/all_booking_details/", response_model=list[Bookingbase])
def read_bookings():
    booking = db.query(Booking).filter(Booking.is_active==True , Booking.is_deleted==False).all()
    length_list = len(booking)
    if length_list == 0:
        raise HTTPException(status_code=404, detail="Table is empty")
    return booking



@Booking1.put("/Update_booking_details/", response_model=Bookingbase)
def update_person(user_id: str, booking: Bookingbase):
    db_booking = db.query(Booking).filter(Booking.id == user_id).first()
    if db_booking is None:
        raise HTTPException(status_code=404, detail="User not found")
    db_booking.user_id = booking.user_id, 
    db_booking.Departure_from =booking.Departure_from,
    db_booking.Arrival_to =booking.Arrival_to,
    db_booking.Departure_Time=booking.Departure_Time,
    db_booking.Departure_date = booking.Departure_date,
    db_booking.Train_class = booking.Train_class,
    db_booking.Categories = booking.Categories,
    db_booking.Num_of_passengers = booking.Num_of_passengers,
    db_booking.Food_Available = booking.Food_Available,
    db_booking.Price_of_one_ticket = booking.Price_of_one_ticket,
    db_booking.Total_amount = booking.Total_amount,


    db.commit()
    
    return db_booking

