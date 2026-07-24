from models.database import execute_query, execute_one


def create_account(name, account_type="bank"):
    query = """
    INSERT INTO accounts (name, type)
    VALUES (?, ?)
    """

    execute_query(
        query,
        (name, account_type)
    )


def get_accounts():
    query = """
    SELECT *
    FROM accounts
    WHERE active = 1
    ORDER BY id
    """

    return execute_query(query)


def get_account(account_id):
    query = """
    SELECT *
    FROM accounts
    WHERE id = ?
    """

    return execute_one(
        query,
        (account_id,)
    )


def deactivate_account(account_id):
    query = """
    UPDATE accounts
    SET active = 0
    WHERE id = ?
    """

    execute_query(
        query,
        (account_id,)
    )
