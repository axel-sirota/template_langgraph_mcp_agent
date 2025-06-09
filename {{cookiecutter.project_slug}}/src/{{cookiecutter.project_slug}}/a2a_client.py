from a2a_protocol.client import A2AClient            # SDK facade 
:contentReference[oaicite:4]{index=4}
from typing import Dict, Any

# -- 1. initialise once (could read from .env) 
-----------------------------
PEER_URL = "http://localhost:8080/a2a"               # target peer
client   = A2AClient(base_url=PEER_URL)

# -- 2. send work 
----------------------------------------------------------
def send_task(body: str | Dict[str, Any]) -> str:
    """
    POST /tasks/send to a peer agent and return the task id.
    `body` can be a simple string or a dict that matches the A2A Task body 
schema.
    """
    task = client.create_task(body=body)             # wrapped POST 
:contentReference[oaicite:5]{index=5}
    return task.id

# -- 3. fetch the answer 
---------------------------------------------------
def get_task_result(task_id: str):
    """
    GET /tasks/<task_id> until status == COMPLETED, then return the final 
Task.
    """
    while True:
        task = client.get_task(task_id)              # wrapped GET 
:contentReference[oaicite:6]{index=6}
        if task.status in {"COMPLETED", "FAILED"}:
            return task
        client.sleep(1)                              # back-off helper in 
SDK

