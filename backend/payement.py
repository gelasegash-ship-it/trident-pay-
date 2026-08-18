from fastapi import APIRouter
from pydantic import BaseModel
router = APIRouter()
class PaymentRequest(BaseModel): amount: int; currency: str = "XAF"; customer_email: str
@router.post("/pay")
def create_payment(payment: PaymentRequest): return {"status": "ok", "amount": payment.amount}
