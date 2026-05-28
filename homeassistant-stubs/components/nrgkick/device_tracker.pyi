from .coordinator import NRGkickConfigEntry as NRGkickConfigEntry, NRGkickDataUpdateCoordinator as NRGkickDataUpdateCoordinator
from .entity import NRGkickEntity as NRGkickEntity, get_nested_dict_value as get_nested_dict_value
from homeassistant.components.device_tracker import TrackerEntity as TrackerEntity
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Final

PARALLEL_UPDATES: int
TRACKER_KEY: Final[str]

async def async_setup_entry(_hass: HomeAssistant, entry: NRGkickConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class NRGkickDeviceTracker(NRGkickEntity, TrackerEntity):
    _attr_translation_key = TRACKER_KEY
    def __init__(self, coordinator: NRGkickDataUpdateCoordinator) -> None: ...
    def _gps_float(self, key: str) -> float | None: ...
    @property
    def latitude(self) -> float | None: ...
    @property
    def longitude(self) -> float | None: ...
    @property
    def location_accuracy(self) -> float: ...
