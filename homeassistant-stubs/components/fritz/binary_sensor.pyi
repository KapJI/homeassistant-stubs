from .coordinator import ConnectionInfo as ConnectionInfo, FritzConfigEntry as FritzConfigEntry
from .entity import FritzBoxBaseCoordinatorEntity as FritzBoxBaseCoordinatorEntity, FritzEntityDescription as FritzEntityDescription
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

_LOGGER: Incomplete
PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class FritzBinarySensorEntityDescription(BinarySensorEntityDescription, FritzEntityDescription):
    is_suitable: Callable[[ConnectionInfo], bool] = ...

SENSOR_TYPES: tuple[FritzBinarySensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: FritzConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class FritzBoxBinarySensor(FritzBoxBaseCoordinatorEntity, BinarySensorEntity):
    entity_description: FritzBinarySensorEntityDescription
    @property
    def is_on(self) -> bool | None: ...
