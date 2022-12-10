from pydantic import BaseModel

class entry(BaseModel):
    id: int
    title: str 
    topic: str 
    state: str
    country: str
    is_delete: bool
    created_at: int
    updated_at: int
    competition_id: int