import stookalert
from .const import CONF_PROVINCE as CONF_PROVINCE, DOMAIN as DOMAIN
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

SCAN_INTERVAL: Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class StookalertBinarySensor(BinarySensorEntity):
    _attr_attribution: str
    _attr_device_class: Any
    _client: Any
    _attr_name: Any
    _attr_unique_id: Any
    _attr_device_info: Any
    def __init__(self, client: stookalert.stookalert, entry: ConfigEntry) -> None: ...
    _attr_is_on: Any
    def update(self) -> None: ...
