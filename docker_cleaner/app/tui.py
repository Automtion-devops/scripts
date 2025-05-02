from textual.app import App
from textual.widgets import Button, Header, Footer
from app import cleaner
from app.utils import ensure_docker_or_exit
from app.utils import log_info

log_info("Usuario ejecutó limpieza avanzada desde TUI.")
ensure_docker_or_exit()

class DockerCleanerApp(App):
    def compose(self):
        yield Header()
        for label, cmd in [("Ver estado", cleaner.show_status),
                           ("Limpieza básica", cleaner.basic_clean),
                           ("Limpieza avanzada", cleaner.advanced_clean),
                           ("Volúmenes", cleaner.volume_clean),
                           ("Uso disco", cleaner.show_disk),
                           ("Salir", lambda: exit())]:
            yield Button(label, on_click=lambda e, c=cmd: print(c()))
        yield Footer()

if __name__ == "__main__":
    DockerCleanerApp().run()
