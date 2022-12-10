from pydantic import BaseModel

class competition(BaseModel):
    id: int
    name: str
    status: str 
    is_active: bool 
    is_delete: bool
    created_at: int
    update_at: int
    description: str
    user_id: int
 