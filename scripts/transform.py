"""Transform step: engineer new columns for matches and players.

Phase 3 / Step 7 requirements (kept exactly as requested):
Matches:
- GoalDifference = home_goals - away_goals
- TotalGoals = home_goals + away_goals
- IsHome = True if home_team == "AC Milan"
- AcMilanGoals = goals scored by Milan in that match
- AcMilanConceded = goals conceded by Milan in that match

Players:
- GoalContributions = goals + assists
- GoalsPerAppearance = goals / appearances
- ContributionsPerAppearance = GoalContributions / appearances

For SQL analytics, we also add snake_case aliases (e.g. goal_contributions)
so your SQL files can stay clean and conventional.
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"


def transform_matches(matches_df: pd.DataFrame) -> pd.DataFrame:
    df = matches_df.copy()

    df["GoalDifference"] = df["home_goals"] - df["away_goals"]
    df["TotalGoals"] = df["home_goals"] + df["away_goals"]

    is_home_milan = df["home_team"].eq("AC Milan")
    is_away_milan = df["away_team"].eq("AC Milan")

    df["IsHome"] = is_home_milan

    df["AcMilanGoals"] = pd.NA
    df.loc[is_home_milan, "AcMilanGoals"] = df.loc[is_home_milan, "home_goals"]
    df.loc[is_away_milan, "AcMilanGoals"] = df.loc[is_away_milan, "away_goals"]

    df["AcMilanConceded"] = pd.NA
    df.loc[is_home_milan, "AcMilanConceded"] = df.loc[is_home_milan, "away_goals"]
    df.loc[is_away_milan, "AcMilanConceded"] = df.loc[is_away_milan, "home_goals"]

    # snake_case aliases for SQL
    df["goal_difference"] = df["GoalDifference"]
    df["total_goals"] = df["TotalGoals"]
    df["is_home"] = df["IsHome"]
    df["ac_milan_goals"] = df["AcMilanGoals"]
    df["ac_milan_conceded"] = df["AcMilanConceded"]

    return df


def transform_players(players_df: pd.DataFrame) -> pd.DataFrame:
    df = players_df.copy()

    df["GoalContributions"] = df["goals"] + df["assists"]

    appearances = df["appearances"].replace({0: pd.NA})
    df["GoalsPerAppearance"] = df["goals"].div(appearances)
    df["ContributionsPerAppearance"] = df["GoalContributions"].div(appearances)

    # snake_case aliases for SQL
    df["goal_contributions"] = df["GoalContributions"]
    df["goals_per_appearance"] = df["GoalsPerAppearance"]
    df["contributions_per_appearance"] = df["ContributionsPerAppearance"]

    return df


def transform_data(
    matches_df: pd.DataFrame, players_df: pd.DataFrame
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Return (matches_transformed, players_transformed)."""

    return transform_matches(matches_df), transform_players(players_df)


def main() -> None:
    matches_df = pd.read_csv(DATA_DIR / "matches.csv")
    players_df = pd.read_csv(DATA_DIR / "players.csv")

    matches_t, players_t = transform_data(matches_df, players_df)

    print(f"Matches transformed: {matches_t.shape}")
    print(
        matches_t[
            [
                "match_id",
                "home_team",
                "away_team",
                "home_goals",
                "away_goals",
                "GoalDifference",
                "TotalGoals",
                "IsHome",
                "AcMilanGoals",
                "AcMilanConceded",
            ]
        ].head()
    )

    print()
    print(f"Players transformed: {players_t.shape}")
    print(
        players_t[
            [
                "player_id",
                "name",
                "appearances",
                "goals",
                "assists",
                "GoalContributions",
                "GoalsPerAppearance",
                "ContributionsPerAppearance",
            ]
        ].head()
    )


if __name__ == "__main__":
    main()
