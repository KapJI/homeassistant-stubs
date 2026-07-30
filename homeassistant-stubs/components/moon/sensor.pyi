from .const import DOMAIN as DOMAIN
from .helpers import MOON_PHASES as MOON_PHASES, moon_phase as moon_phase
from _typeshed import Incomplete
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class MoonSensorEntity(SensorEntity):
    _attr_has_entity_name: bool
    _attr_device_class: Incomplete
    _attr_options: Incomplete
    _attr_translation_key: str
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, entry: ConfigEntry) -> None: ...
    _attr_native_value: Incomplete
    async def async_update(self) -> None: ...
