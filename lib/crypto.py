from requests import get


def get_coin_price(name: str) -> float:
    """
    Fetches the current price of a cryptocurrency based on its name.

    :param name: The name of the cryptocurrency.
    :type name: str

    :return: The current price of the cryptocurrency in USD.
    :rtype: float
    """
    url = f"https://api.coincap.io/v2/assets/{name.lower()}"

    try:
        response = get(url)

        if response.status_code >= 400:
            print(f"[ERROR] Failed to fetch coin price for {name}: status {response.status_code}")
            return 0.0

        data = response.json()
        return float(data["data"]["priceUsd"])
    except OSError as err:
        print(f"[ERROR] Network error while fetching {name}: {err}")
        return 0.0
    except (ValueError, KeyError) as err:
        print(f"[ERROR] Failed to fetch coin price for {name}: {err}")
        return 0.0
