from .coordinator import YotoConfigEntry as YotoConfigEntry, YotoDataUpdateCoordinator as YotoDataUpdateCoordinator
from .entity import YotoPlayerEntity as YotoPlayerEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from typing import override
from yoto_api import CardInsertionState, DayMode, YotoPlayer as YotoPlayer

PARALLEL_UPDATES: int

def _enum_state(value: CardInsertionState | None) -> str | None: ...
def _day_mode_state(value: DayMode | None) -> str | None: ...

@dataclass(frozen=True, kw_only=True)
class YotoSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[YotoPlayer], StateType]

SENSORS: tuple[YotoSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: YotoConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class YotoSensor(YotoPlayerEntity, SensorEntity):
    entity_description: YotoSensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: YotoDataUpdateCoordinator, player: YotoPlayer, description: YotoSensorEntityDescription) -> None: ...
    @property
    @override
    def native_value(self) -> StateType: ...
