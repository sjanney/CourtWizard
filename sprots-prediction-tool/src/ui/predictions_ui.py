from rich.console import Console

console = Console()

def show_predictions(predictions):
    console.print("[bold magenta]Game Predictions[/bold magenta]")
    for game in predictions:
        confidence_color = "green" if game["confidence"] > 0.75 else "yellow"
        console.print(f"[bold {confidence_color}]{game['team1']} vs {game['team2']}[/bold {confidence_color}]")
        console.print(f"Winner: {game['predicted_winner']} (Confidence: {game['confidence']:.2f})\n")
