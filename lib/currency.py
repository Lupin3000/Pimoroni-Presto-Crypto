from time import localtime
from requests import get


CODES: tuple = (
    "AUD", "BGN", "BRL", "CAD", "CHF", "CNY", "DKK", "EUR", "GBP", "HKD", "HUF", "IDR", "ILS",
    "INR", "ISK", "JPY", "KRW", "MXN", "MYR", "NOK", "NZD", "PHP", "PLN", "RON", "SEK", "SGD",
    "THB", "TRY", "USD", "ZAR"
)


def get_exchange_rate(base: str, target: str) -> float:
    """
    Fetches the exchange rate between two currencies for the current date from the Frankfurter API.

    :param base: The base currency code (e.g., 'USD', 'AUD').
    :type base: str
    :param target: The target currency code (e.g., 'CHF', 'EUR').
    :type target: str

    :return: The exchange rate as a float number.
    :rtype: float
    """
    if base not in CODES or target not in CODES:
        raise ValueError("Invalid currency code.")

    if base == target:
        return 1.0

    year, month, day = localtime()[:3]
    current_date = f"{year:04d}-{month:02d}-{day:02d}"
    url = f"https://api.frankfurter.dev/v1/{current_date}?base={base}&symbols={target}"

    try:
        response = get(url)
        data = response.json()
        return data["rates"].get(target, 0.0)
    except OSError as err:
        print(f"[ERROR] Network error while fetching exchange rate: {err}")
        return 0.0
    except Exception as err:
        raise Exception(f"Failed to fetch exchange rate: {err}")
