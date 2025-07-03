# loading once for being seen in all controllers

from helpers.config import Settings , get_settings

class BaseController:
    def __init__(self):
        self.app_settings: Settings = get_settings()