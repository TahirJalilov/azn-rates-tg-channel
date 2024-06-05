"""Main module for azn-rates-tg-channel project."""

import schedule
import time

from datetime import date, timedelta

from azn_rates import cbar
from azn_rates.bot import send_message

# Configurable constants
POLLING_INTERVAL = 20  # seconds
SCHEDULED_TIME = "09:05"  # Asia/Baku timezone


def generate_post_text(rates) -> str:
    """Generate post text for the Telegram channel."""
    text = f"<u>{rates['@Date']}</u> tarixindən etibarən:"
    for currency in rates["ValType"][1]["Valute"]:
        if currency["@Code"] in {"USD", "EUR", "GEL", "GBP", "RUB", "TRY"}:
            text += "\n<code>{0} {1} = {2:.4f} AZN ({3:+.4f})</code>".format(
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
    for _ in range(POLLING_INTERVAL):
        today_rates = cbar.currency_rates_by_date(date.today())
        yesterday_rates = cbar.currency_rates_by_date(date.today() - timedelta(days=1))
        if today_rates == yesterday_rates:
            time.sleep(60)
            continue
        else:
            currency_rates = cbar.currency_rates_with_diff(today_rates, yesterday_rates)
            post_text = generate_post_text(currency_rates)
            send_message(post_text)
            break


if __name__ == "__main__":
    schedule.every().day.at(SCHEDULED_TIME, "Asia/Baku").do(main)

    while True:
        schedule.run_pending()
        time.sleep(1)
