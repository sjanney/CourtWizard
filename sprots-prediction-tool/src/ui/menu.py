from rich.console import Console
from rich.table import Table

console = Console()

def main_menu():
    console.print("[bold magenta]Welcome to the Sports Prediction Tool![/bold magenta]", style="bold green")
    console.print("Select an option below:", style="bold cyan")
    table = Table(show_header=True, header_style="bold blue")
    table.add_column("Option", style="bold white")
    table.add_column("Description", style="bold white")
    table.add_row("1", "View NBA Stats")
    table.add_row("2", "Predictions for Upcoming Games")
    table.add_row("3", "Join Discord Community")
    table.add_row("4", "Exit")
    console.print(table)

    choice = input("\n[bold yellow]Enter your choice: [/bold yellow]")
    return choice


main_menu()