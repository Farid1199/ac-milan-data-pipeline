import pandas as pd
from sqlalchemy import create_engine
import os

def load_data(matches_df, players_df):
    """
    Saves the transformed data into a SQLite database 
    and exports clean CSV files.
    """
    
    # 1. SETUP DIRECTORIES
    # Ensure the database and exports folders exist so the code doesn't crash
    os.makedirs('database', exist_ok=True)
    os.makedirs('exports', exist_ok=True)

    print("💾 Starting Load Phase...")

    # 2. CREATE DATABASE CONNECTION
    # 'sqlite:///...' tells SQLAlchemy to create a local database file
    engine = create_engine('sqlite:///database/ac_milan.db')

    # 3. LOAD TO SQLITE DATABASE
    # 'if_exists=replace' means if the table is already there, overwrite it with fresh data
    # 'index=False' prevents pandas from adding an extra column for the row numbers
    matches_df.to_sql('ac_milan_matches', engine, if_exists='replace', index=False)
    players_df.to_sql('ac_milan_players', engine, if_exists='replace', index=False)
    print("✅ Data successfully loaded into SQLite (database/ac_milan.db)")

    # 4. EXPORT TO CLEAN CSV FILES
    # This is for sharing data easily with people who don't use SQL
    matches_df.to_csv('exports/clean_matches.csv', index=False)
    players_df.to_csv('exports/clean_players.csv', index=False)
    print("✅ Clean CSVs exported to the /exports folder")

    return True

if __name__ == "__main__":
    print("This script is usually run via the master pipeline, not alone.")