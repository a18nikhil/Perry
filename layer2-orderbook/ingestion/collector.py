import asyncio
import json
import websockets
from config.config import WS_URL, SYMBOL
from ingestion.snapshot import fetch_snapshot

def build_ws_url(symbol):
    return f"{WS_URL}/{symbol}@depth@100ms"

async def stream():

    snapshot = fetch_snapshot(SYMBOL)
    url = build_ws_url(SYMBOL)

    async with websockets.connect(url, ping_interval=20) as ws:

        async for msg in ws:

            yield json.loads(msg)
