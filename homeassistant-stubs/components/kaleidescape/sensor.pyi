from . import KaleidescapeConfigEntry as KaleidescapeConfigEntry
from .entity import KaleidescapeEntity as KaleidescapeEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.const import EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from kaleidescape import Device as KaleidescapeDevice

@dataclass(frozen=True, kw_only=True)
class KaleidescapeSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[KaleidescapeDevice], StateType]

SENSOR_TYPES: tuple[KaleidescapeSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: KaleidescapeConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class KaleidescapeSensor(KaleidescapeEntity, SensorEntity):
    entity_description: KaleidescapeSensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, device: KaleidescapeDevice, entity_description: KaleidescapeSensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> StateType: ...
