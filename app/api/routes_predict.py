from fastapi import APIRouter, Depends
from pydantic import BaseModel
from app.core.dependencies import get_api_key, get_current_user
from app.services.model_service import predict_spam_ham

router = APIRouter()

class Email(BaseModel):
    email: str


@router.post("/predict")
def predict_price(email: Email, user = Depends(get_current_user), _= Depends(get_api_key)):
    prediction = predict_spam_ham(email.model_dump())
    return {"Spam or Ham": prediction}