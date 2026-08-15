from .const import HEALTH as HEALTH, RESOURCE as RESOURCE
from .coordinator import MikrotikConfigEntry as MikrotikConfigEntry
from .entity import MikrotikEntity as MikrotikEntity
from _typeshed import Incomplete
from dataclasses import dataclass
from datetime import datetime
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import EntityCategory as EntityCategory, UnitOfElectricPotential as UnitOfElectricPotential, UnitOfRatio as UnitOfRatio, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from typing import Final, override

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class MikrotikSensorEntityDescription(SensorEntityDescription):
    type: str

SENSORS: Final[Incomplete]

async def async_setup_entry(hass: HomeAssistant, entry: MikrotikConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class MikrotikSensorEntity(MikrotikEntity[MikrotikSensorEntityDescription], SensorEntity):
    entity_description: MikrotikSensorEntityDescription
    @property
    @override
    def native_value(self) -> StateType | datetime: ...
