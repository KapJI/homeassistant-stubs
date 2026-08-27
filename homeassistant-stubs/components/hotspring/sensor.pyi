from .coordinator import HotSpringConfigEntry as HotSpringConfigEntry, HotSpringDataUpdateCoordinator as HotSpringDataUpdateCoordinator
from .entity import HotSpringEntity as HotSpringEntity
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import EntityCategory as EntityCategory, UnitOfTemperature as UnitOfTemperature, UnitOfTime as UnitOfTime
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from hotspring import Spa as Spa
from typing import override

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class HotSpringSensorEntityDescription(SensorEntityDescription):
    exists_fn: Callable[[Spa], bool] = ...
    value_fn: Callable[[Spa], StateType]

SENSORS: tuple[HotSpringSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: HotSpringConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class HotSpringSensorEntity(HotSpringEntity, SensorEntity):
    entity_description: HotSpringSensorEntityDescription
    def __init__(self, coordinator: HotSpringDataUpdateCoordinator, description: HotSpringSensorEntityDescription) -> None: ...
    @property
    @override
    def native_value(self) -> StateType: ...
