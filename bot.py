# -*- coding: utf-8 -*-
import requests
from config import CHANNEL, BOT_TOKEN


def post_message(text):
    requests.get(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        params=dict(
            chat_id=CHANNEL, text=text, parse_mode="HTML", disable_web_page_preview=True
        ),
    )
