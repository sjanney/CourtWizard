import pandas as pd

class NBADataPreprocessor:
    """Preprocesses NBA data for machine learning."""

    @staticmethod
    def clean_game_logs(game_logs):
        """
        Cleans and preprocesses game logs.
        :param game_logs: Raw DataFrame of game logs.
        :return: Preprocessed DataFrame.
        """
        # Drop unnecessary columns
        columns_to_drop = ["GAME_ID", "MATCHUP", "VIDEO_AVAILABLE"]
        game_logs = game_logs.drop(columns=columns_to_drop, errors="ignore")

        # Convert dates
        if "GAME_DATE" in game_logs.columns:
            game_logs["GAME_DATE"] = pd.to_datetime(game_logs["GAME_DATE"])

        # Fill missing values
        game_logs = game_logs.fillna(0)

        # Normalize numeric columns
        numeric_columns = game_logs.select_dtypes(include=["float64", "int64"]).columns
        game_logs[numeric_columns] = (game_logs[numeric_columns] - game_logs[numeric_columns].mean()) / game_logs[numeric_columns].std()

        return game_logs

    @staticmethod
    def save_preprocessed_data(df, filepath):
        """Save preprocessed data to CSV."""
        try:
            df.to_csv(filepath, index=False)
            print(f"Preprocessed data saved to {filepath}")
        except Exception as e:
            print(f"Error saving preprocessed data: {e}")
