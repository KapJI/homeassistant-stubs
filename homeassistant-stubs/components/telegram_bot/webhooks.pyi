from .bot import BaseTelegramBot as BaseTelegramBot, TelegramBotConfigEntry as TelegramBotConfigEntry
from .const import CONF_TRUSTED_NETWORKS as CONF_TRUSTED_NETWORKS
from _typeshed import Incomplete
from aiohttp.web_response import Response as Response
from homeassistant.components.http import HomeAssistantRequest as HomeAssistantRequest, HomeAssistantView as HomeAssistantView
from homeassistant.const import CONF_URL as CONF_URL
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.network import get_url as get_url
from ipaddress import IPv4Network
from telegram import Bot as Bot
from telegram.ext import Application as Application

_LOGGER: Incomplete
TELEGRAM_WEBHOOK_URL: str
REMOVE_WEBHOOK_URL: str
SECRET_TOKEN_LENGTH: int

async def async_setup_platform(hass: HomeAssistant, bot: Bot, config: TelegramBotConfigEntry) -> BaseTelegramBot | None: ...
def _get_trusted_networks(config: TelegramBotConfigEntry) -> list[IPv4Network]: ...

class PushBot(BaseTelegramBot):
    bot: Incomplete
    trusted_networks: Incomplete
    secret_token: Incomplete
    application: Incomplete
    base_url: Incomplete
    webhook_url: Incomplete
    def __init__(self, hass: HomeAssistant, bot: Bot, config: TelegramBotConfigEntry, secret_token: str) -> None: ...
    async def shutdown(self) -> None: ...
    async def _try_to_set_webhook(self) -> bool: ...
    async def start_application(self) -> None: ...
    async def register_webhook(self) -> bool: ...
    async def stop_application(self) -> None: ...
    async def deregister_webhook(self) -> None: ...

class PushBotView(HomeAssistantView):
    requires_auth: bool
    url = TELEGRAM_WEBHOOK_URL
    name: str
    hass: Incomplete
    bot: Incomplete
    application: Incomplete
    trusted_networks: Incomplete
    secret_token: Incomplete
    def __init__(self, hass: HomeAssistant, bot: Bot, application: Application, trusted_networks: list[IPv4Network], secret_token: str) -> None: ...
    async def post(self, request: HomeAssistantRequest) -> Response | None: ...
