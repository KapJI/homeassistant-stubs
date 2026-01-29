from .const import DOMAIN as DOMAIN, MANUFACTURER as MANUFACTURER
from .coordinator import PooldoseCoordinator as PooldoseCoordinator
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine
from homeassistant.const import CONF_MAC as CONF_MAC
from homeassistant.exceptions import ServiceValidationError as ServiceValidationError
from homeassistant.helpers.device_registry import CONNECTION_NETWORK_MAC as CONNECTION_NETWORK_MAC, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from pooldose.type_definitions import DeviceInfoDict as DeviceInfoDict, ValueDict as ValueDict
from typing import Any, Literal

def device_info(info: DeviceInfoDict | None, unique_id: str, mac: str | None = None) -> DeviceInfo: ...

class PooldoseEntity(CoordinatorEntity[PooldoseCoordinator]):
    _attr_has_entity_name: bool
    entity_description: Incomplete
    platform_name: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: PooldoseCoordinator, serial_number: str, device_properties: DeviceInfoDict, entity_description: EntityDescription, platform_name: Literal['sensor', 'switch', 'number', 'binary_sensor', 'select']) -> None: ...
    @property
    def available(self) -> bool: ...
    def get_data(self) -> ValueDict | None: ...
    async def _async_perform_write(self, api_call: Callable[[str, Any], Coroutine[Any, Any, bool]], key: str, value: bool | str | float) -> None: ...
