from rich.console import Console
from rich.prompt import Prompt, Confirm
from app import cleaner
from app.utils import ensure_docker_or_exit, log_info, log_error

# Asegúrate de que Docker esté disponible
log_info("Usuario inició Docker Cleaner en modo CLI.")
ensure_docker_or_exit()

console = Console()

def main():
    while True:
        try:
            console.print("\n[bold cyan]Menú Docker Cleaner[/bold cyan]")
            console.print("1. Ver estado\n2. Limpieza básica\n3. Limpieza avanzada\n4. Limpiar volúmenes\n5. Ver uso disco\n0. Salir")
            choice = Prompt.ask("Opción", choices=["0", "1", "2", "3", "4", "5"])
            
            match choice:
                case "1":
                    log_info("Usuario seleccionó 'Ver estado'.")
                    console.print(cleaner.show_status())
                case "2":
                    log_info("Usuario seleccionó 'Limpieza básica'.")
                    if Confirm.ask("[yellow]¿Seguro que deseas realizar limpieza básica?[/yellow]"):
                        console.print(cleaner.basic_clean())
                        console.print("[green]¡Limpieza básica completada![/green]")
                case "3":
                    log_info("Usuario seleccionó 'Limpieza avanzada'.")
                    console.print("[red]¡CUIDADO! Esto eliminará todas las imágenes no usadas, incluso las que no son 'dangling'.[/red]")
                    if Confirm.ask("[yellow]¿Deseas continuar con la limpieza avanzada?[/yellow]"):
                        console.print(cleaner.advanced_clean())
                        console.print("[green]¡Limpieza avanzada completada![/green]")
                case "4":
                    log_info("Usuario seleccionó 'Limpiar volúmenes'.")
                    if Confirm.ask("[yellow]¿Eliminar volúmenes no utilizados?[/yellow]"):
                        console.print(cleaner.volume_clean())
                        console.print("[green]Volúmenes eliminados.[/green]")
                case "5":
                    log_info("Usuario seleccionó 'Ver uso de disco'.")
                    console.print(cleaner.show_disk())
                case "0":
                    log_info("Usuario salió del programa.")
                    console.print("[cyan]¡Hasta luego, DevOps ilustre![/cyan] 👋")
                    break
        except Exception as e:
            log_error(f"Error en el menú CLI: {e}")
            console.print(f"[red]Ocurrió un error: {e}[/red]")

if __name__ == "__main__":
    main()
