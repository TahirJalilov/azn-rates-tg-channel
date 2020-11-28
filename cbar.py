# -*- coding: utf-8 -*-
from typing import Union
import requests
import xmltodict
from datetime import datetime, timedelta
from itertools import product


def get_xml_from_cbar(date: datetime) -> Union[str, bool]:
    r = requests.get(f"https://www.cbar.az/currencies/{date.strftime('%d.%m.%Y')}.xml")
    if not r.text.startswith("<?xml"):
        return False
    return r.text


def cbar_data_by_date(date: datetime) -> Union[dict, bool]:
    xml = get_xml_from_cbar(date)
    try:
        cbar_data = xmltodict.parse(xml)
    except TypeError:
        return False
    else:
        return cbar_data


def cbar_data_with_difference() -> Union[dict, bool]:
    cbar_data_today = cbar_data_by_date(datetime.today())
    cbar_data_yesterday = cbar_data_by_date(datetime.today() - timedelta(days=1))
    if cbar_data_today["ValCurs"]["@Date"] == cbar_data_yesterday["ValCurs"]["@Date"]:
        return False
    for currency_today, currency_yesterday in product(
        cbar_data_today["ValCurs"]["ValType"][1]["Valute"],
        cbar_data_yesterday["ValCurs"]["ValType"][1]["Valute"],
    ):
        if currency_today["@Code"] == currency_yesterday["@Code"]:
            currency_today["difference"] = float(currency_today["Value"]) - float(
                currency_yesterday["Value"]
            )
    return cbar_data_today
