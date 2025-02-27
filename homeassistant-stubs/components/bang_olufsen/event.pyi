from . import BangOlufsenConfigEntry as BangOlufsenConfigEntry
from .const import CONNECTION_STATUS as CONNECTION_STATUS, DEVICE_BUTTONS as DEVICE_BUTTONS, DEVICE_BUTTON_EVENTS as DEVICE_BUTTON_EVENTS, MODEL_SUPPORT_DEVICE_BUTTONS as MODEL_SUPPORT_DEVICE_BUTTONS, MODEL_SUPPORT_MAP as MODEL_SUPPORT_MAP, WebsocketNotification as WebsocketNotification
from .entity import BangOlufsenEntity as BangOlufsenEntity
from _typeshed import Incomplete
from homeassistant.components.event import EventDeviceClass as EventDeviceClass, EventEntity as EventEntity
from homeassistant.const import CONF_MODEL as CONF_MODEL
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, config_entry: BangOlufsenConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class BangOlufsenButtonEvent(BangOlufsenEntity, EventEntity):
    _attr_device_class: Incomplete
    _attr_entity_registry_enabled_default: bool
    _attr_event_types = DEVICE_BUTTON_EVENTS
    _attr_unique_id: Incomplete
    _attr_translation_key: Incomplete
    _button_type: Incomplete
    def __init__(self, config_entry: BangOlufsenConfigEntry, button_type: str) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    @callback
    def _async_handle_event(self, event: str) -> None: ...
