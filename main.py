from fastapi import FastAPI
from src.router.user import User1
from src.router.user import Otp_router
from src.router.booking import Booking1



app = FastAPI()
app.include_router(User1)
app.include_router(Otp_router)
app.include_router(Booking1)