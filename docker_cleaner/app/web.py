from flask import Flask, jsonify
from app import cleaner
from app.utils import ensure_docker_or_exit
from app.utils import log_info

ensure_docker_or_exit()
log_info("Usuario ejecutó limpieza avanzada desde TUI.")


app = Flask(__name__)

@app.route("/status")      # GET /status
def status(): return jsonify(result=cleaner.show_status())

@app.route("/clean/basic") # GET /clean/basic
def clean_basic(): return jsonify(result=cleaner.basic_clean())

# ... lo mismo para advanced, volume, disk

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
