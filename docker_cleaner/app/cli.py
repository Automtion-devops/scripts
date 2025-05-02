from rich.console import Console
from rich.prompt import Prompt, Confirm
from app import cleaner
from app.utils import ensure_docker_or_exit
from app.utils import log_info

log_info("Usuario ejecutó limpieza avanzada desde TUI.")
ensure_docker_or_exit()

console = Console()

def main():
    while True:
        console.print("\n[bold cyan]Menú Docker Cleaner[/bold cyan]")
        console.print("1. Ver estado\n2. Limpieza básica\n3. Limpieza avanzada\n4. Limpiar volúmenes\n5. Ver uso disco\n0. Salir")
        choice = Prompt.ask("Opción", choices=["0", "1", "2", "3", "4", "5"])
        match choice:
            case "1": print(cleaner.show_status())
            case "2": print(cleaner.basic_clean())
            case "3": print(cleaner.advanced_clean())
            case "4": print(cleaner.volume_clean())
            case "5": print(cleaner.show_disk())
            case "0": break
