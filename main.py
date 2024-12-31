from micropython import const
from ntptime import settime
from time import sleep
from presto import Presto
from picovector import ANTIALIAS_FAST, PicoVector, Transform
from lib.currency import get_exchange_rate
from lib.crypto import get_coin_price


BASE_CURRENCY: str = "USD"
TARGET_CURRENCY: str = "CHF"
CRYPTO: dict = {
    "Bitcoin": "BTC",
    "Ethereum": "ETH",
    "Cardano": "ADA",
    "Tezos": "XTZ",
    "Polkadot": "DOT",
    "Solana": "SOL",
    "Dogecoin": "DOGE",
    "Litecoin": "LTC",
    "Uniswap": "UNI",
    "XRP": "XRP"
}
DELAY: int = const(10)
FONT_SIZE: int = const(20)


def get_crypto_prices() -> dict:
    """
    Fetches current cryptocurrency prices converted to the target currency.

    :return: A dictionary containing crypto symbols and prices.
    :rtype: dict
    """
    exchange_rate = get_exchange_rate(BASE_CURRENCY, TARGET_CURRENCY)
    prices = {symbol: round(float(get_coin_price(name) * exchange_rate), 2) for name, symbol in CRYPTO.items()}

    return prices


if __name__ == "__main__":
    presto = Presto()
    display = presto.display
    width, height = display.get_bounds()

    presto.connect()
    settime()

    transform = Transform()

    vector = PicoVector(display)
    vector.set_antialiasing(ANTIALIAS_FAST)
    vector.set_font("fonts/Roboto-Medium.af", FONT_SIZE)
    vector.set_transform(transform)

    black = display.create_pen(0, 0, 0)
    white = display.create_pen(200, 200, 200)
    red = display.create_pen(255, 0, 0)
    green = display.create_pen(0, 255, 0)

    previous_prices = {}

    print("[INFO] Starting...")

    while True:
        display.set_pen(black)
        display.clear()

        crypto_prices = get_crypto_prices()
        i = 10

        for symbol, price in crypto_prices.items():
            information = f"{symbol}: {price} {TARGET_CURRENCY}"

            if symbol not in previous_prices:
                color = white
            else:
                old_price = previous_prices[symbol]
                if price < old_price:
                    color = red
                elif price > old_price:
                    color = green
                else:
                    color = white

            previous_prices[symbol] = price
            display.set_pen(color)

            i += FONT_SIZE
            vector.text(information, 10, i)

        presto.update()

        sleep(DELAY)
