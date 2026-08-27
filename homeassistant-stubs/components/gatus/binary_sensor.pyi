from .coordinator import GatusConfigEntry as GatusConfigEntry, GatusDataUpdateCoordinator as GatusDataUpdateCoordinator
from .entity import GatusEndpointEntity as GatusEndpointEntity
from _typeshed import Incomplete
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import override

PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, entry: GatusConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class GatusEndpointBinarySensor(GatusEndpointEntity, BinarySensorEntity):
    _attr_device_class: Incomplete
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: GatusDataUpdateCoordinator, entry: GatusConfigEntry, endpoint_key: str) -> None: ...
    @property
    @override
    def is_on(self) -> bool: ...
