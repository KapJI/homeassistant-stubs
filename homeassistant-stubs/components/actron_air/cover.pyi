from .coordinator import ActronAirConfigEntry as ActronAirConfigEntry, ActronAirSystemCoordinator as ActronAirSystemCoordinator
from .entity import ActronAirZoneEntity as ActronAirZoneEntity
from _typeshed import Incomplete
from actron_neo_api import ActronAirZone as ActronAirZone
from homeassistant.components.cover import CoverDeviceClass as CoverDeviceClass, CoverEntity as CoverEntity, CoverEntityFeature as CoverEntityFeature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import override

PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, entry: ActronAirConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class ActronAirZoneDamper(ActronAirZoneEntity, CoverEntity):
    _attr_device_class: Incomplete
    _attr_translation_key: str
    _attr_supported_features: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: ActronAirSystemCoordinator, zone: ActronAirZone) -> None: ...
    @property
    @override
    def current_cover_position(self) -> int: ...
    @property
    @override
    def is_closed(self) -> bool: ...
