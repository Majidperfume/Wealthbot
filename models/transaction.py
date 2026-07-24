from models.database import execute_query, execute_one


def create_transaction(
    transaction_type_id,
    description,
    transaction_date,
    category_id=None,
    person_id=None
):
    query = """
    INSERT INTO transactions
    (
        transaction_type_id,
        category_id,
        person_id,
        description,
        transaction_date
    )
    VALUES (?, ?, ?, ?, ?)
    """

    execute_query(
        query,
        (
            transaction_type_id,
            category_id,
            person_id,
            description,
            transaction_date
        )
    )


def get_transactions(limit=50):
    query = """
    SELECT *
    FROM transactions
    ORDER BY id DESC
    LIMIT ?
    """

    return execute_query(
        query,
        (limit,)
    )


def get_transaction(transaction_id):
    query = """
    SELECT *
    FROM transactions
    WHERE id = ?
    """

    return execute_one(
        query,
        (transaction_id,)
    )


def add_transaction_entry(
    transaction_id,
    amount,
    entry_type,
    account_id=None,
    currency_id=None,
    person_id=None,
    note=""
):
    query = """
    INSERT INTO transaction_entries
    (
        transaction_id,
        account_id,
        currency_id,
        person_id,
        amount,
        entry_type,
        note
    )
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """

    execute_query(
        query,
        (
            transaction_id,
            account_id,
            currency_id,
            person_id,
            amount,
            entry_type,
            note
        )
    )


def get_transaction_entries(transaction_id):
    query = """
    SELECT *
    FROM transaction_entries
    WHERE transaction_id = ?
    """

    return execute_query(
        query,
        (transaction_id,)
    )
