import pandas as pd
from pathlib import Path
from config.config import DATA_DIR

class ParquetStore:

    def __init__(self):
        self.base = Path(DATA_DIR)
        self.base.mkdir(exist_ok=True)

    def write(self, events, symbol):

        df = pd.DataFrame(events)

        out = self.base / f"{symbol}_events.parquet"

        df.to_parquet(
            out,
            compression="zstd",
            index=False
        )
