from replay.engine import ReplayEngine
from replay.loader import load_data

class MarketAPI:

    def __init__(self, symbol):

        self.symbol = symbol

        snapshot, events = load_data(symbol)

        self.engine = ReplayEngine(snapshot, events)

    def stream_book(self):

        return self.engine.run()

    def get_latest_book(self):

        for book in self.engine.run():
            pass

        return book
