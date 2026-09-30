from _typeshed import Incomplete
from homeassistant.core import callback as callback
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import Entity as Entity
from lyngdorf import LyngdorfReceiver as LyngdorfReceiver
from typing import override

class LyngdorfEntity(Entity):
    _attr_has_entity_name: bool
    _attr_available: bool
    _attr_should_poll: bool
    _receiver: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, receiver: LyngdorfReceiver, device_info: DeviceInfo) -> None: ...
    @override
    async def async_added_to_hass(self) -> None: ...
    @callback
    def _handle_receiver_update(self) -> None: ...
    @callback
    def _update_availability(self) -> None: ...
