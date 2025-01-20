from nba_api.stats.static import teams, players
from nba_api.stats.endpoints import commonplayerinfo, teamgamelog, playergamelog
from nba_api.stats.library.parameters import Season

class NBAApi:
    def __init__(self):
        """Initialize the NBAApi class."""
        self.teams = teams.get_teams()
        self.players = players.get_players()

    def get_team_id(self, team_name):
        """Get the team ID for a given team name."""
        for team in self.teams:
            if team_name.lower() in team['full_name'].lower():
                return team['id']
        raise ValueError(f"Team '{team_name}' not found.")

    def get_player_id(self, player_name):
        """Get the player ID for a given player name."""
        for player in self.players:
            if player_name.lower() in player['full_name'].lower():
                return player['id']
        raise ValueError(f"Player '{player_name}' not found.")

    def get_player_info(self, player_name):
        """Get detailed information about a player."""
        player_id = self.get_player_id(player_name)
        player_info = commonplayerinfo.CommonPlayerInfo(player_id=player_id).get_normalized_dict()
        return player_info

    def get_team_games(self, team_name, season="2023-24"):
        """Get game logs for a specific team in a given season."""
        team_id = self.get_team_id(team_name)
        games = teamgamelog.TeamGameLog(team_id=team_id, season=season).get_normalized_dict()
        return games

    def get_player_games(self, player_name, season="2023-24"):
        """Get game logs for a specific player in a given season."""
        player_id = self.get_player_id(player_name)
        games = playergamelog.PlayerGameLog(player_id=player_id, season=season).get_normalized_dict()
        return games

    def list_teams(self):
        """List all NBA teams."""
        return [team['full_name'] for team in self.teams]

    def list_players(self, team_name=None):
        """List all players, optionally filtered by team."""
        if team_name:
            team_id = self.get_team_id(team_name)
            return [player['full_name'] for player in self.players if player.get('team_id') == team_id]
        return [player['full_name'] for player in self.players]