from .const import MieleAppliance as MieleAppliance
from .coordinator import MieleConfigEntry as MieleConfigEntry
from .entity import MieleEntity as MieleEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from pymiele import MieleDevice as MieleDevice
from typing import Final

PARALLEL_UPDATES: int
_LOGGER: Incomplete

@dataclass(frozen=True, kw_only=True)
class MieleBinarySensorDescription(BinarySensorEntityDescription):
    value_fn: Callable[[MieleDevice], StateType]

@dataclass
class MieleBinarySensorDefinition:
    types: tuple[MieleAppliance, ...]
    description: MieleBinarySensorDescription

BINARY_SENSOR_TYPES: Final[tuple[MieleBinarySensorDefinition, ...]]

async def async_setup_entry(hass: HomeAssistant, config_entry: MieleConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class MieleBinarySensor(MieleEntity, BinarySensorEntity):
    entity_description: MieleBinarySensorDescription
    @property
    def is_on(self) -> bool | None: ...
