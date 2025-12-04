from db import InMemoryDB, TransactionError

def test_scenario():
    db = InMemoryDB()

    print("get(A) =", db.get("A"))  # None

    try:
        db.put("A", 5)
    except TransactionError as e:
        print("Error (put without tx):", e)

    db.begin_transaction()
    db.put("A", 5)
    print("get(A) during tx =", db.get("A"))

    db.put("A", 6)
    db.commit()
    print("get(A) after commit =", db.get("A"))

    try:
        db.commit()
    except TransactionError as e:
        print("Error (commit without tx):", e)

    try:
        db.rollback()
    except TransactionError as e:
        print("Error (rollback without tx):", e)

    print("get(B) =", db.get("B"))

    db.begin_transaction()
    db.put("B", 10)
    db.rollback()
    print("get(B) after rollback =", db.get("B"))


if __name__ == "__main__":
    test_scenario()