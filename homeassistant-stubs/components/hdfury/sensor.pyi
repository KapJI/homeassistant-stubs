from .coordinator import HDFuryConfigEntry as HDFuryConfigEntry
from .entity import HDFuryEntity as HDFuryEntity
from homeassistant.components.sensor import SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

PARALLEL_UPDATES: int
SENSORS: tuple[SensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: HDFuryConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class HDFurySensor(HDFuryEntity, SensorEntity):
    entity_description: SensorEntityDescription
    @property
    def native_value(self) -> str: ...
