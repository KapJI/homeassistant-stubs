from .const import READ_MODE_BOOL as READ_MODE_BOOL, READ_MODE_INT as READ_MODE_INT
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo, Entity as Entity, EntityDescription as EntityDescription
from homeassistant.helpers.typing import StateType as StateType
from pyownet import protocol
from typing import Any

class OneWireEntityDescription(EntityDescription):
    read_mode: Union[str, None]

_LOGGER: Any

class OneWireBaseEntity(Entity):
    entity_description: OneWireEntityDescription
    _attr_unique_id: Any
    _attr_device_info: Any
    _attr_name: Any
    _device_file: Any
    _state: Any
    _value_raw: Any
    def __init__(self, description: OneWireEntityDescription, device_id: str, device_info: DeviceInfo, device_file: str, name: str) -> None: ...
    @property
    def extra_state_attributes(self) -> Union[dict[str, Any], None]: ...

class OneWireProxyEntity(OneWireBaseEntity):
    _owproxy: Any
    def __init__(self, description: OneWireEntityDescription, device_id: str, device_info: DeviceInfo, device_file: str, name: str, owproxy: protocol._Proxy) -> None: ...
    def _read_value_ownet(self) -> str: ...
    def _write_value_ownet(self, value: bytes) -> None: ...
    _value_raw: Any
    _state: Any
    def update(self) -> None: ...
