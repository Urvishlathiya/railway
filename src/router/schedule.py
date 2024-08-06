from fastapi import FastAPI, HTTPException, APIRouter , Depends , Header
from database.database import SessionLocal
from src.model.user import User
from src.model.otp import Otp
from src.model.bookings import Booking
from src.model.schedule import Schedule
from passlib.context import CryptContext
from src.schemas.user1 import StuBase
from src.utils.otp import generate_otp,send_otp_email
from src.schemas.user1 import Bookingbase
from src.schemas.user1 import Schedules

from datetime import datetime


#from src.schemas.student import RollStu, BranchStu
Schedule1 = APIRouter(tags=["SCHEDULE"])


db = SessionLocal()



@Schedule1.post("/Schedule_of_trains/", response_model= Schedules)
def booking_tickets(schedule : Schedules):
    newdetail = Schedule(

    
    train_id = schedule.train_id,
    Departure_from = schedule.Departure_from,
    Arrival_to  = schedule.Arrival_to,
    Departure_Time = schedule.Departure_Time,
    Departure_date   = schedule.Departure_date,
    JourneyDuration  = schedule.JourneyDuration,
    Booked_tickets  = schedule.Booked_tickets,
    Availability  = schedule.Availability,
    Status  = schedule.Status,
    Stations   = schedule.Stations,

    )

    db.add(newdetail)
    db.commit()

    return schedule


@Schedule1.get("/get_schedule_details", response_model=Schedules)

def read_details(schdeule_id : str):
    breakpoint()
    schdeule = db.query(Schedule).filter(Schedule.id == schdeule_id, Schedule.is_active==True , Schedule.is_deleted == False).first()
    if schdeule is None:
        raise HTTPException(status_code=404, detail="Details not found")
    return schdeule


@Schedule1.get("/all_schedule_details/", response_model=list[Schedules])
def read_bookings():
    schedule = db.query(Schedule).filter(Schedule.is_active==True , Schedule.is_deleted==False).all()
    length_list = len(schedule)
    if length_list == 0:
        raise HTTPException(status_code=404, detail="Table is empty")
    return schedule



@Schedule1.put("/Update_schedule_details/", response_model=Schedules)
def update_person(schedule: Schedules):
    db_schedule = db.query().filter(Schedule.id == schedule.id).first()
    if db_schedule is None:
        raise HTTPException(status_code=404, detail="Details not found")


    
    db_schedule.train_id = schedule.train_id,
    db_schedule.Departure_from = schedule.Departure_from,
    db_schedule.Arrival_to= schedule.Arrival_to,
    db_schedule.Departure_Time= schedule.Departure_Time,
    db_schedule.Departure_date = schedule.Departure_date,
    db_schedule.JourneyDuration  = schedule.JourneyDuration,
    db_schedule.Booked_tickets = schedule.Booked_tickets,
    db_schedule.Availability  = schedule.Availability,
    db_schedule.Status = schedule.Status,
    db_schedule.Stations  = schedule.Stations,


    db.delete(db_schedule)
    db.commit()
    
    
    return db_schedule

