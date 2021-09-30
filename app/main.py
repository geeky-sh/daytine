from fastapi import FastAPI
from app.task.router import router as task_router


app = FastAPI()
app.include_router(task_router)


@app.get('/')
def index():
    return {"working": True}