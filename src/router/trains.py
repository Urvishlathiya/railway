from fastapi import FastAPI, HTTPException, APIRouter , Depends , Header
from database.database import SessionLocal
from src.model.user import User
from src.model.otp import Otp
from src.model.bookings import Booking
from src.model.trains import Train
from passlib.context import CryptContext
from src.schemas.user1 import StuBase
from src.utils.otp import generate_otp,send_otp_email
from src.schemas.user1 import Bookingbase
from src.schemas.user1 import Trains
from datetime import datetime


#from src.schemas.student import RollStu, BranchStu
Train1 = APIRouter(tags=["TRAINS"])


db = SessionLocal()



@Train1.post("/trains/", response_model= Trains)
def trains_details(train : Trains):
    newDetail = Train(

    Train_name = train.Train_name,
    Train_class = train.Train_class,
    Departure_from = train.Departure_from,
    Arrival_to = train.Arrival_to,
    Departure_Time= train.Departure_Time,
    Departure_date = train.Departure_date,
    Price_of_one_ticket = train.Price_of_one_ticket,
    
    )

    db.add(newDetail)
    db.commit()

    return train


@Train1.get("/get_train_details", response_model=Trains)

def read_details(train_id : str):
    breakpoint()
    details = db.query(Train).filter(Train.id == train_id, Train.is_active==True , Train.is_deleted == False).first()
    if details is None:
        raise HTTPException(status_code=404, detail="Details not found")
    return details


@Train1.get("/all_details/", response_model=list[Trains])
def read_details():
    details = db.query(Train).filter(Train.is_active==True , Train.is_deleted==False).all()
    length_list = len(details)
    if length_list == 0:
        raise HTTPException(status_code=404, detail="Table is empty")
    return details



@Train1.put("/Update_train_details/", response_model=Trains)
def update_details(train_id: str , train : Trains):
    db_detail = db.query(Train).filter(Train.id == train_id).first()
    if db_detail is None:
        raise HTTPException(status_code=404, detail="Details not found")


    
    db_detail.Train_name = train.Train_name,
    db_detail.Train_class = train.Train_class,
    db_detail.Departure_from = train.Departure_from,
    db_detail.Arrival_to = train.Arrival_to,
    db_detail.Departure_Time= train.Departure_Time,
    db_detail.Departure_date = train.Departure_date,
    db_detail.Price_of_one_ticket = train.Price_of_one_ticket,
    


    db.delete(db_detail)
    db.commit()
    
    
    return db_detail

