# -*- coding: utf-8 -*-
from bot import post_message
from cbar import cbar_data_with_difference


def get_message_text():
    cbar_data = cbar_data_with_difference()
    currency_date = cbar_data["ValCurs"]["@Date"]
    msg = f"{currency_date} tarixindən etibarən"
    for currency in cbar_data["ValCurs"]["ValType"][1]["Valute"]:
        if currency["@Code"] in ("USD", "EUR", "GEL", "GBP", "RUB", "TRY"):
            msg += "\n{} {} = {:.4f} AZN ({:+.4f})".format(
                currency["Nominal"],
                currency["@Code"],
                float(currency["Value"]),
                currency["difference"],
            )
    msg += "\n<a href='https://www.cbar.az/currency/rates'><i>tam siyahı...</i></a>"
    return msg


def main():
    msg = get_message_text()
    post_message(msg)


if __name__ == "__main__":
    main()
