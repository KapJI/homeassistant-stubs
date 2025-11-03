from .bot import TelegramBotConfigEntry as TelegramBotConfigEntry
from .const import EVENT_TELEGRAM_ATTACHMENT as EVENT_TELEGRAM_ATTACHMENT, EVENT_TELEGRAM_CALLBACK as EVENT_TELEGRAM_CALLBACK, EVENT_TELEGRAM_COMMAND as EVENT_TELEGRAM_COMMAND, EVENT_TELEGRAM_SENT as EVENT_TELEGRAM_SENT, EVENT_TELEGRAM_TEXT as EVENT_TELEGRAM_TEXT
from .entity import TelegramBotEntity as TelegramBotEntity
from .helpers import signal as signal
from _typeshed import Incomplete
from homeassistant.components.event import EventEntity as EventEntity, EventEntityDescription as EventEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any

async def async_setup_entry(hass: HomeAssistant, config_entry: TelegramBotConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class TelegramBotEventEntity(TelegramBotEntity, EventEntity):
    _attr_event_types: Incomplete
    def __init__(self, config_entry: TelegramBotConfigEntry) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    @callback
    def _async_handle_event(self, event_type: str, event_data: dict[str, Any]) -> None: ...
