from . import BeoConfigEntry as BeoConfigEntry
from .const import BEO_REMOTE_KEY_EVENTS as BEO_REMOTE_KEY_EVENTS, BeoModel as BeoModel, CONNECTION_STATUS as CONNECTION_STATUS, DEVICE_BUTTON_EVENTS as DEVICE_BUTTON_EVENTS, DOMAIN as DOMAIN, MANUFACTURER as MANUFACTURER, WebsocketNotification as WebsocketNotification
from .entity import BeoEntity as BeoEntity
from .util import get_device_buttons as get_device_buttons, get_remote_keys as get_remote_keys, get_remotes as get_remotes
from _typeshed import Incomplete
from homeassistant.components.event import EventDeviceClass as EventDeviceClass, EventEntity as EventEntity
from homeassistant.const import CONF_MODEL as CONF_MODEL
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from mozart_api.models import PairedRemote as PairedRemote

PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, config_entry: BeoConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class BeoEvent(BeoEntity, EventEntity):
    _attr_device_class: Incomplete
    _attr_entity_registry_enabled_default: bool
    def __init__(self, config_entry: BeoConfigEntry) -> None: ...
    @callback
    def _async_handle_event(self, event: str) -> None: ...

class BeoButtonEvent(BeoEvent):
    _attr_event_types = DEVICE_BUTTON_EVENTS
    _attr_unique_id: Incomplete
    _attr_translation_key: Incomplete
    _button_type: Incomplete
    def __init__(self, config_entry: BeoConfigEntry, button_type: str) -> None: ...
    async def async_added_to_hass(self) -> None: ...

class BeoRemoteKeyEvent(BeoEvent):
    _attr_event_types = BEO_REMOTE_KEY_EVENTS
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    _attr_translation_key: Incomplete
    _key_type: Incomplete
    def __init__(self, config_entry: BeoConfigEntry, remote: PairedRemote, key_type: str) -> None: ...
    async def async_added_to_hass(self) -> None: ...
