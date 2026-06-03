class Validator:

    def __init__(self):
        self.last_u = None

    def init(self, snapshot_id):
        self.last_u = snapshot_id

    def validate(self, U, u):

        if self.last_u is None:
            self.last_u = u
            return True

        # gap detection
        if U > self.last_u + 1:
            return False

        self.last_u = u
        return True
