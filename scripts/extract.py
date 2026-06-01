import pandas as pd
import os

def extract_data():
    """Loads CSV files from the data folder."""
    
    # Define file paths
    # Note: We use paths relative to the project root
    matches_file = "data/matches.csv"
    players_file = "data/players.csv"

    print("🚀 Starting Extraction Phase...")

    # Load matches
    if os.path.exists(matches_file):
        matches_df = pd.read_csv(matches_file)
        print(f"✅ Extracted matches.csv: {matches_df.shape[0]} rows found.")
    else:
        print(f"❌ Error: {matches_file} not found.")
        matches_df = None

    # Load players
    if os.path.exists(players_file):
        players_df = pd.read_csv(players_file)
        print(f"✅ Extracted players.csv: {players_df.shape[0]} rows found.")
    else:
        print(f"❌ Error: {players_file} not found.")
        players_df = None

    return matches_df, players_df

if __name__ == "__main__":
    # This part only runs if you execute this file directly
    m_df, p_df = extract_data()
    if m_df is not None:
        print("\nMatches Preview:")
        print(m_df.head())
    if p_df is not None:
        print("\nPlayers Preview:")
        print(p_df.head())