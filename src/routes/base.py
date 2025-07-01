from fastapi import FastAPI , APIRouter
import os 

base_router = APIRouter(
    prefix="api/v1", # static prefix before each route 
    tags=["api_v1"], # organized routes under a specific_tag
    responses={404: {"description": "Not found"}}
)

@base_router.get("/")
async def welcome():
    app_name = os.getenv("APP_NAME")
    app_version = os.getenv("APP_VERSION")
    return {
        "message": "Hello ",
        "app_name" : app_name ,
        "app_version" : app_version
    }
