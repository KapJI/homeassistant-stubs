from .const import DOMAIN as DOMAIN, _LOGGER as _LOGGER
from .coordinator import AmazonConfigEntry as AmazonConfigEntry
from .entity import AmazonEntity as AmazonEntity
from .utils import async_update_unique_id as async_update_unique_id
from _typeshed import Incomplete
from aioamazondevices.structures import AmazonDevice as AmazonDevice
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Final

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class AmazonBinarySensorEntityDescription(BinarySensorEntityDescription):
    is_on_fn: Callable[[AmazonDevice, str], bool]
    is_supported: Callable[[AmazonDevice, str], bool] = ...
    is_available_fn: Callable[[AmazonDevice, str], bool] = ...

BINARY_SENSORS: Final[Incomplete]
DEPRECATED_BINARY_SENSORS: Final[Incomplete]

async def async_setup_entry(hass: HomeAssistant, entry: AmazonConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class AmazonBinarySensorEntity(AmazonEntity, BinarySensorEntity):
    entity_description: AmazonBinarySensorEntityDescription
    @property
    def is_on(self) -> bool: ...
    @property
    def available(self) -> bool: ...
