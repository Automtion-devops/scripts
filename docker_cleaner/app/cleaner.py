import subprocess
import logging

logging.basicConfig(filename="docker_cleaner.log", level=logging.INFO, format="%(asctime)s - %(message)s")

def run_command(command: str) -> str:
    try:
        result = subprocess.run(command, shell=True, text=True, capture_output=True)
        output = result.stdout if result.returncode == 0 else result.stderr
        logging.info(f"CMD: {command}\n{output}")
        return output
    except Exception as e:
        logging.error(f"Error ejecutando comando: {command} - {e}")
        return f"Error: {e}"

def basic_clean(): return run_command("docker system prune -f")
def advanced_clean(): return run_command("docker system prune -a -f")
def volume_clean(): return run_command("docker volume prune -f")
def show_status(): return run_command("docker ps -a && docker images && docker volume ls")
def show_disk(): return run_command("docker system df")
