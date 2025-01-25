from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from supabase import create_client, Client
from nba_api.stats.endpoints import playercareerstats, teamyearbyyearstats, playergamelog
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Supabase setup
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# FastAPI app
app = FastAPI()
security = HTTPBearer()

# Dependency for JWT authentication
async def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    try:
        user = supabase.auth.get_user(credentials.credentials)
        return user
    except Exception as e:
        raise HTTPException(status_code=401, detail="Invalid token")

# Endpoint to fetch player career stats
@app.get("/player-stats/{player_id}")
async def get_player_stats(player_id: str, user: dict = Depends(get_current_user)):
    try:
        player_stats = playercareerstats.PlayerCareerStats(player_id=player_id)
        return player_stats.get_data_frames()[0].to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Endpoint to fetch team year-by-year stats
@app.get("/team-stats/{team_id}")
async def get_team_stats(team_id: str, user: dict = Depends(get_current_user)):
    try:
        team_stats = teamyearbyyearstats.TeamYearByYearStats(team_id=team_id)
        return team_stats.get_data_frames()[0].to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Endpoint to fetch player game logs
@app.get("/player-gamelog/{player_id}/{season}")
async def get_player_gamelog(player_id: str, season: str, user: dict = Depends(get_current_user)):
    try:
        gamelog = playergamelog.PlayerGameLog(player_id=player_id, season=season)
        return gamelog.get_data_frames()[0].to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Run the app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)