from sqlalchemy import Column, Integer, String, Date, Time
from app.dependencies import Base



class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, index=True)
    start_time = Column(Time)
    end_time = Column(Time)
    content = Column(String)