# In-Memory Transactional Key-Value Database

This project implements a simple in-memory key-value database with transaction support.

Keys are strings and values are integers. The database supports the following operations:

- `begin_transaction()`
- `put(key, val)`
- `get(key)`
- `commit()`
- `rollback()`

The behavior follows the assignment specification:
- `put()` can only be called when a transaction is in progress; otherwise an error is raised.
- `get()` can be called at any time, but it only sees committed values from the main store.
- Only one transaction may exist at a time.
- `commit()` applies all changes made in the current transaction to the main state.
- `rollback()` discards all changes made in the current transaction.

## How to Run

1. Make sure you have Python 3 installed.
2. Open this project in PyCharm (or any terminal).
3. Run the example scenario:

```bash
python main.py
```

## Suggestions for improving this assignment in the future
To make this assignment more suitable as an official assignment in the future, a starter skeleton (interface and empty method definitions) could be provided so that students can focus on implementing the transaction logic rather than boilerplate setup. An automatic test suite could also be distributed so that students can easily validate their solutions and graders can grade more consistently. Finally, the assignment could be extended with optional features such as nested transactions or allowing `get()` to read uncommitted values, which would help students explore different transaction models.