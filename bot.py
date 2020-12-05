# -*- coding: utf-8 -*-

import requests

from config import BOT_TOKEN, CHANNEL


def post_message(text):
    requests.get(
        'https://api.telegram.org/bot{0}/sendMessage'.format(BOT_TOKEN),
        params={
            'chat_id': CHANNEL,
            'text': text,
            'parse_mode': 'HTML',
            'disable_web_page_preview': True,
        },
    )
