from models.database import execute_query, execute_one


def create_transaction_type(name, icon=""):
    query = """
    INSERT INTO transaction_types (name, icon)
    VALUES (?, ?)
    """

    execute_query(
        query,
        (name, icon)
    )


def get_transaction_types():
    query = """
    SELECT *
    FROM transaction_types
    WHERE active = 1
    ORDER BY id
    """

    return execute_query(query)


def get_transaction_type(transaction_type_id):
    query = """
    SELECT *
    FROM transaction_types
    WHERE id = ?
    """

    return execute_one(
        query,
        (transaction_type_id,)
    )


def deactivate_transaction_type(transaction_type_id):
    query = """
    UPDATE transaction_types
    SET active = 0
    WHERE id = ?
    """

    execute_query(
        query,
        (transaction_type_id,)
    )
