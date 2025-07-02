from fastapi import FastAPI , APIRouter
from helpers.config import get_settings 

base_router = APIRouter(
    prefix="/api/v1", # static prefix before each route 
    tags=["api_v1"], # organized routes under a specific_tag
    # responses={404: {"description": "Not found"}}
)

@base_router.get("/")
async def welcome():
    app_settings = get_settings()

    app_name = app_settings.APP_NAME
    app_version = app_settings.APP_VERSION
    return {
        "message": "Hello ",
        "app_name" : app_name ,
        "app_version" : app_version
    }
