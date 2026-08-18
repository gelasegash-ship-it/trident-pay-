from fastapi import APIRouter, UploadFile
import cloudinary
import cloudinary.uploader
import os

router = APIRouter()

cloudinary.config(
    cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME"),
    api_key=os.getenv("CLOUDINARY_API_KEY"),
    api_secret=os.getenv("CLOUDINARY_API_SECRET")
)

@router.post("/upload")
async def upload_file(file: UploadFile):
    result = cloudinary.uploader.upload(file.file)
    return {"url": result["secure_url"]}
