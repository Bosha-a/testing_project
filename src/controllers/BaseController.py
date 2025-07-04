# loading once for being seen in all controllers
from helpers.config import Settings , get_settings
import os 
import random 
import string

class BaseController:
    def __init__(self):
        self.app_settings: Settings = get_settings()   
        self.base_dir = os.path.dirname(os.path.dirname(__file__)) # path for parent or root (src)
        self.files_dir = os.path.join(self.base_dir, 'assets', 'files') 


        def generate_random_string(self, length: int = 12) -> str:
            """
            Generate a random string of fixed length.
            """
            letters = string.ascii_letters + string.digits
            return ''.join(random.choice(letters) for i in range(length))