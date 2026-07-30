import aiopulse
from .const import DOMAIN as DOMAIN, LOGGER as LOGGER
from _typeshed import Incomplete
from homeassistant.core import callback as callback
from homeassistant.helpers import device_registry as dr, entity as entity
from typing import override

class AcmedaEntity(entity.Entity):
    _attr_should_poll: bool
    _attr_has_entity_name: bool
    roller: Incomplete
    def __init__(self, roller: aiopulse.Roller) -> None: ...
    @override
    async def async_added_to_hass(self) -> None: ...
    @override
    async def async_will_remove_from_hass(self) -> None: ...
    @callback
    def notify_update(self) -> None: ...
    @property
    @override
    def unique_id(self) -> str: ...
    @property
    def device_id(self) -> str: ...
    @property
    @override
    def device_info(self) -> dr.DeviceInfo: ...
