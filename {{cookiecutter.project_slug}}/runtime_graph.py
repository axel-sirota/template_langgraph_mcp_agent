from .a2a_client import send_task, get_task_result

def coder_node(state):
    todo = state["user_input"]
    peer_task_id = send_task({"text": f"Write docs for: {todo}"})
    result = get_task_result(peer_task_id)
    return {"peer_reply": result.body}

