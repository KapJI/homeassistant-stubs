from .const import DOMAIN as DOMAIN
from .coordinator import GatusConfigEntry as GatusConfigEntry, GatusDataUpdateCoordinator as GatusDataUpdateCoordinator
from _typeshed import Incomplete
from gatus_api import EndpointStatus as EndpointStatus, Result as Result
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import override

PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, entry: GatusConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class GatusEndpointBinarySensor(CoordinatorEntity[GatusDataUpdateCoordinator], BinarySensorEntity):
    _attr_device_class: Incomplete
    _attr_has_entity_name: bool
    _attr_name: Incomplete
    _endpoint_key: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: GatusDataUpdateCoordinator, entry: GatusConfigEntry, endpoint_key: str) -> None: ...
    @property
    @override
    def is_on(self) -> bool | None: ...
    @property
    @override
    def available(self) -> bool: ...
    @property
    def endpoint_data(self) -> EndpointStatus: ...
    @property
    def latest_result(self) -> Result | None: ...
