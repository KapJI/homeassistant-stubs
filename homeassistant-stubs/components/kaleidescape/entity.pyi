from homeassistant.core import callback as callback
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo, Entity as Entity
from kaleidescape import Device as KaleidescapeDevice
from typing import Any

_LOGGER: Any

class KaleidescapeEntity(Entity):
    _device: Any
    _attr_should_poll: bool
    _attr_unique_id: Any
    _attr_name: Any
    _attr_device_info: Any
    def __init__(self, device: KaleidescapeDevice) -> None: ...
    async def async_added_to_hass(self) -> None: ...
