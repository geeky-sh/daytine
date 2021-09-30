import datetime
from pydantic import BaseModel

class TaskBase(BaseModel):
    date: datetime.date
    start_time: datetime.time
    end_time: datetime.time
    content: str


class TaskCreate(TaskBase):
    pass


class Task(TaskBase):
    id: int

    class Config:
        orm_mode = True

