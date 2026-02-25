import subprocess

def teacher_response(prompt: str) -> str:
    result = subprocess.run(
        ["ollama", "run", "mistral", prompt],
        capture_output=True,
        text=True
    )
    return result.stdout.strip()
