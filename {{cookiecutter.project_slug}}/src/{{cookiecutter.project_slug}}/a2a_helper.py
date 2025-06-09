from __future__ import annotations
from fastapi import APIRouter, HTTPException
from a2a_protocol.models import Task, TaskStatus
from langgraph.messages import MessageChannel
from typing import Dict

# LangGraph channels: already declared in a2a_channels.py
from .a2a_channels import review_channel, data_channel

router = APIRouter()
TASK_STORE: Dict[str, Task] = {}   # simple in-memory store

@router.post("/tasks/send", response_model=Task, status_code=202)
def send_task(task: Task):
    TASK_STORE[task.id] = task
    # Fan-out to graph: put the task body on the shared message bus
    review_channel.put(task)
    return task.copy(update={"status": TaskStatus.ACCEPTED})

@router.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: str):
    task = TASK_STORE.get(task_id)
    if not task:
        raise HTTPException(404, "task not found")
    return task

