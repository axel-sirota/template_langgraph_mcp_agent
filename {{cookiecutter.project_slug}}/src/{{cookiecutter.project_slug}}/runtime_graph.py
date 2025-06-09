from .a2a_client import send_task, get_task_result
import langchain; from langchain.cache import InMemoryCache
langchain.cache = InMemoryCache(maxsize=1_000)   # avoid duplicate calls 

def coder_node(state):
    todo = state["user_input"]
    peer_task_id = send_task({"text": f"Write docs for: {todo}"})
    result = get_task_result(peer_task_id)
    return {"peer_reply": result.body}

