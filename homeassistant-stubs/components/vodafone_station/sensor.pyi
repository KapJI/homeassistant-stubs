from .const import LINE_TYPES as LINE_TYPES, _LOGGER as _LOGGER
from .coordinator import VodafoneConfigEntry as VodafoneConfigEntry, VodafoneStationRouter as VodafoneStationRouter
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from datetime import datetime
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.const import EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE, UnitOfDataRate as UnitOfDataRate
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Final

PARALLEL_UPDATES: int
NOT_AVAILABLE: list
UPTIME_DEVIATION: int

@dataclass(frozen=True, kw_only=True)
class VodafoneStationEntityDescription(SensorEntityDescription):
    value: Callable[[VodafoneStationRouter, str | datetime | float | None, str], str | datetime | float | None] = ...
    is_suitable: Callable[[dict], bool] = ...

def _calculate_uptime(coordinator: VodafoneStationRouter, last_value: str | datetime | float | None, key: str) -> datetime: ...
def _line_connection(coordinator: VodafoneStationRouter, last_value: str | datetime | float | None, key: str) -> str | None: ...

SENSOR_TYPES: Final[Incomplete]

async def async_setup_entry(hass: HomeAssistant, entry: VodafoneConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class VodafoneStationSensorEntity(CoordinatorEntity[VodafoneStationRouter], SensorEntity):
    _attr_has_entity_name: bool
    entity_description: VodafoneStationEntityDescription
    _attr_device_info: Incomplete
    _attr_unique_id: Incomplete
    _old_state: str | datetime | float | None
    def __init__(self, coordinator: VodafoneStationRouter, description: VodafoneStationEntityDescription) -> None: ...
    @property
    def native_value(self) -> str | datetime | float | None: ...
