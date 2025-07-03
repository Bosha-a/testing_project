# loading once for being seen in all controllers
from helpers.config import Settings , get_settings
import os 
class BaseController:
    def __init__(self):
        self.app_settings: Settings = get_settings()   
        self.base_dir = os.path.dirname(os.path.dirname(__file__)) # path for parent or root (src)
        self.file_dir = os.path.join(self.base_dir, 'assets', 'files') 
        self.file_dir = self.base_dir + '/' + 'assets/files'