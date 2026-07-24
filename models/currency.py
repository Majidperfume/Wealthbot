from models.database import execute_query, execute_one


def create_currency(name, code, symbol=""):
    query = """
    INSERT INTO currencies (name, code, symbol)
    VALUES (?, ?, ?)
    """

    execute_query(
        query,
        (name, code, symbol)
    )


def get_currencies():
    query = """
    SELECT *
    FROM currencies
    WHERE active = 1
    ORDER BY id
    """

    return execute_query(query)


def get_currency(currency_id):
    query = """
    SELECT *
    FROM currencies
    WHERE id = ?
    """

    return execute_one(
        query,
        (currency_id,)
    )


def deactivate_currency(currency_id):
    query = """
    UPDATE currencies
    SET active = 0
    WHERE id = ?
    """

    execute_query(
        query,
        (currency_id,)
    )
