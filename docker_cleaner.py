#!/usr/bin/env python3
import subprocess
import sys
from rich.console import Console
from rich.prompt import Prompt, Confirm
from rich.table import Table
from rich import print

console = Console()

def run_command(command):
    try:
        result = subprocess.run(command, shell=True, text=True, capture_output=True)
        return result.stdout if result.returncode == 0 else result.stderr
    except Exception as e:
        return f"[red]Error ejecutando el comando:[/red] {e}"

def check_docker():
    output = run_command("docker info")
    if "Cannot connect to the Docker daemon" in output or "permission denied" in output.lower():
        console.print("[red]Docker no está corriendo o no tienes permisos suficientes.[/red]")
        sys.exit(1)

def show_status():
    console.rule("[bold yellow]Estado de Docker[/bold yellow]")
    print("[cyan]Contenedores:[/cyan]")
    print(run_command("docker ps -a"))

    print("[cyan]Imágenes:[/cyan]")
    print(run_command("docker images"))

    print("[cyan]Volúmenes:[/cyan]")
    print(run_command("docker volume ls"))

def basic_prune():
    if Confirm.ask("[yellow]¿Seguro que deseas realizar limpieza básica?[/yellow]"):
        print(run_command("docker system prune -f"))
        print("[green]¡Limpieza básica completada![/green]")

def advanced_prune():
    console.print("[red]¡CUIDADO! Esto eliminará todas las imágenes no usadas, incluso las que no son 'dangling'.[/red]")
    if Confirm.ask("[yellow]¿Deseas continuar con la limpieza avanzada?[/yellow]"):
        print(run_command("docker system prune -a -f"))
        print("[green]¡Limpieza avanzada completada![/green]")

def volume_prune():
    if Confirm.ask("[yellow]¿Eliminar volúmenes no utilizados?[/yellow]"):
        print(run_command("docker volume prune -f"))
        print("[green]Volúmenes eliminados.[/green]")

def show_disk_usage():
    console.rule("[bold cyan]Uso de Disco[/bold cyan]")
    print(run_command("docker system df"))

def main_menu():
    check_docker()

    while True:
        console.rule("[bold blue]Menú de Limpieza Docker[/bold blue]")
        table = Table(title="Opciones disponibles", show_lines=True)
        table.add_column("Opción", justify="center")
        table.add_column("Acción")
        table.add_row("1", "Ver estado actual")
        table.add_row("2", "Limpieza básica")
        table.add_row("3", "Limpieza avanzada (-a)")
        table.add_row("4", "Limpiar volúmenes no usados")
        table.add_row("5", "Ver uso de disco")
        table.add_row("0", "Salir")
        console.print(table)

        choice = Prompt.ask("[bold green]Elige una opción[/bold green]", choices=["0", "1", "2", "3", "4", "5"])
        match choice:
            case "1": show_status()
            case "2": basic_prune()
            case "3": advanced_prune()
            case "4": volume_prune()
            case "5": show_disk_usage()
            case "0":
                console.print("[cyan]¡Hasta luego, DevOps ilustre![/cyan] 👋")
                sys.exit()

if __name__ == "__main__":
    main_menu()
