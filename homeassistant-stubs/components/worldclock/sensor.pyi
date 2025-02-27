from .const import CONF_TIME_FORMAT as CONF_TIME_FORMAT, DOMAIN as DOMAIN
from _typeshed import Incomplete
from datetime import tzinfo
from homeassistant.components.sensor import SensorEntity as SensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_NAME as CONF_NAME, CONF_TIME_ZONE as CONF_TIME_ZONE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class WorldClockSensor(SensorEntity):
    _attr_icon: str
    _attr_has_entity_name: bool
    _attr_name: Incomplete
    _time_zone: Incomplete
    _time_format: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, time_zone: tzinfo | None, name: str, time_format: str, unique_id: str) -> None: ...
    _attr_native_value: Incomplete
    async def async_update(self) -> None: ...
