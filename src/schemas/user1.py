from pydantic import BaseModel 

class StuBase(BaseModel):
    user_name : str
    Mobile_No : int
    Email : str
    Date_of_Birth : str
    password : str
    Gender : str

class User_OTP(BaseModel):
    Email : str
    
class OTP_Verify(BaseModel):
    Email : str
    otp : str
    
class Bookingbase(BaseModel):
    user_id : str
    Departure_from  : str
    Arrival_to  : str 
    Departure_Time : str 
    Departure_date  : str 
    Train_class  : str 
    Categories  : str 
    Num_of_passengers  : str 
    Food_Available  : str 
    Price_of_one_ticket  : str 
    Total_amount  : str 

class Payment(BaseModel):
    Booking_id : str
    payment_method : str
    transaction_status : str
    total_amount : str

class Trains(BaseModel):
    Train_name : str
    Train_class : str
    Departure_from : str
    Arrival_to : str
    Departure_Time: str
    Departure_date : str
    Price_of_one_ticket : str

class Schedules(BaseModel):
    train_id : str
    Departure_from : str
    Arrival_to: str
    Departure_Time: str
    Departure_date  : str
    JourneyDuration : str
    Booked_tickets : str
    Availability : str
    Status : str
    Stations  : str

class Mybookings(BaseModel):
    user_id   : str
    Booking_id  : str
    Train_name  : str
    Departure_from  : str
    Arrival_to  : str
    Departure_Time : str
    Departure_date  : str
    Booked_tickets  : str
    Booking_Status  : str
    Booking_date  : str