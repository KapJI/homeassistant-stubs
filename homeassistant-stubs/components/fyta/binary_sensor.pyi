from .coordinator import FytaConfigEntry as FytaConfigEntry
from .entity import FytaPlantEntity as FytaPlantEntity
from collections.abc import Callable as Callable
from dataclasses import dataclass
from fyta_cli.fyta_models import Plant as Plant
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Final

@dataclass(frozen=True, kw_only=True)
class FytaBinarySensorEntityDescription(BinarySensorEntityDescription):
    value_fn: Callable[[Plant], bool]

BINARY_SENSORS: Final[list[FytaBinarySensorEntityDescription]]

async def async_setup_entry(hass: HomeAssistant, entry: FytaConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class FytaPlantBinarySensor(FytaPlantEntity, BinarySensorEntity):
    entity_description: FytaBinarySensorEntityDescription
    @property
    def is_on(self) -> bool: ...
