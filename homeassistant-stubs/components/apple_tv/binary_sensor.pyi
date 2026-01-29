from . import AppleTvConfigEntry as AppleTvConfigEntry
from .entity import AppleTVEntity as AppleTVEntity
from _typeshed import Incomplete
from homeassistant.components.binary_sensor import BinarySensorEntity as BinarySensorEntity
from homeassistant.const import CONF_NAME as CONF_NAME
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from pyatv.const import KeyboardFocusState
from pyatv.interface import AppleTV as AppleTV, KeyboardListener

async def async_setup_entry(hass: HomeAssistant, config_entry: AppleTvConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class AppleTVKeyboardFocused(AppleTVEntity, BinarySensorEntity, KeyboardListener):
    _attr_translation_key: str
    _attr_available: bool
    @callback
    def async_device_connected(self, atv: AppleTV) -> None: ...
    @callback
    def async_device_disconnected(self) -> None: ...
    def focusstate_update(self, old_state: KeyboardFocusState, new_state: KeyboardFocusState) -> None: ...
    _attr_is_on: Incomplete
    def _update_state(self, new_state: bool) -> None: ...
