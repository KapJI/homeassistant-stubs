from _typeshed import Incomplete
from aio_ownet.proxy import OWServerStatelessProxy as OWServerStatelessProxy
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import Entity as Entity, EntityDescription as EntityDescription
from typing import Any

_LOGGER: Incomplete

class OneWireEntity(Entity):
    _attr_has_entity_name: bool
    entity_description: Incomplete
    _last_update_success: bool
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    _device_file: Incomplete
    _state: str | None
    _owproxy: Incomplete
    def __init__(self, description: EntityDescription, device_id: str, device_info: DeviceInfo, device_file: str, owproxy: OWServerStatelessProxy) -> None: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any] | None: ...
    async def _write_value(self, value: bytes) -> None: ...
    async def async_update(self) -> None: ...
