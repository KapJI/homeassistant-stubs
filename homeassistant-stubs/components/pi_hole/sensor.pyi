from . import PiHoleConfigEntry as PiHoleConfigEntry
from .entity import PiHoleEntity as PiHoleEntity
from _typeshed import Incomplete
from collections.abc import Mapping
from hole import Hole as Hole
from homeassistant.components.sensor import SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.const import CONF_NAME as CONF_NAME, PERCENTAGE as PERCENTAGE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator
from typing import Any

SENSOR_TYPES: tuple[SensorEntityDescription, ...]
SENSOR_TYPES_V6: tuple[SensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: PiHoleConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class PiHoleSensor(PiHoleEntity, SensorEntity):
    entity_description: SensorEntityDescription
    _attr_has_entity_name: bool
    _attr_unique_id: Incomplete
    def __init__(self, api: Hole, coordinator: DataUpdateCoordinator[None], name: str, server_unique_id: str, description: SensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> StateType: ...

def get_nested(data: Mapping[str, Any], key: str) -> float | int: ...
