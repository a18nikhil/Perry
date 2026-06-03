import pandas as pd
from config.config import DATA_DIR
from ingestion.snapshot import fetch_snapshot

def load_data(symbol):

    snapshot = fetch_snapshot(symbol)

    try:
        df = pd.read_parquet(f"{DATA_DIR}/{symbol}_events.parquet")
    except:
        df = pd.DataFrame()

    return snapshot, df.to_dict("records")
