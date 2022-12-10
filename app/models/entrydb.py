from database.database import Base
from sqlalchemy import Column , Integer , String  , DateTime , Boolean , ForeignKey

class entry_table(Base):
    __tablename__ = "entry_table"
    id = Column(Integer, primary_key = True,index = True)
    title = Column(String)
    topic = Column(String)
    state = Column(String)
    country = Column(String)
    is_delete = Column(Boolean)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    competition_id = Column(Integer , ForeignKey("competition.id"))
 