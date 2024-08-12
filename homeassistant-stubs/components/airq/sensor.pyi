from . import AirQConfigEntry as AirQConfigEntry, AirQCoordinator as AirQCoordinator
from .const import ACTIVITY_BECQUEREL_PER_CUBIC_METER as ACTIVITY_BECQUEREL_PER_CUBIC_METER, CONCENTRATION_GRAMS_PER_CUBIC_METER as CONCENTRATION_GRAMS_PER_CUBIC_METER
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import CONCENTRATION_MICROGRAMS_PER_CUBIC_METER as CONCENTRATION_MICROGRAMS_PER_CUBIC_METER, CONCENTRATION_MILLIGRAMS_PER_CUBIC_METER as CONCENTRATION_MILLIGRAMS_PER_CUBIC_METER, CONCENTRATION_PARTS_PER_BILLION as CONCENTRATION_PARTS_PER_BILLION, CONCENTRATION_PARTS_PER_MILLION as CONCENTRATION_PARTS_PER_MILLION, PERCENTAGE as PERCENTAGE, UnitOfPressure as UnitOfPressure, UnitOfSoundPressure as UnitOfSoundPressure, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

_LOGGER: Incomplete

@dataclass(frozen=True, kw_only=True)
class AirQEntityDescription(SensorEntityDescription):
    value: Callable[[dict], float | int | None]
    def __init__(self, *, key, device_class=..., entity_category=..., entity_registry_enabled_default=..., entity_registry_visible_default=..., force_update=..., icon=..., has_entity_name=..., name=..., translation_key=..., translation_placeholders=..., unit_of_measurement=..., last_reset=..., native_unit_of_measurement=..., options=..., state_class=..., suggested_display_precision=..., suggested_unit_of_measurement=..., value) -> None: ...

SENSOR_TYPES: list[AirQEntityDescription]

async def async_setup_entry(hass: HomeAssistant, entry: AirQConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class AirQSensor(CoordinatorEntity, SensorEntity):
    _attr_has_entity_name: bool
    entity_description: Incomplete
    _attr_device_info: Incomplete
    _attr_unique_id: Incomplete
    _attr_native_value: Incomplete
    def __init__(self, coordinator: AirQCoordinator, description: AirQEntityDescription) -> None: ...
    def _handle_coordinator_update(self) -> None: ...
