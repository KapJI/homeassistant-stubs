import asyncio
from .const import CONF_MESSAGE as CONF_MESSAGE, CONF_PRIORITY as CONF_PRIORITY, CONF_TAGS as CONF_TAGS, CONF_TITLE as CONF_TITLE, CONF_TOPIC as CONF_TOPIC, DOMAIN as DOMAIN
from .coordinator import NtfyConfigEntry as NtfyConfigEntry
from .entity import NtfyBaseEntity as NtfyBaseEntity
from _typeshed import Incomplete
from aiontfy import Notification as Notification
from homeassistant.components.event import EventEntity as EventEntity, EventEntityDescription as EventEntityDescription
from homeassistant.config_entries import ConfigSubentry as ConfigSubentry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

_LOGGER: Incomplete
PARALLEL_UPDATES: int
RECONNECT_INTERVAL: int

async def async_setup_entry(hass: HomeAssistant, config_entry: NtfyConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class NtfyEventEntity(NtfyBaseEntity, EventEntity):
    entity_description: Incomplete
    _ws: asyncio.Task | None
    def __init__(self, config_entry: NtfyConfigEntry, subentry: ConfigSubentry) -> None: ...
    _attr_event_types: Incomplete
    @callback
    def _async_handle_event(self, notification: Notification) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    _attr_available: bool
    async def ws_connect(self) -> None: ...
    @property
    def entity_picture(self) -> str | None: ...
