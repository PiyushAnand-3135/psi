from fastapi import FastAPI, UploadFile, File
from routers import face_detection, object_detection

app = FastAPI()

app.include_router(face_detection.router, prefix="/face")
# app.include_router(object_detection.router, prefix="/object")

@app.get("/")
async def root():
    return {"route_type" : "fast api root route"}


