from . import AbodeSystem as AbodeSystem
from .const import DOMAIN as DOMAIN
from .entity import AbodeDevice as AbodeDevice
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import LIGHT_LUX as LIGHT_LUX, PERCENTAGE as PERCENTAGE, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from jaraco.abode.devices.sensor import Sensor as Sensor

ABODE_TEMPERATURE_UNIT_HA_UNIT: Incomplete

@dataclass(frozen=True, kw_only=True)
class AbodeSensorDescription(SensorEntityDescription):
    value_fn: Callable[[Sensor], float]
    native_unit_of_measurement_fn: Callable[[Sensor], str]
    def __init__(self, *, key, device_class=..., entity_category=..., entity_registry_enabled_default=..., entity_registry_visible_default=..., force_update=..., icon=..., has_entity_name=..., name=..., translation_key=..., translation_placeholders=..., unit_of_measurement=..., last_reset=..., native_unit_of_measurement=..., options=..., state_class=..., suggested_display_precision=..., suggested_unit_of_measurement=..., value_fn, native_unit_of_measurement_fn) -> None: ...

SENSOR_TYPES: tuple[AbodeSensorDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class AbodeSensor(AbodeDevice, SensorEntity):
    entity_description: AbodeSensorDescription
    _device: Sensor
    _attr_unique_id: Incomplete
    def __init__(self, data: AbodeSystem, device: Sensor, description: AbodeSensorDescription) -> None: ...
    @property
    def native_value(self) -> float: ...
    @property
    def native_unit_of_measurement(self) -> str: ...
