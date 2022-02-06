from pydantic import BaseModel
from db import BaseMongoDBModel
from typing import Optional, Dict



class IndexModel(BaseMongoDBModel):
    name: Optional[str]
    methodology_file: Optional[Dict]
    factsheet_file: Optional[Dict]

class FileModel(BaseMongoDBModel):
    file_name: Optional[str]
    file_type: Optional[str]