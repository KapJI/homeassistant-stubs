from . import NordPoolConfigEntry as NordPoolConfigEntry
from .const import CONF_AREAS as CONF_AREAS
from .coordinator import NordPoolDataUpdateCoordinator as NordPoolDataUpdateCoordinator
from .entity import NordpoolBaseEntity as NordpoolBaseEntity
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.binary_sensor import BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.components.sensor import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

PARALLEL_UPDATES: int

def get_tomorrow_price_available(entity: NordpoolPriceBinarySensor) -> bool: ...

@dataclass(frozen=True, kw_only=True)
class NordpoolBinarySensorEntityDescription(BinarySensorEntityDescription):
    value_fn: Callable[[NordpoolPriceBinarySensor], bool | None]

BINARY_SENSOR_TYPES: tuple[NordpoolBinarySensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: NordPoolConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class NordpoolPriceBinarySensor(NordpoolBaseEntity, BinarySensorEntity):
    entity_description: NordpoolBinarySensorEntityDescription
    def __init__(self, coordinator: NordPoolDataUpdateCoordinator, entity_description: NordpoolBinarySensorEntityDescription, area: str) -> None: ...
    @property
    def is_on(self) -> bool | None: ...
