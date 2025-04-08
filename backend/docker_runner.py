import subprocess
import os
import uuid

DOCKER_IMAGE_NAME = "lambda-python-func"  # already built
TEMP_DIR = "/tmp/lambda_functions"

def run_function_in_docker(code: str) -> str:
    # 1. Create temp dir if not exists
    os.makedirs(TEMP_DIR, exist_ok=True)

    # 2. Generate unique file name
    file_id = str(uuid.uuid4())
    file_path_host = os.path.join(TEMP_DIR, f"{file_id}.py")
    file_path_container = f"/app/{file_id}.py"

    # 3. Save code to file
    with open(file_path_host, "w") as f:
        f.write(code)

    # 4. Run Docker container with mounted code file
    try:
        result = subprocess.run([
            "docker", "run", "--rm",
            "-v", f"{TEMP_DIR}:/app",  # mount host:/app inside container
            DOCKER_IMAGE_NAME,
            "python", file_path_container
        ], capture_output=True, text=True, timeout=10)

        if result.returncode == 0:
            return result.stdout
        else:
            return f"Error:\n{result.stderr}"
    except subprocess.TimeoutExpired:
        return "Error: Execution timed out."

