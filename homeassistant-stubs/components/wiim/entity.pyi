from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.helpers.entity import Entity as Entity
from typing import override
from wiim.wiim_device import WiimDevice as WiimDevice

class WiimBaseEntity(Entity):
    _attr_has_entity_name: bool
    _device: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, wiim_device: WiimDevice) -> None: ...
    @property
    @override
    def available(self) -> bool: ...
