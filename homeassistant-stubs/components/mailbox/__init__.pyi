from aiohttp import web
from homeassistant.components.http import HomeAssistantView as HomeAssistantView
from homeassistant.const import HTTP_INTERNAL_SERVER_ERROR as HTTP_INTERNAL_SERVER_ERROR
from homeassistant.core import callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers import config_per_platform as config_per_platform, discovery as discovery
from homeassistant.helpers.entity import Entity as Entity
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.setup import async_prepare_setup_platform as async_prepare_setup_platform
from typing import Any

_LOGGER: Any
DOMAIN: str
EVENT: str
CONTENT_TYPE_MPEG: str
CONTENT_TYPE_NONE: str
SCAN_INTERVAL: Any

async def async_setup(hass, config): ...

class MailboxEntity(Entity):
    mailbox: Any
    message_count: int
    def __init__(self, mailbox) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    @property
    def state(self): ...
    @property
    def name(self): ...
    async def async_update(self) -> None: ...

class Mailbox:
    hass: Any
    name: Any
    def __init__(self, hass, name) -> None: ...
    def async_update(self) -> None: ...
    @property
    def media_type(self) -> None: ...
    @property
    def can_delete(self): ...
    @property
    def has_media(self): ...
    async def async_get_media(self, msgid) -> None: ...
    async def async_get_messages(self) -> None: ...
    async def async_delete(self, msgid) -> None: ...

class StreamError(Exception): ...

class MailboxView(HomeAssistantView):
    mailboxes: Any
    def __init__(self, mailboxes) -> None: ...
    def get_mailbox(self, platform): ...

class MailboxPlatformsView(MailboxView):
    url: str
    name: str
    async def get(self, request: web.Request) -> web.Response: ...

class MailboxMessageView(MailboxView):
    url: str
    name: str
    async def get(self, request, platform): ...

class MailboxDeleteView(MailboxView):
    url: str
    name: str
    async def delete(self, request, platform, msgid) -> None: ...

class MailboxMediaView(MailboxView):
    url: str
    name: str
    async def get(self, request, platform, msgid): ...
