from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components.infrared import async_send_command as async_send_command
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import STATE_UNAVAILABLE as STATE_UNAVAILABLE
from homeassistant.core import Event as Event, EventStateChangedData as EventStateChangedData, callback as callback
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import Entity as Entity
from homeassistant.helpers.event import async_track_state_change_event as async_track_state_change_event
from infrared_protocols.codes.lg.tv import LGTVCode as LGTVCode

_LOGGER: Incomplete

class LgIrEntity(Entity):
    _attr_has_entity_name: bool
    _infrared_entity_id: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, entry: ConfigEntry, infrared_entity_id: str, unique_id_suffix: str) -> None: ...
    _attr_available: Incomplete
    async def async_added_to_hass(self) -> None: ...
    async def _send_command(self, code: LGTVCode) -> None: ...
