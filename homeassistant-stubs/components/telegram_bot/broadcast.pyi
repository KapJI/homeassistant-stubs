from .bot import BaseTelegramBot as BaseTelegramBot, TelegramBotConfigEntry as TelegramBotConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from telegram import Bot as Bot

async def async_setup_platform(hass: HomeAssistant, bot: Bot, config: TelegramBotConfigEntry) -> type[BaseTelegramBot] | None: ...
