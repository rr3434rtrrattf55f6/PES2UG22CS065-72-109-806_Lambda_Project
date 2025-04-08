from fastapi import FastAPI
from pydantic import BaseModel
from docker_runner import run_function_in_docker

app = FastAPI()

class CodeRequest(BaseModel):
    code: str

@app.post("/run")
def run_code(request: CodeRequest):
    result = run_function_in_docker(request.code)
    return {"output": result}

