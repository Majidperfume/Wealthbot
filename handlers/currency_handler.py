from services.currency_service import CurrencyService


def get_currency_trades(currency_id):
    return CurrencyService.get_trades(currency_id)


def get_average_price(trades):
    return CurrencyService.calculate_average_price(trades)


def calculate_profit(
    buy_amount,
    buy_average,
    sell_amount,
    sell_average
):
    return CurrencyService.calculate_profit(
        buy_amount,
        buy_average,
        sell_amount,
        sell_average,
    )
