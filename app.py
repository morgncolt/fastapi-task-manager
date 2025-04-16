from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict

app = FastAPI()

# Data model
class Task(BaseModel):
    title: str
    description: str
    completed: bool = False

# In-memory database
tasks: Dict[int, Task] = {}
task_id_counter = 1

# Create task
@app.post("/tasks")
def create_task(task: Task) -> Dict[str, int]:
    global task_id_counter
    tasks[task_id_counter] = task
    task_id = task_id_counter
    task_id_counter += 1
    return {"task_id": task_id}

# Read task
@app.get("/tasks/{task_id}")
def read_task(task_id: int) -> Task:
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    return tasks[task_id]

# Read all tasks
@app.get("/tasks")
def read_all_tasks() -> Dict[int, Task]:
    return tasks

# Update task
@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: Task) -> Dict[str, str]:
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    tasks[task_id] = task
    return {"message": "Task updated successfully"}

# Delete task
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int) -> Dict[str, str]:
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    del tasks[task_id]
    return {"message": "Task deleted successfully"}
