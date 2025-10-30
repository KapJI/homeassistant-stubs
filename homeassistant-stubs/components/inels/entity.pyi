from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import Entity as Entity
from inelsmqtt.devices import Device as Device

class InelsBaseEntity(Entity):
    _attr_should_poll: bool
    _attr_has_entity_name: bool
    _device: Incomplete
    _device_id: Incomplete
    _attr_unique_id: Incomplete
    _key: Incomplete
    _index: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, device: Device, key: str, index: int) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    def _callback(self) -> None: ...
    @property
    def available(self) -> bool: ...
