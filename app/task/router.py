import datetime
from typing import List, Optional
from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from . import query, serializers
from app.dependencies import get_db, NoOp


router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.get("/", response_model=List[serializers.Task], summary="Get list of tasks for the day")
def get_tasks(date: Optional[datetime.date] = None, db: Session = Depends(get_db)):
    return query.get_tasks(db, date=date)


@router.post('/', response_model=serializers.Task, summary="Create a task")
def add_task(task: serializers.TaskCreate, db: Session = Depends(get_db)):
    return query.add_task(db, task)


@router.delete("/{task_id}", response_model=NoOp, summary="Delete a task by task_id")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    query.delete_task(db, task_id)
    return NoOp()