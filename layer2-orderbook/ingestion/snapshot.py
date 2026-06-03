import requests
from config.config import REST_URL

def fetch_snapshot(symbol: str, limit: int = 1000):

    r = requests.get(
        REST_URL,
        params={
            "symbol": symbol.upper(),
            "limit": limit
        },
        timeout=10
    )

    data = r.json()

    return {
        "last_update_id": data["lastUpdateId"],
        "bids": data["bids"],
        "asks": data["asks"]
    }
