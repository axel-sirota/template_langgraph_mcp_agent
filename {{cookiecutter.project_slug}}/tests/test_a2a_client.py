from {{cookiecutter.project_slug}}.a2a_client import send_task, 
get_task_result
import uuid

def test_roundtrip():
    tid = send_task(f"ping-{uuid.uuid4()}")
    task = get_task_result(tid)
    assert task.status == "COMPLETED"
    assert "pong" in task.body.lower()   # whatever your peer returns

