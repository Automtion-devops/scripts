from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
from app import cleaner
from app.utils import ensure_docker_or_exit, log_info, log_error

# Asegúrate de que Docker esté disponible
ensure_docker_or_exit()
log_info("Usuario inició Docker Cleaner en modo Web.")

app = Flask(__name__, static_folder="static", template_folder="templates")
CORS(app)  # Habilita CORS para permitir solicitudes desde otros dominios

@app.route("/")
def index():
    """Sirve la página principal."""
    return render_template("index.html")

@app.route("/status", methods=["GET"])
def status():
    """Devuelve el estado actual de Docker."""
    try:
        result = cleaner.show_status()
        log_info("Endpoint /status ejecutado correctamente.")
        return jsonify({"status": "success", "result": result})
    except Exception as e:
        log_error(f"Error en /status: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route("/clean/basic", methods=["POST"])
def clean_basic():
    """Realiza una limpieza básica."""
    try:
        result = cleaner.basic_clean()
        log_info("Endpoint /clean/basic ejecutado correctamente.")
        return jsonify({"status": "success", "result": result})
    except Exception as e:
        log_error(f"Error en /clean/basic: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route("/clean/advanced", methods=["POST"])
def clean_advanced():
    """Realiza una limpieza avanzada."""
    try:
        result = cleaner.advanced_clean()
        log_info("Endpoint /clean/advanced ejecutado correctamente.")
        return jsonify({"status": "success", "result": result})
    except Exception as e:
        log_error(f"Error en /clean/advanced: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route("/clean/volumes", methods=["POST"])
def clean_volumes():
    """Limpia los volúmenes no utilizados."""
    try:
        result = cleaner.volume_clean()
        log_info("Endpoint /clean/volumes ejecutado correctamente.")
        return jsonify({"status": "success", "result": result})
    except Exception as e:
        log_error(f"Error en /clean/volumes: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route("/disk", methods=["GET"])
def show_disk():
    """Muestra el uso de disco de Docker."""
    try:
        result = cleaner.show_disk()
        log_info("Endpoint /disk ejecutado correctamente.")
        return jsonify({"status": "success", "result": result})
    except Exception as e:
        log_error(f"Error en /disk: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    # Configuración dinámica del host y puerto
    import os
    host = os.getenv("FLASK_HOST", "0.0.0.0")
    port = int(os.getenv("FLASK_PORT", 5000))
    debug = os.getenv("FLASK_DEBUG", "false").lower() == "true"

    app.run(host=host, port=port, debug=debug)
