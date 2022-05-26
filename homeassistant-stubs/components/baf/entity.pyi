from _typeshed import Incomplete
from aiobafi6 import Device as Device
from homeassistant.core import callback as callback
from homeassistant.helpers.device_registry import format_mac as format_mac
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo, Entity as Entity

class BAFEntity(Entity):
    _attr_should_poll: bool
    _device: Incomplete
    _attr_unique_id: Incomplete
    _attr_name: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, device: Device, name: str) -> None: ...
    _attr_available: Incomplete
    def _async_update_attrs(self) -> None: ...
    def _async_update_from_device(self, device: Device) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
