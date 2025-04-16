from pydantic import BaseModel

class Item(BaseModel):  # Added BaseModel inheritance
    name: str  # Changed from int to str
    description: str

class User(BaseModel):
    username: str
    bio: str
