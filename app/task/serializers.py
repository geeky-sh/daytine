import datetime
from pydantic import BaseModel, Field

class TaskBase(BaseModel):
    date: datetime.date = Field(example="1991-01-23")
    start_time: datetime.time = Field(example="7:00")
    end_time: datetime.time = Field(example="8:00")
    content: str = Field(max_length=255, example="Exercise")


class TaskCreate(TaskBase):
    pass


class Task(TaskBase):
    id: int

    class Config:
        orm_mode = True

