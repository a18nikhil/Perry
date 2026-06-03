import asyncio
import json
from ingestion.snapshot import fetch_snapshot
from ingestion.collector import stream
from core.validator import Validator
from core.orderbook import OrderBook
from storage.parquet_store import ParquetStore
from utils.logger import get_logger

logger = get_logger()

store = ParquetStore()

async def run():

    symbol = "btcusdt"

    snapshot = fetch_snapshot(symbol)

    book = OrderBook()
    validator = Validator()

    validator.init(snapshot["last_update_id"])

    buffer = []

    async for msg in stream():

        U = msg.get("U")
        u = msg.get("u")

        if not validator.validate(U, u):
            logger.warning("GAP detected")
            continue

        buffer.append({
            "symbol": symbol,
            "U": U,
            "u": u,
            "bids": msg.get("b", []),
            "asks": msg.get("a", [])
        })

        book.apply(msg.get("b", []), msg.get("a", []))

        if len(buffer) > 500:
            store.write(buffer, symbol)
            logger.info(f"Saved {len(buffer)} events")
            buffer = []

if __name__ == "__main__":
    asyncio.run(run())
