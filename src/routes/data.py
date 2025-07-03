from fastapi import FastAPI , APIRouter , Depends , UploadFile
import os 
from helpers.config import get_settings , Settings
from controllers import DataController


data_router = APIRouter(
    prefix="/api/v1/data",
    tags=["api_v1" , "data"]
)

@data_router.post("/upload/{priject_id}")
async def upload_data(project_id: str, file: UploadFile, 
                      app_settings : Settings = Depends(get_settings)): 
    """
    Upload data to the specified project.
    Logic:
    Allowed File type 
    Allowed MAX Size 
    """

    is_valid = DataController().validate_uploaded_file(file)
    return { 
        is_valid
    }