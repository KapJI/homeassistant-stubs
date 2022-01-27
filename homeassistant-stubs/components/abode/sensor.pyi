from . import AbodeDevice as AbodeDevice, AbodeSystem as AbodeSystem
from .const import DOMAIN as DOMAIN
from abodepy.devices.sensor import AbodeSensor as AbodeSense
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

SENSOR_TYPES: tuple[SensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class AbodeSensor(AbodeDevice, SensorEntity):
    _device: AbodeSense
    entity_description: Any
    _attr_name: Any
    _attr_unique_id: Any
    _attr_native_unit_of_measurement: Any
    def __init__(self, data: AbodeSystem, device: AbodeSense, description: SensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> Union[float, None]: ...
