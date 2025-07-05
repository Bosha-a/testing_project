from pydantic import BaseModel
from typing import Optional 

class ProcessRequest(BaseModel):
    project_id: str
    file_id: str
    chunk_size : Optional[int] = 100 # default chunk size for processing is 100 if user didnt input anything 
    overlap_size: Optional[int] = 20 
    do_reset: Optional[int] = 0 # reset the process if user want to start over