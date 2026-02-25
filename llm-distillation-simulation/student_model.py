import subprocess

def student_response(prompt: str) -> str:
    result = subprocess.run(
        ["ollama", "run", "phi", prompt],
        capture_output=True,
        text=True
    )
    return result.stdout.strip()