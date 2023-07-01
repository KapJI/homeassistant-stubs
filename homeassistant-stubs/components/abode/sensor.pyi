from . import AbodeDevice as AbodeDevice, AbodeSystem as AbodeSystem
from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import LIGHT_LUX as LIGHT_LUX
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from jaraco.abode.devices.sensor import Sensor as AbodeSense

SENSOR_TYPES: tuple[SensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class AbodeSensor(AbodeDevice, SensorEntity):
    _device: AbodeSense
    entity_description: Incomplete
    _attr_unique_id: Incomplete
    _attr_native_unit_of_measurement: Incomplete
    def __init__(self, data: AbodeSystem, device: AbodeSense, description: SensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> float | None: ...
