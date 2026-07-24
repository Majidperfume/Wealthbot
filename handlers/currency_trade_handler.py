from services.currency_trade_service import CurrencyTradeService


def buy_currency(data):

    return CurrencyTradeService.buy_currency(
        template_id=data["template_id"],
        cash_asset_id=data["cash_asset_id"],
        currency_asset_id=data["currency_asset_id"],
        amount=data["amount"],
        price=data["price"],
        note=data.get("note", ""),
    )


def sell_currency(data):

    return CurrencyTradeService.sell_currency(
        template_id=data["template_id"],
        currency_asset_id=data["currency_asset_id"],
        cash_asset_id=data["cash_asset_id"],
        amount=data["amount"],
        price=data["price"],
        note=data.get("note", ""),
    )
