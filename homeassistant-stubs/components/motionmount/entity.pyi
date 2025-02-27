import motionmount
from . import MotionMountConfigEntry as MotionMountConfigEntry
from .const import DOMAIN as DOMAIN, EMPTY_MAC as EMPTY_MAC
from _typeshed import Incomplete
from homeassistant.const import ATTR_CONNECTIONS as ATTR_CONNECTIONS, ATTR_IDENTIFIERS as ATTR_IDENTIFIERS, CONF_PIN as CONF_PIN
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo, format_mac as format_mac
from homeassistant.helpers.entity import Entity as Entity

_LOGGER: Incomplete

class MotionMountEntity(Entity):
    _attr_should_poll: bool
    _attr_has_entity_name: bool
    mm: Incomplete
    config_entry: Incomplete
    pin: Incomplete
    _base_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, mm: motionmount.MotionMount, config_entry: MotionMountConfigEntry) -> None: ...
    @property
    def available(self) -> bool: ...
    def update_name(self) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
