from . import broadcast as broadcast, polling as polling, webhooks as webhooks
from .bot import BaseTelegramBot as BaseTelegramBot, TelegramBotConfigEntry as TelegramBotConfigEntry, TelegramNotificationService as TelegramNotificationService, initialize_bot as initialize_bot
from .const import ATTR_CHAT_ID as ATTR_CHAT_ID, ATTR_DISABLE_NOTIF as ATTR_DISABLE_NOTIF, ATTR_DISABLE_WEB_PREV as ATTR_DISABLE_WEB_PREV, ATTR_MESSAGE_TAG as ATTR_MESSAGE_TAG, ATTR_MESSAGE_THREAD_ID as ATTR_MESSAGE_THREAD_ID, ATTR_PARSER as ATTR_PARSER, CONF_API_ENDPOINT as CONF_API_ENDPOINT, CONF_CHAT_ID as CONF_CHAT_ID, DEFAULT_API_ENDPOINT as DEFAULT_API_ENDPOINT, DOMAIN as DOMAIN, PLATFORM_BROADCAST as PLATFORM_BROADCAST, PLATFORM_POLLING as PLATFORM_POLLING, PLATFORM_WEBHOOKS as PLATFORM_WEBHOOKS
from .log_filter import async_redact_token as async_redact_token, async_unredact_token as async_unredact_token
from .services import async_setup_services as async_setup_services
from _typeshed import Incomplete
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_PLATFORM as CONF_PLATFORM, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers import device_registry as dr
from homeassistant.helpers.typing import ConfigType as ConfigType
from telegram import Bot as Bot
from typing import Protocol

_LOGGER: Incomplete
CONFIG_SCHEMA: Incomplete

class BotPlatformModule(Protocol):
    async def async_setup_bot_platform(self, hass: HomeAssistant, bot: Bot, config: TelegramBotConfigEntry) -> BaseTelegramBot | None: ...

MODULES: Incomplete
PLATFORMS: list[Platform]

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_migrate_entry(hass: HomeAssistant, config_entry: TelegramBotConfigEntry) -> bool: ...
def bot_device_info(config_entry: TelegramBotConfigEntry, bot_id: int) -> dr.DeviceInfo: ...
async def async_setup_entry(hass: HomeAssistant, entry: TelegramBotConfigEntry) -> bool: ...
async def update_listener(hass: HomeAssistant, entry: TelegramBotConfigEntry) -> None: ...
async def async_unload_entry(hass: HomeAssistant, entry: TelegramBotConfigEntry) -> bool: ...
