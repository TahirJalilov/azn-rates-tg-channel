# -*- coding: utf-8 -*-
from typing import Union

from bot import post_message
from cbar import cbar_data_with_difference


def get_message_text() -> Union[str, bool]:
    cbar_data = cbar_data_with_difference()
    try:
        currency_date = cbar_data['ValCurs']['@Date']
    except TypeError:
        return False
    msg = '{0} tarixindən etibarən'.format(currency_date)
    for currency in cbar_data['ValCurs']['ValType'][1]['Valute']:
        if currency['@Code'] in {'USD', 'EUR', 'GEL', 'GBP', 'RUB', 'TRY'}:
            msg += '\n{0} {1} = {2:.4f} AZN ({3:+.4f})'.format(
                currency['Nominal'],
                currency['@Code'],
                float(currency['Value']),
                currency['difference'],
            )
    msg += (
        '\n<a href="https://www.cbar.az/currency/rates"><i>tam siyahıya keçid</i></a>'
    )
    return msg


def main():
    msg = get_message_text()
    if msg:
        post_message(msg)


if __name__ == '__main__':
    main()
