from pydantic import BaseModel

class CategoryOut(BaseModel):
    id:   int
    name: str

class BusinessOut(BaseModel):
    id:       int
    name:     str
    category: str
    location: str
    rating:   float