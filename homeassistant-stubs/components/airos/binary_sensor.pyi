from .coordinator import AirOS8Data as AirOS8Data, AirOSConfigEntry as AirOSConfigEntry, AirOSDataUpdateCoordinator as AirOSDataUpdateCoordinator
from .entity import AirOSEntity as AirOSEntity
from _typeshed import Incomplete
from airos.data import AirOSDataBaseClass
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Generic, TypeVar

PARALLEL_UPDATES: int
AirOSDataModel = TypeVar('AirOSDataModel', bound=AirOSDataBaseClass)

@dataclass(frozen=True, kw_only=True)
class AirOSBinarySensorEntityDescription(BinarySensorEntityDescription, Generic[AirOSDataModel]):
    value_fn: Callable[[AirOSDataModel], bool]
AirOS8BinarySensorEntityDescription = AirOSBinarySensorEntityDescription[AirOS8Data]
COMMON_BINARY_SENSORS: tuple[AirOSBinarySensorEntityDescription, ...]
AIROS8_BINARY_SENSORS: tuple[AirOS8BinarySensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, config_entry: AirOSConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class AirOSBinarySensor(AirOSEntity, BinarySensorEntity):
    entity_description: AirOSBinarySensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: AirOSDataUpdateCoordinator, description: AirOSBinarySensorEntityDescription) -> None: ...
    @property
    def is_on(self) -> bool: ...
