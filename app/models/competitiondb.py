from database.database import Base
from sqlalchemy import Column , Integer , String  , DateTime , Boolean , ForeignKey

class competition(Base):
    __tablename__ = "competition_table"
    id = Column(Integer, primary_key = True,index = True)
    name = Column(String)
    status = Column(DateTime)
    is_active = Column(Boolean)
    is_delete = Column(Boolean)
    created_at = Column(DateTime)
    update_at = Column(DateTime)
    description = Column(String)
    user_id = Column(Integer,ForeignKey("user.id"))
 