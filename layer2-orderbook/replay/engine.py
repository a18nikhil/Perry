from core.orderbook import OrderBook
from core.validator import Validator

class ReplayEngine:

    def __init__(self, snapshot, events):

        self.snapshot = snapshot
        self.events = events

        self.book = OrderBook()
        self.validator = Validator()

    def run(self):

        # init book from snapshot
        self.book.apply(
            self.snapshot["bids"],
            self.snapshot["asks"]
        )

        self.validator.init(
            self.snapshot["last_update_id"]
        )

        yield self.book

        for e in self.events:

            U = e.get("U", 0)
            u = e.get("u", 0)

            if not self.validator.validate(U, u):
                continue

            self.book.apply(
                e.get("bids", []),
                e.get("asks", [])
            )

            yield self.book
