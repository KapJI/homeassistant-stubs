from .bridge import SamsungTVBridge as SamsungTVBridge
from .const import CONF_MANUFACTURER as CONF_MANUFACTURER, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_MAC as CONF_MAC, CONF_MODEL as CONF_MODEL, CONF_NAME as CONF_NAME
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import Entity as Entity

class SamsungTVEntity(Entity):
    _attr_has_entity_name: bool
    _bridge: Incomplete
    _mac: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, *, bridge: SamsungTVBridge, config_entry: ConfigEntry) -> None: ...
