from fastapi import FastAPI
from uvicorn import run as uvrun
from .a2a_adapter import router
from .runtime_graph import runner          # your existing LangGraph 
runner

app = FastAPI()
app.include_router(router, prefix="/a2a")

if __name__ == "__main__":
    uvrun("{{cookiecutter.project_slug}}.main:app", host="0.0.0.0", 
port=8080, reload=True)

