from models.database import execute_query, execute_one


def create_category(name, icon=""):
    query = """
    INSERT INTO categories (name, icon)
    VALUES (?, ?)
    """

    execute_query(
        query,
        (name, icon)
    )


def get_categories():
    query = """
    SELECT *
    FROM categories
    WHERE active = 1
    ORDER BY id
    """

    return execute_query(query)


def get_category(category_id):
    query = """
    SELECT *
    FROM categories
    WHERE id = ?
    """

    return execute_one(
        query,
        (category_id,)
    )


def deactivate_category(category_id):
    query = """
    UPDATE categories
    SET active = 0
    WHERE id = ?
    """

    execute_query(
        query,
        (category_id,)
    )
