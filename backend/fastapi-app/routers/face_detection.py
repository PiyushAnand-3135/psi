from fastapi import APIRouter, File, UploadFile
import requests


router = APIRouter()

EXPRESS_API_URL = "http://localhost:8080/mark-attendance"

@router.post("/detect-face")
async def detect_face(file : UploadFile = File(...)):
    detected_user = {"user_id" : 1,
                     "name" : "Piyush Anand",
                     "confidence" : 0.98}
    return {"status" : "success", "detected_user" : detected_user}