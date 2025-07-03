from fastapi import FastAPI , APIRouter , Depends , UploadFile, status
from fastapi.responses import JSONResponse
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

    is_valid , result_signal = DataController().validate_uploaded_file(file)
    
    if not is_valid:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            # status_code=400 # it is also ok 
            content={
                "signal": result_signal
            }
        )