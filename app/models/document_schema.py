from pydantic import BaseModel, Field

class DocumentCreateSchema(BaseModel):
    title: str = Field(..., min_length=1, max_length=255)
    file_url: str