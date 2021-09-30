import datetime
from sqlalchemy.orm import Session
from . import models, serializers
from typing import Optional


def add_task(db: Session, task: serializers.TaskCreate):
    db_task = models.Task(**task.dict())

    db.add(db_task)
    db.commit()
    db.refresh(db_task)

    return db_task


def get_tasks(db: Session, date: Optional[datetime.date]):
    q = db.query(models.Task)
    if date:
        q = q.filter(models.Task.date==date)
    return q.all()


def delete_task(db: Session, task_id: int):
    db.query(models.Task).filter(models.Task.id == task_id).delete(synchronize_session=False)
    db.commit()
