"""Main module."""

import schedule
import time

from datetime import date, timedelta

from azn_rates_tg_channel import cbar
from azn_rates_tg_channel.bot import send_message


def generate_post_text(rates) -> str:
    """Generate post text for telegram channel.

    Returns:
        text: generated post text
    """
    text = f"<u>{rates['@Date']}</u> tarixindən etibarən:"
    for currency in rates["ValType"][1]["Valute"]:
        if currency["@Code"] in {"USD", "EUR", "GEL", "GBP", "RUB", "TRY"}:
            text += "\n<pre>{0} {1} = {2:.4f} AZN ({3:+.4f})</pre>".format(
                currency["Nominal"],
                currency["@Code"],
                float(currency["Value"]),
                currency["diff"],
            )
    text += (
        '\n<a href="https://www.cbar.az/currency/rates?date={0}">'
        "<i>tam siyahıya keçid</i></a>".format(rates['@Date'].replace(".", "/"))
    )
    return text


def main():
    for _ in range(20):
        rates_today = cbar.currency_rates_by_date(date.today())
        rates_yesterday = cbar.currency_rates_by_date(date.today() - timedelta(days=1))
        if rates_today == rates_yesterday:
            time.sleep(60)
            continue
        else:
            currency_rates = cbar.currency_rates_with_diff(rates_today, rates_yesterday)
            post_text = generate_post_text(currency_rates)
            send_message(post_text)
            break


if __name__ == "__main__":
    schedule.every().day.at("09:05", "Asia/Baku").do(main)

    while True:
        schedule.run_pending()
        time.sleep(1)
