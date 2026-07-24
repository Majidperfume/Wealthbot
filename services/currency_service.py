from database.database import db


class CurrencyService:

    @staticmethod
    def get_trades(currency_id):

        return db.fetchall(
            """
            SELECT

                transactions.id,
                transactions.transaction_date,
                transactions.note,

                transaction_entries.amount,
                transaction_entries.price,
                transaction_entries.total_value,

                assets.name AS asset_name


            FROM transaction_entries


            JOIN transactions

            ON transaction_entries.transaction_id =
               transactions.id


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
    def calculate_average_price(trades):

        total_amount = 0
        total_value = 0

        for trade in trades:

            amount = trade["amount"]
            value = trade["total_value"]

            total_amount += amount
            total_value += value


        if total_amount == 0:
            return 0


        return total_value / total_amount


    @staticmethod
    def calculate_profit(
        buy_amount,
        buy_average,
        sell_amount,
        sell_average
    ):

        cost = buy_amount * buy_average

        income = sell_amount * sell_average

        return income - cost
