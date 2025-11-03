from .const import SIGNAL_UPDATE_EVENT as SIGNAL_UPDATE_EVENT
from telegram import Bot as Bot

def signal(bot: Bot) -> str: ...
