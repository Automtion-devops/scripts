import subprocess
import sys
import logging

def check_docker_access() -> bool:
    """Verifica si Docker está disponible y accesible."""
    try:
        result = subprocess.run("docker info", shell=True, text=True, capture_output=True)
        if result.returncode != 0 or "Cannot connect" in result.stderr:
            return False
        return True
    except Exception as e:
        log_error(f"Error verificando Docker: {e}")
        return False

def ensure_docker_or_exit():
    """Sale del programa si Docker no está accesible."""
    if not check_docker_access():
        print("[ERROR] Docker no está disponible o no tienes permisos. ¿Está el daemon activo?")
        sys.exit(1)

def log_info(msg: str):
    logging.info(msg)

def log_error(msg: str):
    logging.error(msg)
