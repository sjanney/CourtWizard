from textual.app import App
from textual.widgets import Header, Footer, Button, Static, Input, Table, TableRow, TableHeader
from textual.containers import Container, HorizontalTate
import requests

# Backend API URL
API_URL = "http://localhost:8000"

class NBAPredictorApp(App):
    CSS_PATH = "style.tcss"

    def compose(self):
        yield Header()
        yield Container(
            Static("Welcome to NBA Predictor!", id="title"),
            Horizontal(
                Input(placeholder="Enter Player ID", id="player-id-input"),
                Button("Get Player Stats", id="player-stats-btn"),
                Input(placeholder="Enter Team ID", id="team-id-input"),
                Button("Get Team Stats", id="team-stats-btn"),
                id="menu"
            ),
            Table(
                TableHeader("Stat", "Value"),
                id="output"
            ),
        )
        yield Footer()

    async def on_button_pressed(self, event: Button.Pressed):
        table = self.query_one("#output", Table)
        table.clear()

        if event.button.id == "player-stats-btn":
            player_id = self.query_one("#player-id-input", Input).value
            response = requests.get(f"{API_URL}/player-stats/{player_id}")
            stats = response.json()
            for key, value in stats[0].items():
                table.add_row(TableRow(key, str(value)))

        elif event.button.id == "team-stats-btn":
            team_id = self.query_one("#team-id-input", Input).value
            response = requests.get(f"{API_URL}/team-stats/{team_id}")
            stats = response.json()
            for key, value in stats[0].items():
                table.add_row(TableRow(key, str(value)))

if __name__ == "__main__":
    app = NBAPredictorApp()
    app.run()