"""Module for work with rates xml."""

from datetime import date

import requests
import xmltodict


def currency_rates_by_date(rates_date: date) -> dict | bool:
    """Get xml file with rates from cbar web page parse it and return as dictionary.

    Args:
        rates_date

    Returns:
        dict with rates or False
    """
    try:
        response = requests.get(
            f"https://cbar.az/currencies/{rates_date.strftime('%d.%m.%Y')}.xml",
        )
    except requests.exceptions.ConnectionError:
        return False
    currency_rates = xmltodict.parse(response.text)["ValCurs"]
    return currency_rates


def currency_rates_with_diff(currency_rates1: dict, currency_rates2: dict) -> dict:
    """Generate currency rates dictionary with calculated differences.

    Args:
        currency_rates1
        currency_rates2

    Returns:
        dict with rates and calculated differences or False
    """
    for rates in zip(
        currency_rates1["ValType"][1]["Valute"],
        currency_rates2["ValType"][1]["Valute"],
    ):
        rates[0]["diff"] = float(rates[0]["Value"]) - float(rates[1]["Value"])

    return currency_rates1
