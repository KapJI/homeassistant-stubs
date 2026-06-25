from .coordinator import StreamlabsConfigEntry as StreamlabsConfigEntry, StreamlabsCoordinator as StreamlabsCoordinator
from .entity import StreamlabsWaterEntity as StreamlabsWaterEntity
from homeassistant.components.binary_sensor import BinarySensorEntity as BinarySensorEntity
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import override

async def async_setup_entry(hass: HomeAssistant, entry: StreamlabsConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class StreamlabsAwayMode(StreamlabsWaterEntity, BinarySensorEntity):
    _attr_translation_key: str
    def __init__(self, coordinator: StreamlabsCoordinator, location_id: str) -> None: ...
    @property
    @override
    def is_on(self) -> bool: ...
