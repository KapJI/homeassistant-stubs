from .coordinator import OpenEVSEConfigEntry as OpenEVSEConfigEntry
from .entity import OpenEVSEEntity as OpenEVSEEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from datetime import datetime
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE, SIGNAL_STRENGTH_DECIBELS as SIGNAL_STRENGTH_DECIBELS, UnitOfElectricCurrent as UnitOfElectricCurrent, UnitOfElectricPotential as UnitOfElectricPotential, UnitOfEnergy as UnitOfEnergy, UnitOfInformation as UnitOfInformation, UnitOfLength as UnitOfLength, UnitOfPower as UnitOfPower, UnitOfTemperature as UnitOfTemperature, UnitOfTime as UnitOfTime
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.util import slugify as slugify
from openevsehttp.__main__ import OpenEVSE as OpenEVSE
from typing import override

_LOGGER: Incomplete
PARALLEL_UPDATES: int
STATUS_OPTIONS: list[str]

def _map_status(status: str | None) -> str | None: ...

@dataclass(frozen=True, kw_only=True)
class OpenEVSESensorDescription(SensorEntityDescription):
    value_fn: Callable[[OpenEVSE], str | float | datetime | None]

SENSOR_TYPES: tuple[OpenEVSESensorDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: OpenEVSEConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class OpenEVSESensor(OpenEVSEEntity, SensorEntity):
    entity_description: OpenEVSESensorDescription
    @property
    @override
    def native_value(self) -> StateType | datetime: ...
