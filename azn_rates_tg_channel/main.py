# -*- coding: utf-8 -*-
"""Main module."""

from typing import Union

from azn_rates_tg_channel.bot import send_message
from azn_rates_tg_channel.cbar import currency_rates_with_diff


def generate_message() -> Union[str, bool]:
    """Generate message for telegram channel.

    Returns:
        msg: generated message text
    """
    rates = currency_rates_with_diff()
    try:
        rates_date = rates['@Date']
    except TypeError:
        return False
    msg = '<u>{0}</u> tarixindən etibarən:'.format(rates_date)
    for currency in rates['ValType'][1]['Valute']:
        if currency['@Code'] in {'USD', 'EUR', 'GEL', 'GBP', 'RUB', 'TRY'}:
            msg += '\n<pre>{0} {1} = {2:.4f} AZN ({3:+.4f})</pre>'.format(
                currency['Nominal'],
                currency['@Code'],
                float(currency['Value']),
                currency['diff'],
            )
    msg += '\n<a href="https://www.cbar.az/currency/rates?date={0}">' \
           '<i>tam siyahıya keçid</i></a>'.format(rates_date.replace('.', '/'))
    return msg


def main():
    """Run main functionality."""
    msg = generate_message()
    if msg:
        send_message(msg)


if __name__ == '__main__':
    main()
