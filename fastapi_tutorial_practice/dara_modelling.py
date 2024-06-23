from pydantic import BaseModel
class NewStudent(BaseModel):
    name: str
    age: int