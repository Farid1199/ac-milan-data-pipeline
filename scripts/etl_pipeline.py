import time
# Import the functions we wrote in the other files
from extract import extract_data
from transform import transform_matches, transform_players
from load import load_data

def run_pipeline():
    start_time = time.time()
    print("--- AC MILAN ETL PIPELINE STARTING ---")

    # STAGE 1: EXTRACT
    raw_matches, raw_players = extract_data()

    if raw_matches is None or raw_players is None:
        print("❌ Pipeline failed during extraction.")
        return

    # STAGE 2: TRANSFORM
    clean_matches = transform_matches(raw_matches)
    clean_players = transform_players(raw_players)

    # STAGE 3: LOAD
    success = load_data(clean_matches, clean_players)

    if success:
        end_time = time.time()
        duration = round(end_time - start_time, 2)
        print(f"--- ✅ PIPELINE COMPLETE IN {duration} SECONDS ---")

if __name__ == "__main__":
    run_pipeline()