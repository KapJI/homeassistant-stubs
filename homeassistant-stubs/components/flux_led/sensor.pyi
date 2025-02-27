from .coordinator import FluxLedConfigEntry as FluxLedConfigEntry
from .entity import FluxEntity as FluxEntity
from _typeshed import Incomplete
from homeassistant.components.sensor import SensorEntity as SensorEntity
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

async def async_setup_entry(hass: HomeAssistant, entry: FluxLedConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class FluxPairedRemotes(FluxEntity, SensorEntity):
    _attr_entity_category: Incomplete
    _attr_translation_key: str
    @property
    def native_value(self) -> int: ...
