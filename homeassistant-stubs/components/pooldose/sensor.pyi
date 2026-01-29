from . import PooldoseConfigEntry as PooldoseConfigEntry
from .const import UNIT_MAPPING as UNIT_MAPPING
from .entity import PooldoseEntity as PooldoseEntity
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import CONCENTRATION_PARTS_PER_MILLION as CONCENTRATION_PARTS_PER_MILLION, EntityCategory as EntityCategory, UnitOfElectricPotential as UnitOfElectricPotential, UnitOfTime as UnitOfTime
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

_LOGGER: Incomplete
PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class PooldoseSensorEntityDescription(SensorEntityDescription):
    use_unit_conversion: bool = ...

SENSOR_DESCRIPTIONS: tuple[PooldoseSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, config_entry: PooldoseConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class PooldoseSensor(PooldoseEntity, SensorEntity):
    entity_description: PooldoseSensorEntityDescription
    @property
    def native_value(self) -> float | int | str | None: ...
    @property
    def native_unit_of_measurement(self) -> str | None: ...
