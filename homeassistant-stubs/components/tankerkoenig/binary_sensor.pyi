from .coordinator import TankerkoenigConfigEntry as TankerkoenigConfigEntry, TankerkoenigDataUpdateCoordinator as TankerkoenigDataUpdateCoordinator
from .entity import TankerkoenigCoordinatorEntity as TankerkoenigCoordinatorEntity
from _typeshed import Incomplete
from aiotankerkoenig import PriceInfo as PriceInfo, Station as Station
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity
from homeassistant.const import ATTR_LATITUDE as ATTR_LATITUDE, ATTR_LONGITUDE as ATTR_LONGITUDE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

PARALLEL_UPDATES: int
_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: TankerkoenigConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class StationOpenBinarySensorEntity(TankerkoenigCoordinatorEntity, BinarySensorEntity):
    _attr_device_class: Incomplete
    _attr_translation_key: str
    _station_id: Incomplete
    _attr_unique_id: Incomplete
    _attr_extra_state_attributes: Incomplete
    def __init__(self, station: Station, coordinator: TankerkoenigDataUpdateCoordinator) -> None: ...
    @property
    def is_on(self) -> bool | None: ...
