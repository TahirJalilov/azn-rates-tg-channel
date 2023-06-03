"""Module for working with bot."""

import requests

from config import BOT_TOKEN, TG_CHANNELS


def send_message(text: str) -> None:
    """Send message to the channel.

    Args:
        text: text for message.
    """
    for chat_id in TG_CHANNELS:
        requests.get(
            f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
            params={
                "chat_id": chat_id,
                "text": text,
                "parse_mode": "HTML",
                "disable_web_page_preview": True,
            },
        )
