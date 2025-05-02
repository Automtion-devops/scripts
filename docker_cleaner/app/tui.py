import unicodedata
from textual.app import App, ComposeResult
from textual.widgets import Button, Header, Footer, Static
from app import cleaner
from app.utils import ensure_docker_or_exit
from app.utils import log_info

log_info("Usuario ejecutó limpieza avanzada desde TUI.")
ensure_docker_or_exit()

def normalize_id(label: str) -> str:
    """Normaliza un texto para usarlo como identificador válido."""
    # Elimina acentos y caracteres especiales
    normalized = unicodedata.normalize('NFKD', label).encode('ascii', 'ignore').decode('ascii')
    # Reemplaza espacios por guiones bajos y convierte a minúsculas
    return normalized.lower().replace(" ", "_")

class DockerCleanerApp(App):
    def compose(self) -> ComposeResult:
        yield Header()
        self.result_widget = Static("Resultados aparecerán aquí.")
        yield self.result_widget
        for label in ["Ver estado", "Limpieza básica", "Limpieza avanzada", "Volúmenes", "Uso disco", "Salir"]:
            yield Button(label, id=normalize_id(label))
        yield Footer()

    async def on_button_pressed(self, event: Button.Pressed) -> None:
        button_id = event.button.id
        try:
            if button_id == "ver_estado":
                result = cleaner.show_status()
            elif button_id == "limpieza_basica":
                result = cleaner.basic_clean()
            elif button_id == "limpieza_avanzada":
                result = cleaner.advanced_clean()
            elif button_id == "volumenes":
                result = cleaner.volume_clean()
            elif button_id == "uso_disco":
                result = cleaner.show_disk()
            elif button_id == "salir":
                self.exit()
                return
            else:
                result = "Acción no reconocida."

            # Actualiza el widget con el resultado
            self.result_widget.update(result.strip() or "No se obtuvo ningún resultado.")
        except Exception as e:
            self.result_widget.update(f"[red]Error:[/red] {e}")

if __name__ == "__main__":
    DockerCleanerApp().run()
