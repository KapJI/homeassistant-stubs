from .const import DOMAIN as DOMAIN
from .coordinator import GatusConfigEntry as GatusConfigEntry, GatusDataUpdateCoordinator as GatusDataUpdateCoordinator
from _typeshed import Incomplete
from gatus_api import EndpointStatus as EndpointStatus, Result as Result
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import override

class GatusEndpointEntity(CoordinatorEntity[GatusDataUpdateCoordinator]):
    _attr_has_entity_name: bool
    _endpoint_key: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: GatusDataUpdateCoordinator, entry: GatusConfigEntry, endpoint_key: str) -> None: ...
    @property
    @override
    def available(self) -> bool: ...
    @property
    def endpoint_data(self) -> EndpointStatus: ...
    @property
    def latest_result(self) -> Result | None: ...
