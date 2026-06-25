from .const import SUBENTRY_TYPE_VELOV_STATION as SUBENTRY_TYPE_VELOV_STATION
from .coordinator import DataGrandLyonConfigEntry as DataGrandLyonConfigEntry
from .entity import DataGrandLyonVelovEntity as DataGrandLyonVelovEntity
from homeassistant.components.binary_sensor import BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import override

PARALLEL_UPDATES: int
VELOV_BINARY_SENSOR_DESCRIPTIONS: tuple[BinarySensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: DataGrandLyonConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class DataGrandLyonVelovBinarySensor(DataGrandLyonVelovEntity, BinarySensorEntity):
    @property
    @override
    def is_on(self) -> bool: ...
