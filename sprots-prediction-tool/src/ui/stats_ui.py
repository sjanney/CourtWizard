from rich.console import Console
from rich.table import Table

console = Console()

def display_nba_stats(stats):
    table = Table(title="NBA Player Stats", header_style="bold magenta")
    table.add_column("Player", justify="left", style="cyan", no_wrap=True)
    table.add_column("Points", justify="right", style="green")
    table.add_column("Rebounds", justify="right", style="green")
    table.add_column("Assists", justify="right", style="green")

    for player in stats:
        table.add_row(player["name"], str(player["points"]), str(player["rebounds"]), str(player["assists"]))

    console.print(table)
