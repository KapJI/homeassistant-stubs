from .api import async_api_call as async_api_call
from .const import DOMAIN as DOMAIN
from .coordinator import NRGkickDataUpdateCoordinator as NRGkickDataUpdateCoordinator
from _typeshed import Incomplete
from collections.abc import Awaitable
from homeassistant.const import CONF_HOST as CONF_HOST
from homeassistant.helpers.device_registry import CONNECTION_NETWORK_MAC as CONNECTION_NETWORK_MAC, DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

class NRGkickEntity(CoordinatorEntity[NRGkickDataUpdateCoordinator]):
    _attr_has_entity_name: bool
    _key: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: NRGkickDataUpdateCoordinator, key: str) -> None: ...
    async def _async_call_api[_T](self, awaitable: Awaitable[_T]) -> _T: ...
