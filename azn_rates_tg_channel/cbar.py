"""Module for work with rates xml."""

from datetime import datetime, timedelta
from typing import Union

import requests
import xmltodict


def _get_xml_with_rates(date: datetime) -> Union[str, bool]:
    """Get xml file from cbar web page.

    Args:
        date: date of rates

    Returns:
        xml file as text or False
    """
    response = requests.get(
        f"https://www.cbar.az/currencies/{date.strftime('%d.%m.%Y')}.xml",
    )
    if not response.text.startswith("<?xml"):
        return False
    return response.text


def currency_rates_by_date(date: datetime) -> Union[dict, bool]:
    """Get dictionary with rates.

    Args:
        date: date of rates

    Returns:
        dict with rates or False
    """
    xml = _get_xml_with_rates(date)
    try:
        currency_rates = xmltodict.parse(xml)
    except TypeError:
        return False
    else:
        return currency_rates["ValCurs"]


def currency_rates_with_diff() -> Union[dict, bool]:
    """Get dictionary with rates and calculated differences.

    Returns:
        dict with rates and calculated differences or False
    """
    rates_today = currency_rates_by_date(datetime.today())
    rates_yesterday = currency_rates_by_date(
        datetime.today() - timedelta(days=1),
    )
    if rates_today["@Date"] == rates_yesterday["@Date"]:
        return False
    for rates in zip(
        rates_today["ValType"][1]["Valute"],
        rates_yesterday["ValType"][1]["Valute"],
    ):
        rates[0]["diff"] = float(rates[0]["Value"]) - float(rates[1]["Value"])

    return rates_today
