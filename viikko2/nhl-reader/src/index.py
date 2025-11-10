from player_reader import PlayerReader
from player_stats import PlayerStats
from rich.console import Console
from rich.table import Table

def main():
    console = Console()

    console.print("[bold cyan]Welcome to NHL Stats![/bold cyan]")

    season = input("Enter season (e.g. 2024-25): ").strip()
    nationality = input("Enter nationality (e.g. FIN): ").strip().upper()

    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"

    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality(nationality)

    console.print(f"\n[bold yellow]Players from {nationality} ({season})[/bold yellow]\n")

    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Name", style="cyan", justify="left")
    table.add_column("Team", style="green", justify="center")
    table.add_column("Goals", justify="right")
    table.add_column("Assists", justify="right")
    table.add_column("Points", justify="right", style="bold")

    for player in players:
        table.add_row(
            player.name,
            player.team,
            str(player.goals),
            str(player.assists),
            str(player.points())
        )

    console.print(table)

if __name__ == "__main__":
    main()
