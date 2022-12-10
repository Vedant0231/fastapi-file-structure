from pydantic import BaseModel

class user(BaseModel):
    id: int
    name: str
    birth_date: int
    gender: str
    created_at: int
    update_at: int
    is_active: bool
    is_delete: bool
 