from .coordinator import NRGkickConfigEntry as NRGkickConfigEntry, NRGkickData as NRGkickData, NRGkickDataUpdateCoordinator as NRGkickDataUpdateCoordinator
from .entity import NRGkickEntity as NRGkickEntity, get_nested_dict_value as get_nested_dict_value
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.binary_sensor import BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class NRGkickBinarySensorEntityDescription(BinarySensorEntityDescription):
    is_on_fn: Callable[[NRGkickData], bool | None]

BINARY_SENSORS: tuple[NRGkickBinarySensorEntityDescription, ...]

async def async_setup_entry(_hass: HomeAssistant, entry: NRGkickConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class NRGkickBinarySensor(NRGkickEntity, BinarySensorEntity):
    entity_description: NRGkickBinarySensorEntityDescription
    def __init__(self, coordinator: NRGkickDataUpdateCoordinator, entity_description: NRGkickBinarySensorEntityDescription) -> None: ...
    @property
    def is_on(self) -> bool | None: ...
