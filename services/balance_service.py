from database.database import db


class BalanceService:

    @staticmethod
    def get_asset_balance(asset_id):

        result = db.fetchone(
            """
            SELECT
                COALESCE(SUM(amount), 0) AS balance

            FROM transaction_entries

            JOIN transactions

            ON transaction_entries.transaction_id = transactions.id

            WHERE transaction_entries.asset_id = ?

            AND transactions.active = 1

            """,
            (asset_id,),
        )

        return result["balance"]


    @staticmethod
    def get_all_balances():

        return db.fetchall(
            """
            SELECT

                assets.id,
                assets.name,

                currencies.code AS currency,

                COALESCE(
                    SUM(transaction_entries.amount),
                    0
                ) AS balance


            FROM assets


            JOIN currencies

            ON assets.currency_id = currencies.id


            LEFT JOIN transaction_entries

            ON assets.id = transaction_entries.asset_id


            LEFT JOIN transactions

            ON transaction_entries.transaction_id = transactions.id


            WHERE assets.active = 1


            GROUP BY assets.id


            ORDER BY assets.name

            """
        )
