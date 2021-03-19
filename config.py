# -*- coding: utf-8 -*-
"""Load variables from .env and create some configs"""

import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN: str = os.getenv('BOT_TOKEN')
ADMINS: list = list(map(int, os.getenv('ADMINS').split(',')))
TG_CHANNELS: list = list(map(int, os.getenv('TG_CHANNELS').split(',')))
