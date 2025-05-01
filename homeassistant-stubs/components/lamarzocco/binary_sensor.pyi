from .coordinator import LaMarzoccoConfigEntry as LaMarzoccoConfigEntry
from .entity import LaMarzoccoEntity as LaMarzoccoEntity, LaMarzoccoEntityDescription as LaMarzoccoEntityDescription
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from pylamarzocco import LaMarzoccoMachine as LaMarzoccoMachine

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class LaMarzoccoBinarySensorEntityDescription(LaMarzoccoEntityDescription, BinarySensorEntityDescription):
    is_on_fn: Callable[[LaMarzoccoMachine], bool | None]

ENTITIES: tuple[LaMarzoccoBinarySensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: LaMarzoccoConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class LaMarzoccoBinarySensorEntity(LaMarzoccoEntity, BinarySensorEntity):
    entity_description: LaMarzoccoBinarySensorEntityDescription
    @property
    def is_on(self) -> bool | None: ...
