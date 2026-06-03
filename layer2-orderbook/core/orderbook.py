class OrderBook:

    def __init__(self):
        self.bids = {}
        self.asks = {}

    def apply(self, bids, asks):

        for p, q in bids:
            p = float(p)
            q = float(q)

            if q == 0:
                self.bids.pop(p, None)
            else:
                self.bids[p] = q

        for p, q in asks:
            p = float(p)
            q = float(q)

            if q == 0:
                self.asks.pop(p, None)
            else:
                self.asks[p] = q
