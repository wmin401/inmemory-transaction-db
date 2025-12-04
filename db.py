class TransactionError(Exception):
    pass


class InMemoryDB:
    def __init__(self):
        self.main_store = {}
        self.tx_store = None
        self.in_transaction = False

    def begin_transaction(self):
        if self.in_transaction:
            raise TransactionError("A transaction is already in progress")
        self.in_transaction = True
        self.tx_store = {}

    def put(self, key: str, val: int):
        if not self.in_transaction:
            raise TransactionError("No transaction in progress")
        self.tx_store[key] = val

    def get(self, key: str):
        return self.main_store.get(key, None)

    def commit(self):
        if not self.in_transaction:
            raise TransactionError("No transaction in progress")

        for k, v in self.tx_store.items():
            self.main_store[k] = v

        self.tx_store = None
        self.in_transaction = False

    def rollback(self):
        if not self.in_transaction:
            raise TransactionError("No transaction in progress")

        self.tx_store = None
        self.in_transaction = False