from .const import UPTIME_DEVIATION as UPTIME_DEVIATION
from .coordinator import SmConfigEntry as SmConfigEntry, SmDataUpdateCoordinator as SmDataUpdateCoordinator
from .entity import SmEntity as SmEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from datetime import datetime
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import EntityCategory as EntityCategory, UnitOfInformation as UnitOfInformation, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.util.dt import utcnow as utcnow
from pysmlight import Info as Info, Sensors as Sensors

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class SmSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[Sensors], float | None]

@dataclass(frozen=True, kw_only=True)
class SmInfoEntityDescription(SensorEntityDescription):
    value_fn: Callable[[Info, int], StateType]

INFO: list[SmInfoEntityDescription]
RADIO_INFO: Incomplete
SENSORS: list[SmSensorEntityDescription]
EXTRA_SENSOR: Incomplete
UPTIME: list[SmSensorEntityDescription]

async def async_setup_entry(hass: HomeAssistant, entry: SmConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class SmSensorEntity(SmEntity, SensorEntity):
    coordinator: SmDataUpdateCoordinator
    entity_description: SmSensorEntityDescription
    _attr_entity_category: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: SmDataUpdateCoordinator, description: SmSensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> datetime | str | float | None: ...

class SmInfoSensorEntity(SmEntity, SensorEntity):
    coordinator: SmDataUpdateCoordinator
    entity_description: SmInfoEntityDescription
    _attr_entity_category: Incomplete
    idx: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: SmDataUpdateCoordinator, description: SmInfoEntityDescription, idx: int = 0) -> None: ...
    @property
    def native_value(self) -> StateType: ...

class SmUptimeSensorEntity(SmSensorEntity):
    _last_uptime: datetime | None
    def __init__(self, coordinator: SmDataUpdateCoordinator, description: SmSensorEntityDescription) -> None: ...
    def get_uptime(self, uptime: float | None) -> datetime | None: ...
    @property
    def native_value(self) -> datetime | None: ...
