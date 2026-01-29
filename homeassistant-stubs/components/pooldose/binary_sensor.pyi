from . import PooldoseConfigEntry as PooldoseConfigEntry
from .entity import PooldoseEntity as PooldoseEntity
from _typeshed import Incomplete
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

_LOGGER: Incomplete
PARALLEL_UPDATES: int
BINARY_SENSOR_DESCRIPTIONS: tuple[BinarySensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, config_entry: PooldoseConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class PooldoseBinarySensor(PooldoseEntity, BinarySensorEntity):
    @property
    def is_on(self) -> bool: ...
