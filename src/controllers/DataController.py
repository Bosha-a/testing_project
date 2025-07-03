from BaseController import BaseController
from fastapi import UploadFile


class DataController(BaseController):
    def __init__(self):
        super().__init__()
        self.scaling_size = 1048576

    def validate_uploaded_file(self , file : UploadFile):
        if file.content_type not in self.app_settings.FILE_ALLOWED_TYPES:
            raise False
        
        if file.size > self.app_settings.FILE_MAX_SIZE * self.scaling_size: # file.size -> bytes    | FILE_MAX_SIZE -> MB
            return False