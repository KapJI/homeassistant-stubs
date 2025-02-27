from .coordinator import TechnoVEConfigEntry as TechnoVEConfigEntry, TechnoVEDataUpdateCoordinator as TechnoVEDataUpdateCoordinator
from .entity import TechnoVEEntity as TechnoVEEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from technove import Station as TechnoVEStation

@dataclass(frozen=True, kw_only=True)
class TechnoVEBinarySensorDescription(BinarySensorEntityDescription):
    value_fn: Callable[[TechnoVEStation], bool | None]

BINARY_SENSORS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: TechnoVEConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class TechnoVEBinarySensorEntity(TechnoVEEntity, BinarySensorEntity):
    entity_description: TechnoVEBinarySensorDescription
    def __init__(self, coordinator: TechnoVEDataUpdateCoordinator, description: TechnoVEBinarySensorDescription) -> None: ...
    @property
    def is_on(self) -> bool | None: ...
