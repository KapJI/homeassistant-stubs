from . import SmConfigEntry as SmConfigEntry
from .const import UPTIME_DEVIATION as UPTIME_DEVIATION
from .coordinator import SmDataUpdateCoordinator as SmDataUpdateCoordinator
from .entity import SmEntity as SmEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from datetime import datetime
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import EntityCategory as EntityCategory, UnitOfInformation as UnitOfInformation, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.util.dt import utcnow as utcnow
from pysmlight import Info as Info, Sensors as Sensors

@dataclass(frozen=True, kw_only=True)
class SmSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[Sensors], float | None]
    def __init__(self, *, key, device_class=..., entity_category=..., entity_registry_enabled_default=..., entity_registry_visible_default=..., force_update=..., icon=..., has_entity_name=..., name=..., translation_key=..., translation_placeholders=..., unit_of_measurement=..., last_reset=..., native_unit_of_measurement=..., options=..., state_class=..., suggested_display_precision=..., suggested_unit_of_measurement=..., value_fn) -> None: ...

@dataclass(frozen=True, kw_only=True)
class SmInfoEntityDescription(SensorEntityDescription):
    value_fn: Callable[[Info], StateType]
    def __init__(self, *, key, device_class=..., entity_category=..., entity_registry_enabled_default=..., entity_registry_visible_default=..., force_update=..., icon=..., has_entity_name=..., name=..., translation_key=..., translation_placeholders=..., unit_of_measurement=..., last_reset=..., native_unit_of_measurement=..., options=..., state_class=..., suggested_display_precision=..., suggested_unit_of_measurement=..., value_fn) -> None: ...

INFO: list[SmInfoEntityDescription]
SENSORS: list[SmSensorEntityDescription]
UPTIME: list[SmSensorEntityDescription]

async def async_setup_entry(hass: HomeAssistant, entry: SmConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

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
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: SmDataUpdateCoordinator, description: SmInfoEntityDescription) -> None: ...
    @property
    def native_value(self) -> StateType: ...

class SmUptimeSensorEntity(SmSensorEntity):
    _last_uptime: Incomplete
    def __init__(self, coordinator: SmDataUpdateCoordinator, description: SmSensorEntityDescription) -> None: ...
    def get_uptime(self, uptime: float | None) -> datetime | None: ...
    @property
    def native_value(self) -> datetime | None: ...
