from fastapi import APIRouter, HTTPException
from datetime import datetime
from database.database import SessionLocal
# from database import get_db
from src.model.payment import Payment as PaymentModel
from src.schemas.user1 import Payment as PaymentSchema
import uuid

pay = APIRouter(tags=["PAYMENT"])
db = SessionLocal()


@pay.post("/add_payments_data/", response_model=PaymentSchema)
def create_payment(payment: PaymentSchema):
    db_payment = PaymentModel(
        Booking_id = payment.Booking_id,
        payment_method=payment.payment_method,
        transaction_status=payment.transaction_status,
        total_amount=payment.total_amount,
        is_deleted=False,
        is_active=True,
        created_at=datetime.now(),
        modified_at=datetime.now()
    )
    db.add(db_payment)
    db.commit()

    return db_payment

@pay.get("/Get_Payment", response_model=PaymentSchema)
def read_payment(payment_id: str):
    db_payment = db.query(PaymentModel).filter(PaymentModel.payment_id == payment_id).first()
    if db_payment is None:
        raise HTTPException(status_code=404, detail="Payment not found")
    return db_payment

@pay.put("/Update_payments_detail", response_model=PaymentSchema)
def update_payment(payment_id: str, payment: PaymentSchema):
    db_payment = db.query(PaymentModel).filter(PaymentModel.payment_id == payment_id).first()
    if db_payment is None:
        raise HTTPException(status_code=404, detail="Payment not found")
    for key, value in payment.dict().items():
        setattr(db_payment, key, value)
    db_payment.modified_at = datetime.now()
    db.commit()
    
    return db_payment

@pay.delete("/Delete_payments")
def delete_payment(payment_id: str):
    db_payment = db.query(PaymentModel).filter(PaymentModel.payment_id == payment_id).first()
    if db_payment is None:
        raise HTTPException(status_code=404, detail="Payment not found")
    db.delete(db_payment)
    db.commit()
    return {"detail": "Payment deleted"}
