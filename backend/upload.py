from fastapi import APIRouter, UploadFile, File, HTTPException
import cloudinary, cloudinary.uploader, os
router = APIRouter()
cloudinary.config(cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME"), api_key=os.getenv("CLOUDINARY_API_KEY"), api_secret=os.getenv("CLOUDINARY_API_SECRET"))
@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    result = cloudinary.uploader.upload(file.file, resource_type="auto")
    return {"url": result["secure_url"]}
