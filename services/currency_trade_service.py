from services.transaction_service import TransactionService


class CurrencyTradeService:

    @staticmethod
    def buy_currency(
        template_id,
        cash_asset_id,
        currency_asset_id,
        amount,
        price,
        note=""
    ):

        total = amount * price

        entries = [

            {
                "asset_id": cash_asset_id,
                "amount": -total,
                "price": price,
                "total_value": total,
            },

            {
                "asset_id": currency_asset_id,
                "amount": amount,
                "price": price,
                "total_value": total,
            }

        ]


        return TransactionService.create_transaction(
            template_id=template_id,
            entries=entries,
            note=note,
        )


    @staticmethod
    def sell_currency(
        template_id,
        currency_asset_id,
        cash_asset_id,
        amount,
        price,
        note=""
    ):

        total = amount * price


        entries = [

            {
                "asset_id": currency_asset_id,
                "amount": -amount,
                "price": price,
                "total_value": total,
            },

            {
                "asset_id": cash_asset_id,
                "amount": total,
                "price": price,
                "total_value": total,
            }

        ]


        return TransactionService.create_transaction(
            template_id=template_id,
            entries=entries,
            note=note,
        )
