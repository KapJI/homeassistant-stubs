from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo, Entity as Entity
from velbusaio.channels import Channel as VelbusChannel

class VelbusEntity(Entity):
    _attr_should_poll: bool
    _channel: Incomplete
    _attr_name: Incomplete
    _attr_device_info: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, channel: VelbusChannel) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def _on_update(self) -> None: ...
