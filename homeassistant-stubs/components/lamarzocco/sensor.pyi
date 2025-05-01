from .coordinator import LaMarzoccoConfigEntry as LaMarzoccoConfigEntry
from .entity import LaMarzoccoEntity as LaMarzoccoEntity, LaMarzoccoEntityDescription as LaMarzoccoEntityDescription
from collections.abc import Callable as Callable
from dataclasses import dataclass
from datetime import datetime
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from pylamarzocco.const import WidgetType
from pylamarzocco.models import BaseWidgetOutput as BaseWidgetOutput

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class LaMarzoccoSensorEntityDescription(LaMarzoccoEntityDescription, SensorEntityDescription):
    value_fn: Callable[[dict[WidgetType, BaseWidgetOutput]], StateType | datetime | None]

ENTITIES: tuple[LaMarzoccoSensorEntityDescription, ...]
STATISTIC_ENTITIES: tuple[LaMarzoccoSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: LaMarzoccoConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class LaMarzoccoSensorEntity(LaMarzoccoEntity, SensorEntity):
    entity_description: LaMarzoccoSensorEntityDescription
    @property
    def native_value(self) -> StateType | datetime | None: ...

class LaMarzoccoStatisticSensorEntity(LaMarzoccoSensorEntity):
    @property
    def native_value(self) -> StateType | datetime | None: ...
