import pandas as pd

def transform_matches(df):
    print("🛠️ Transforming Match data...")
    # 1. Goal Difference
    df['goal_difference'] = df['home_goals'] - df['away_goals']
    
    # 2. Total Goals
    df['total_goals'] = df['home_goals'] + df['away_goals']
    
    # 3. Identify if Milan played at Home
    df['is_home'] = df['home_team'] == "AC Milan"
    
    # 4. Milan specific goals (Logic: if home, take home goals, else take away goals)
    df['milan_goals'] = df.apply(lambda x: x['home_goals'] if x['is_home'] else x['away_goals'], axis=1)
    df['milan_conceded'] = df.apply(lambda x: x['away_goals'] if x['is_home'] else x['home_goals'], axis=1)
    
    return df

def transform_players(df):
    print("🛠️ Transforming Player data...")
    # 1. Goal Contributions (Goals + Assists)
    df['goal_contributions'] = df['goals'] + df['assists']
    
    # 2. Goals per Appearance
    # We use .round(2) to keep it clean
    df['goals_per_appearance'] = (df['goals'] / df['appearances']).round(2)
    
    # 3. Contributions per Appearance
    df['contributions_per_appearance'] = (df['goal_contributions'] / df['appearances']).round(2)
    
    return df

if __name__ == "__main__":
    # Quick test to see if logic works
    from extract import extract_data
    m_df, p_df = extract_data()
    
    if m_df is not None and p_df is not None:
        m_df_clean = transform_matches(m_df)
        p_df_clean = transform_players(p_df)
        print("\nNew Match Columns:", m_df_clean[['goal_difference', 'milan_goals']].head())
        print("New Player Columns:", p_df_clean[['name', 'goal_contributions']].head())