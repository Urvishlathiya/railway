from fastapi import FastAPI
from src.router.user import User1
from src.router.user import Otp_router
from src.router.booking import Booking1
from src.router.payment import pay
from src.router.trains import Train1
from src.router.schedule import Schedule1
from src.router.mybooking import mybooking1



app = FastAPI()
app.include_router(User1)
app.include_router(Otp_router)
app.include_router(Booking1)
app.include_router(pay)
app.include_router(Train1)
app.include_router(Schedule1)
app.include_router(mybooking1)