# -*- coding: utf-8 -*-
"""Module for working with bot."""

import requests
import toml

config = toml.load('config.toml')
token = config['bot']['token']
channels = config['channels']['name']


def send_message(text: str) -> None:
    """Send message to the channel.

    Args:
        text: text of message
    """
    for chat_id in channels:
        requests.get(
            'https://api.telegram.org/bot{0}/sendMessage'.format(token),
            params={
                'chat_id': chat_id,
                'text': text,
                'parse_mode': 'HTML',
                'disable_web_page_preview': True,
            },
        )
