from _typeshed import Incomplete
from aiohttp import web
from homeassistant.components import frontend as frontend
from homeassistant.components.http import HomeAssistantView as HomeAssistantView
from homeassistant.config import config_per_platform as config_per_platform
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers import discovery as discovery
from homeassistant.helpers.entity import Entity as Entity
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.helpers.issue_registry import IssueSeverity as IssueSeverity, async_create_issue as async_create_issue
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from homeassistant.setup import async_prepare_setup_platform as async_prepare_setup_platform
from typing import Any, Final

_LOGGER: Incomplete
DOMAIN: Final[str]
EVENT: Final[str]
CONTENT_TYPE_MPEG: Final[str]
CONTENT_TYPE_NONE: Final[str]
SCAN_INTERVAL: Incomplete
CONFIG_SCHEMA: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...

class MailboxEntity(Entity):
    mailbox: Incomplete
    message_count: int
    def __init__(self, mailbox: Mailbox) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    @property
    def state(self) -> str: ...
    @property
    def name(self) -> str: ...
    async def async_update(self) -> None: ...

class Mailbox:
    hass: Incomplete
    name: Incomplete
    def __init__(self, hass: HomeAssistant, name: str) -> None: ...
    def async_update(self) -> None: ...
    @property
    def media_type(self) -> str: ...
    @property
    def can_delete(self) -> bool: ...
    @property
    def has_media(self) -> bool: ...
    async def async_get_media(self, msgid: str) -> bytes: ...
    async def async_get_messages(self) -> list[dict[str, Any]]: ...
    async def async_delete(self, msgid: str) -> bool: ...

class StreamError(Exception): ...

class MailboxView(HomeAssistantView):
    mailboxes: Incomplete
    def __init__(self, mailboxes: list[Mailbox]) -> None: ...
    def get_mailbox(self, platform: str) -> Mailbox: ...

class MailboxPlatformsView(MailboxView):
    url: str
    name: str
    async def get(self, request: web.Request) -> web.Response: ...

class MailboxMessageView(MailboxView):
    url: str
    name: str
    async def get(self, request: web.Request, platform: str) -> web.Response: ...

class MailboxDeleteView(MailboxView):
    url: str
    name: str
    async def delete(self, request: web.Request, platform: str, msgid: str) -> None: ...

class MailboxMediaView(MailboxView):
    url: str
    name: str
    async def get(self, request: web.Request, platform: str, msgid: str) -> web.Response: ...
