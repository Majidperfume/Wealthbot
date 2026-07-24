from models.database import execute_query, execute_one


def create_person(name, phone="", note=""):
    query = """
    INSERT INTO persons (name, phone, note)
    VALUES (?, ?, ?)
    """

    execute_query(
        query,
        (name, phone, note)
    )


def get_persons():
    query = """
    SELECT *
    FROM persons
    WHERE active = 1
    ORDER BY id
    """

    return execute_query(query)


def get_person(person_id):
    query = """
    SELECT *
    FROM persons
    WHERE id = ?
    """

    return execute_one(
        query,
        (person_id,)
    )


def deactivate_person(person_id):
    query = """
    UPDATE persons
    SET active = 0
    WHERE id = ?
    """

    execute_query(
        query,
        (person_id,)
    )
