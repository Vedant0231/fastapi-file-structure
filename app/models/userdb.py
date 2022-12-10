from database.database import Base
from sqlalchemy import Column , Integer , String  , DateTime , Boolean , Date

class user(Base):
    __tablename__ = "user_table"
    id = Column(Integer, primary_key = True,index = True)
    name = Column(String)
    birth_date = Column(Date)
    gender = Column(String)
    created_at = Column(DateTime)
    update_at = Column(DateTime)
    is_active = Column(Boolean)
    is_delete = Column(Boolean)
 