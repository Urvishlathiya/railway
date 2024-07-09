from fastapi import FastAPI, HTTPException, APIRouter , Depends , Header
from database.database import SessionLocal
from src.model.user import User
from src.model.otp import Otp
from passlib.context import CryptContext
from src.schemas.user1 import StuBase
from src.utils.otp import generate_otp,send_otp_email
from src.schemas.user1 import User_OTP
from src.schemas.user1 import OTP_Verify
from datetime import datetime
from src.utils.token import decode_token_user_id,decode_token_user_email,decode_token_user_name,logging_token


#from src.schemas.student import RollStu, BranchStu
User1 = APIRouter()
Otp_router = APIRouter()
db = SessionLocal()



pwd_context = CryptContext(schemes = ["bcrypt"] , deprecated = "auto")

@User1.post("/Register/", response_model=StuBase)
def create_user_id(stu: StuBase):
    newUser = User(

    user_name = stu.user_name,
    Mobile_No = stu.Mobile_No,
    Email = stu.Email,
    password = pwd_context.hash(stu.password),
    Date_of_Birth =stu.Date_of_Birth,
    Gender = stu.Gender,
    
    )
    db.add(newUser)
    db.commit()
    return stu


@User1.get("/get_user_details", response_model=StuBase)

def read_person(user_id : int):
    stu = db.query(User).filter(User.id == user_id, User.is_active==True , User.is_deleted == False).first()
    if stu is None:
        raise HTTPException(status_code=404, detail="Person not found")
    return stu



@User1.get("/post_your_details/", response_model=list[StuBase])
def read_persons():
    stu = db.query(User).filter(User.is_active==True , User.is_deleted==False).all()
    length_list = len(stu)
    if length_list == 0:
        raise HTTPException(status_code=404, detail="Table is empty")
    return stu


@User1.get("/get_data",response_model=StuBase)
def update_user_pass(email: str, password:str):
    db_user = db.query(User).filter(User.Email == email, User.is_active == True).first()
    #breakpoint()
    if db_user.Email == email:
        if pwd_context.verify(password,db_user.password):
            return db_user
    raise HTTPException(status_code=404, detail="user not found")


@User1.put("/Update_user_details/", response_model=StuBase)
def update_person(user_id: int, stu: StuBase):
    db_stu = db.query(User).filter(User.id == user_id).first()
    if db_stu is None:
        raise HTTPException(status_code=404, detail="User not found")
    db_stu.user_name = stu.user_name,
    db_stu.Mobile_No = stu.Mobile_No,
    db_stu.Email = stu.Email,
    db_stu.Date_of_Birth =stu.Date_of_Birth,
    db_stu.Gender = stu.Gender,

    db.commit()
    
    return db_stu


@User1.put("/delete_user")
def delete_person(user_id: int ):
    db_stu = db.query(User).filter(User.id == user_id).first()
    if db_stu is None:
        raise HTTPException(status_code=404, detail="User not found")
    db_stu.is_deleted = True
    db_stu.is_active = False
    db.commit()
    return {"message": "User deleted successfully"}

#-------------------- OTP -----------------------------

@Otp_router.post("/generate_otp")
def generate_otp_endpoint(request: User_OTP):
    email = request.Email
    user = db.query(User).filter(User.Email == email).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    otp_code = generate_otp(email)
    send_otp_email(email, otp_code)

    return {"message": "OTP generated and sent successfully to the provided email address."}



#**********************************************verify_otp********************************************

@Otp_router.post("/verify_otp")
def verify_otp(otp_verify: OTP_Verify):
    otp_entry = db.query(Otp).filter(
        Otp.Email == otp_verify.Email,
        Otp.otp == otp_verify.otp,
        Otp.expires_at > datetime.now(),
    ).first()
    if otp_entry is None:
        raise HTTPException(status_code=400, detail="Invalid or expired OTP") 
    db_user = db.query(User).filter(User.Email == otp_verify.Email).first()
    db_user.is_verified = True

    
    db.delete(otp_entry)
    db.commit()


    return {"message": "OTP verified successfully"}


#--------------------------------Login(token)---------------------------



@User1.get("/logging_user")
def logging_user(Email:str, password:str):
    # breakpoint()

    db_user = db.query(User).filter(User.Email == Email,User.is_active == True,User.is_deleted == False,User.is_verified == True).first()
    if db_user is None:
      
        raise HTTPException(status_code=404, detail="User not found")
    
    if not pwd_context.verify(password, db_user.password):
   
        raise HTTPException(status_code=404, detail="Password is incorrect")
    
    access_token = logging_token(db_user.id,Email,db_user.user_name)
    return  access_token

#------------------------------------------------------------------------------------------------------

