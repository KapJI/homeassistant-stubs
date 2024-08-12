from . import ElgatorConfigEntry as ElgatorConfigEntry
from .coordinator import ElgatoData as ElgatoData, ElgatoDataUpdateCoordinator as ElgatoDataUpdateCoordinator
from .entity import ElgatoEntity as ElgatoEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE, UnitOfElectricCurrent as UnitOfElectricCurrent, UnitOfElectricPotential as UnitOfElectricPotential, UnitOfPower as UnitOfPower
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

@dataclass(frozen=True, kw_only=True)
class ElgatoSensorEntityDescription(SensorEntityDescription):
    has_fn: Callable[[ElgatoData], bool] = ...
    value_fn: Callable[[ElgatoData], float | int | None]
    def __init__(self, *, key, device_class=..., entity_category=..., entity_registry_enabled_default=..., entity_registry_visible_default=..., force_update=..., icon=..., has_entity_name=..., name=..., translation_key=..., translation_placeholders=..., unit_of_measurement=..., last_reset=..., native_unit_of_measurement=..., options=..., state_class=..., suggested_display_precision=..., suggested_unit_of_measurement=..., has_fn=..., value_fn) -> None: ...

SENSORS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ElgatorConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ElgatoSensorEntity(ElgatoEntity, SensorEntity):
    entity_description: ElgatoSensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: ElgatoDataUpdateCoordinator, description: ElgatoSensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> float | int | None: ...
