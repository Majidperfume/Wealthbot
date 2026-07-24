from database.database import db


class Transaction:

    @staticmethod
    def create(template_id, project_id=None, person_id=None, note=""):
        result = db.execute(
            """
            INSERT INTO transactions
            (
                template_id,
                project_id,
                person_id,
                note
            )
            VALUES (?, ?, ?, ?)
            """,
            (
                template_id,
                project_id,
                person_id,
                note,
            ),
        )

        return result.lastrowid


    @staticmethod
    def add_entry(
        transaction_id,
        asset_id,
        amount,
        price=0,
        total_value=0
    ):
        db.execute(
            """
            INSERT INTO transaction_entries
            (
                transaction_id,
                asset_id,
                amount,
                price,
                total_value
            )
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                transaction_id,
                asset_id,
                amount,
                price,
                total_value,
            ),
        )


    @staticmethod
    def get(transaction_id):
        return db.fetchone(
            """
            SELECT *
            FROM transactions
            WHERE id = ?
            """,
            (transaction_id,),
        )


    @staticmethod
    def entries(transaction_id):
        return db.fetchall(
            """
            SELECT

                transaction_entries.*,

                assets.name AS asset_name,

                currencies.code AS currency


            FROM transaction_entries


            JOIN assets

            ON transaction_entries.asset_id = assets.id


            JOIN currencies

            ON assets.currency_id = currencies.id


            WHERE transaction_id = ?

            """,
            (transaction_id,),
        )


    @staticmethod
    def all():
        return db.fetchall(
            """
            SELECT *

            FROM transactions

            WHERE active = 1

            ORDER BY transaction_date DESC

            """
        )


    @staticmethod
    def delete(transaction_id):
        db.execute(
            """
            UPDATE transactions

            SET active = 0

            WHERE id = ?

            """,
            (transaction_id,),
        )
