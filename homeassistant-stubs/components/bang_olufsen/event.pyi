from . import BangOlufsenConfigEntry as BangOlufsenConfigEntry
from .const import BEO_REMOTE_CONTROL_KEYS as BEO_REMOTE_CONTROL_KEYS, BEO_REMOTE_KEYS as BEO_REMOTE_KEYS, BEO_REMOTE_KEY_EVENTS as BEO_REMOTE_KEY_EVENTS, BEO_REMOTE_SUBMENU_CONTROL as BEO_REMOTE_SUBMENU_CONTROL, BEO_REMOTE_SUBMENU_LIGHT as BEO_REMOTE_SUBMENU_LIGHT, BangOlufsenModel as BangOlufsenModel, CONNECTION_STATUS as CONNECTION_STATUS, DEVICE_BUTTON_EVENTS as DEVICE_BUTTON_EVENTS, DOMAIN as DOMAIN, MANUFACTURER as MANUFACTURER, WebsocketNotification as WebsocketNotification
from .entity import BangOlufsenEntity as BangOlufsenEntity
from .util import get_device_buttons as get_device_buttons, get_remotes as get_remotes
from _typeshed import Incomplete
from homeassistant.components.event import EventDeviceClass as EventDeviceClass, EventEntity as EventEntity
from homeassistant.const import CONF_MODEL as CONF_MODEL
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from mozart_api.models import PairedRemote as PairedRemote

PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, config_entry: BangOlufsenConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class BangOlufsenEvent(BangOlufsenEntity, EventEntity):
    _attr_device_class: Incomplete
    _attr_entity_registry_enabled_default: bool
    def __init__(self, config_entry: BangOlufsenConfigEntry) -> None: ...
    @callback
    def _async_handle_event(self, event: str) -> None: ...

class BangOlufsenButtonEvent(BangOlufsenEvent):
    _attr_event_types = DEVICE_BUTTON_EVENTS
    _attr_unique_id: Incomplete
    _attr_translation_key: Incomplete
    _button_type: Incomplete
    def __init__(self, config_entry: BangOlufsenConfigEntry, button_type: str) -> None: ...
    async def async_added_to_hass(self) -> None: ...

class BangOlufsenRemoteKeyEvent(BangOlufsenEvent):
    _attr_event_types = BEO_REMOTE_KEY_EVENTS
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    _attr_translation_key: Incomplete
    _key_type: Incomplete
    def __init__(self, config_entry: BangOlufsenConfigEntry, remote: PairedRemote, key_type: str) -> None: ...
    async def async_added_to_hass(self) -> None: ...
