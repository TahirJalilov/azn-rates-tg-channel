"""Module for working with bot."""

import requests

from .config import BOT_TOKEN, TG_CHANNELS


def send_message(message_text: str) -> None:
    """Send message to the channel.

    Args:
        message_text: Text for the message.
    """
    for chat_id in TG_CHANNELS:
        try:
            response = requests.get(
                f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
                params={
                    "chat_id": chat_id,
                    "text": message_text,
                    "parse_mode": "HTML",
                    "disable_web_page_preview": True,
                },
            )
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"Failed to send message: {e}")
