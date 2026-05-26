import pandas as pd
import requests
from sqlalchemy import create_engine

# =========================================
# EXTRACT
# =========================================

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

data = response.json()

df = pd.DataFrame(data)

print("\n===================================")
print("RAW API DATA")
print("===================================")
print(df.head())

# =========================================
# TRANSFORM
# =========================================

df = df[["id", "name", "email", "phone", "website"]]

# Simulated AC Milan football data
df["club"] = "AC Milan"

positions = [
    "Forward",
    "Midfielder",
    "Defender",
    "Goalkeeper",
    "Winger",
    "Striker",
    "Centre Back",
    "Full Back",
    "Attacking Midfielder",
    "Defensive Midfielder"
]

df["position"] = positions[:len(df)]

df["goals"] = [12, 7, 2, 0, 9, 15, 1, 0, 6, 3]

df["assists"] = [5, 11, 1, 0, 7, 4, 0, 2, 10, 5]

df["goal_contributions"] = df["goals"] + df["assists"]

print("\n===================================")
print("TRANSFORMED AC MILAN DATA")
print("===================================")
print(df)

# =========================================
# LOAD TO SQL DATABASE
# =========================================

engine = create_engine("sqlite:///acmilan.db")

df.to_sql(
    "ac_milan_player_stats",
    engine,
    if_exists="replace",
    index=False
)

print("\n===================================")
print("DATA SUCCESSFULLY LOADED")
print("===================================")
print("SQLite database created successfully.")

# =========================================
# EXPORT CLEAN DATA
# =========================================

df.to_csv("ac_milan_player_stats.csv", index=False)

print("\nCSV export created successfully.")