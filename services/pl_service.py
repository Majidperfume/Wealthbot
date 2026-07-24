from database.database import db


class PLService:

    @staticmethod
    def get_currency_trades(currency_id):

        return db.fetchall(
            """
            SELECT

                transactions.id,
                transactions.transaction_date,
                transactions.note,

                transaction_entries.amount,

                assets.name AS asset_name

            FROM transactions


            JOIN transaction_entries

            ON transactions.id =
            transaction_entries.transaction_id


            JOIN assets

            ON transaction_entries.asset_id =
            assets.id


            WHERE assets.currency_id = ?

            AND transactions.active = 1


            ORDER BY transactions.transaction_date

            """,
            (currency_id,),
        )


    @staticmethod
    def calculate_average_buy(buys):

        total_amount = 0
        total_cost = 0

        for item in buys:
            total_amount += item["amount"]
            total_cost += item["amount"] * item["price"]

        if total_amount == 0:
            return 0

        return total_cost / total_amount


    @staticmethod
    def calculate_average_sell(sells):

        total_amount = 0
        total_income = 0

        for item in sells:
            total_amount += item["amount"]
            total_income += item["amount"] * item["price"]

        if total_amount == 0:
            return 0

        return total_income / total_amount
